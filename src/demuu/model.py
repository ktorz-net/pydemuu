# Core LibBbMm Wraps:
from . import clib as core

### Model Node (A node in a Dynamic Bayesian Network)
class Node():
    # Construction destruction:
    def __init__( self, model= None, iVar=0 ) -> None:
        self._model= model
        self._id= iVar
    
    # Accessor:
    def id(self):
        return self._id
    
    def name(self):
        return self._model._varNames[ self._id-1 ]

    def domain(self):
        return self._model._domains[ self._id-1 ]

    def parents(self):
        idParents= self._model._trans.parents( self._id ).asList()
        return [ self._model._varNames[ ip-1 ] for ip in idParents ]

    def distribution( self, configuration=[] ):
        return self._model.inode_distribution( self._id, configuration )
    
    def index(self, value):
        return self._model.inode_index( self._id, value )

    def value( self, index ):
        return self._model.inode_value( self._id, index )

    # Construction:
    def initialize( self, parents, defaultDistrib ):
        self._model.inode_initialize(
            self._id,
            self._model.nodeIds( parents ),
            defaultDistrib
        )
        return self
    
    def setConditionalDistribution( self, configuration, distribution ):
        self._model.inode_setConditionalDistribution( self._id, configuration, distribution )
        return self
    
    def create( self, parents, function ):
        self._model.inode_create(
            self._id,
            self._model.nodeIds( parents ),
            function
        )
        return self
    
    def createDeterministic( self, parents, function ):
        return self.create(
            parents,
            lambda configuration : [( function(configuration), 1.0 )]
        )

### Model Reward (A reward function to optimize)
class Reward():
    # Constructor / destruction:
    def __init__( self, model= None, iCrit=0 ) -> None:
        self._model= model
        self._id= iCrit
        self._coreCrit= model._rewards.criterion(self._id)
    
    # Accessor:
    def id(self):
        return self._id

    def parentIds(self):
        return  self._model._rewards.criterionParents( self._id )
    
    def parents(self):
        return [ self._model.domain(iNode) for iNode in  self.parentIds() ]
    
    def weight( self ):
        return self._model._rewards.weight( self._id )
    
    def outputs( self ):
        return self._coreCrit.outputs()

    # Construction:
    def initialize( self, parentsList, possibleValues ):
        self._model._rewards.criterion_intialize(
            self._id,
            self._model.nodeIds( parentsList ),
            possibleValues
        )
        return self
    
    def from_set( self, configuration, value ):
        codeConfig= self._model.digits( configuration, self.parentIds() )
        try:
            outputId= self.outputs().index( value )+1
        except ValueError:
            outputId= self._coreCrit.addValue( value )
    
        self._coreCrit.from_set( codeConfig, outputId )
        return outputId

    def setWeight( self, value ):
        return self._model._rewards.criterion_setWeight( self._id, value )

class Model():
    # Construction destruction:
    def __init__( self, stateVariables= {}, actionVariables= {}, shiftVariables= {}, numberOfCriteria=1 ) -> None:
        # Initialize variable enumeration :
        self._varNames= [ var+'-0' for var in stateVariables ]
        self._varNames+= [ var for var in actionVariables ]
        self._varNames+= [ var for var in shiftVariables ]
        self._varNames+= [ var+'-1' for var in stateVariables ]
        nbVariable= len(self._varNames)
        self._varIds= { name: i for name, i in zip( self._varNames, range(1, nbVariable+1) ) }
        
        # List Domains :
        self._domains= list(stateVariables.values()) + list(actionVariables.values()) + list(shiftVariables.values()) + list(stateVariables.values())

        # Transition function:
        nbStateVar= len(stateVariables)
        nbActVar= len(actionVariables)
        space= [len(d) for d in self._domains ]
        self._trans= core.Dynamic( space, nbStateVar+nbActVar, nbStateVar )
        
        # Rewards function:
        self._rewards= core.Evaluator( space, numberOfCriteria )

    # Accessor
    def stateDimention(self):
        return core.Dynamic( cdynamic=self._trans._cdynamic ).stateDimention()
    
    def actionDimention(self):
        return core.Dynamic( cdynamic=self._trans._cdynamic ).actionDimention()
    
    def shiftDimention(self):
        return core.Dynamic( cdynamic=self._trans._cdynamic ).shiftDimention()
    
    def nodes(self):
        return self._varNames

    def domains(self):
        return self._domains

    def domain(self, iNode):
        return self._domains[iNode-1]

    def node( self, variableName ):
        return Node( self, self._varIds[variableName] )
    
    def nodeIds( self, variableNames ):
        return [ self._varIds[name] for name in variableNames ]

    def numberOfCriteria( self ):
        return self._rewards.numberOfCriteria()

    def criterion( self, iCriterion=1 ):
        return Reward( self, iCriterion )
    
    # Node Accessor:
    def inode_index( self, iNode, value ):
        try :
            i= self._domains[ iNode-1 ].index(value)
            return i+1
        except :
            return 0

    def inode_value( self, iNode, index ):
        return self._domains[ iNode-1 ][index-1]
    
    def inode_distribution( self, iNode, configuration ):
        idParents= self._trans.parents( iNode ).asList()
        assert( len(idParents) == len(configuration) )
        condition= self._trans.node( iNode )
        digitConf= [ self._domains[p-1].index(val)+1 for p, val in zip(idParents, configuration) ]
        domain= self._domains[ iNode-1 ]
        return [ (domain[id-1], proba) for id, proba in condition.fromList( digitConf ) ]
    
    # Transformation (Values <-> Digits)
    def digits( self, values, iNodes= None ):
        if not iNodes :
            iNodes= [ i for i in range(1, len(values)+1) ]
        assert( len(values) == len(iNodes) )
        return [ self.inode_index(i, v) for i, v in zip( iNodes, values ) ]
    
    def values( self, digits, iNodes= None ):
        if not iNodes :
            iNodes= [ i for i in range(1, len(digits)+1) ]
        assert( len(digits) == len(iNodes) )
        return [ self.domain(i)[d-1] for i, d in zip( iNodes, digits ) ]
    
    # Node Construction:
    def inode_initialize( self, iNode, parentsIds, defaultExplicitDistrib ):
        domain= self._domains[ iNode-1 ]
        defaultDigitDistrib= [ (domain.index(val)+1, proba) for val, proba in defaultExplicitDistrib ]
        self._trans.node_setDependancy( iNode, parentsIds, defaultDigitDistrib )
    
    def inode_setConditionalDistribution( self, iNode, configuration, distribution ):
        condition= self._trans.node( iNode )
        idParents= self._trans.parents( iNode ).asList()
        digitConf= [ self._domains[p-1].index(val)+1 for p, val in zip(idParents, configuration) ]
        domain= self._domains[ iNode-1 ]
        digitDistrib= [ (domain.index(val)+1, proba) for val, proba in distribution ]
        condition.fromList_set( digitConf, digitDistrib )

    def inode_create( self, iNode, parentsIds, function ):
        depSize= len(parentsIds)
        parentsDoms= [ self._domains[ip-1] for ip in parentsIds ]
        domain= self._domains[ iNode-1 ]
        explicitDistrib= function( [ dom[0] for dom in parentsDoms ] )
        digitDistrib= [ (domain.index(val)+1, proba) for val, proba in explicitDistrib ]
        self._trans.node_setDependancy( iNode, parentsIds, digitDistrib )
        condition= self._trans.node( iNode )
        for digitConf in core.Code( [len(d) for d in parentsDoms] ) :
            explicitDistrib= function( [ dom[i-1] for i, dom in zip(digitConf, parentsDoms) ] )
            digitDistrib= [ (domain.index(val)+1, proba) for val, proba in explicitDistrib ]
            condition.fromList_set( digitConf, digitDistrib )

    # Process:
    def digitTransition( self, digitStates, digitActions ):
        return self._trans.processFrom( digitStates+digitActions ).asCodeValueList()
    
    def transition( self, state, action=[] ):
        digitInpout= self.digits( state+action )
        distribution= [
            (self.values( code ), proba)
            for code, proba in self._trans.processFrom( digitInpout ).asCodeValueList()
        ]
        return distribution
    
    def reward( self, state, action, futur ):
        shift= [1 for i in range( self.shiftDimention() ) ]
        digitConfig= self.digits( state+action+shift+futur )
        return self._rewards.process( digitConfig )

    # Dump & Load
    def dump( self ):
        stBound= self.stateDimention()
        acBound= stBound + self.actionDimention()
        shBound= acBound + self.shiftDimention()
        rewardDump= self._rewards.dump()

        descriptor= {
            'state': {},
            'action':{},
            'shift': {},
            'numberOfCriteria': rewardDump['numberOfCriteria'],
            'criteria': rewardDump['criteria']
        }

        for var in self._varNames[:stBound] :
            var= var.split('-')[0]
            n= self.node(var+'-1')
            descriptor['state'][var]= {
                "domain": list( n.domain() ),
                "parents": n.parents(),
                "condition": self._trans.node( n.id() ).dump()
            }
        
        for var in self._varNames[stBound:acBound] :
            n= self.node(var)
            descriptor['action'][var]= {
                "domain": list( n.domain() ),
                "parents": n.parents(),
                "condition": self._trans.node( n.id() ).dump()
            }

        for var in self._varNames[acBound:shBound] :
            n= self.node(var)
            descriptor['shift'][var]= {
                "domain": list( n.domain() ),
                "parents": n.parents(),
                "condition": self._trans.node( n.id() ).dump()
            }
        
        return descriptor
    
    #def load( self, descriptor ):
    #    self.initialize(  )
    #    return self