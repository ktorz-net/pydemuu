from .clibdemuu import c_digit
from . import clibdemuu as cc
from .code import Code
from .bench import Bench
from .tree import Tree
from .condition import Condition

class Dynamic:
    # Construction destruction:
    def __init__(self, space=[2, 2], inputDimention=1, outputDimention=1, cdynamic= None):
        if cdynamic is None :
            codeSpace= Code( space )
            self._cdynamic= cc.newDuDynamic(
                     codeSpace._ccode,
                     c_digit(inputDimention),
                     c_digit(outputDimention)
            )
            self._cmaster= True
        else: 
            self._cdynamic= cdynamic
            self._cmaster= False

    def __del__(self):
        if self._cmaster :
            cc.deleteDuDynamic( self._cdynamic )

    # Accessor
    def distribution( self ):
        return Bench( cbench= cc.DuDynamic_distribution( self._cdynamic ) )

    def inputDimention( self ):
        return cc.DuDynamic_inputDimention( self._cdynamic )
    
    def outputDimention( self ):
        return cc.DuDynamic_outputDimention( self._cdynamic )

    def shiftDimention( self ):
        return cc.DuDynamic_shiftDimention( self._cdynamic )
    
    def stateDimention( self ):
        return cc.DuDynamic_outputDimention( self._cdynamic )
    
    def actionDimention( self ):
        return cc.DuDynamic_inputDimention( self._cdynamic ) - cc.DuDynamic_outputDimention( self._cdynamic )

    def overallDimention( self ):
        return cc.DuDynamic_overallDimention( self._cdynamic )

    def node(self, iVar):
        return Condition( ccondition= cc.DuDynamic_node(
            self._cdynamic, c_digit(iVar) )
        )
    
    def parents( self, iVar ):
        return Code( ccode=cc.DuDynamic_node_parents(
            self._cdynamic, c_digit(iVar) )
        )
    def space( self ):
        return [ cc.DuDynamic_node_size( self._cdynamic, c_digit(i) ) for i in range( 1, self.inputDimention()+1 ) ]
    
    def inputs( self ):
        inputBound= self.inputDimention()+1
        return [ cc.DuDynamic_node_size( self._cdynamic, c_digit(i) ) for i in range( 1, inputBound ) ]
    
    def outputs( self ):
        overBound= self.overallDimention()+1
        outputStart= overBound - self.outputDimention()
        return [ cc.DuDynamic_node_size( self._cdynamic, c_digit(i) ) for i in range( outputStart, overBound ) ]
    
    def shifts( self ):
        inputBound= self.inputDimention()+1
        shiftBound= inputBound + self.shiftDimention()
        return [ cc.DuDynamic_node_size( self._cdynamic, c_digit(i) ) for i in range( inputBound, shiftBound ) ]
    
    # Construction :
    def initialize( self, inputs, outputs, shifts= [] ):
        spaceCode= Code( inputs+shifts+outputs )
        cc.DuDynamic_destroy( self._cdynamic )
        cc.DuDynamic_create(
            self._cdynamic,
            spaceCode._ccode,
            c_digit( len(inputs) ), c_digit( len(outputs) )
        )
        return self
    
    def node_setDependancyBm( self, iVar, parents, defaultDistrib ):
        assert( parents._cmaster and defaultDistrib._cmaster )
        assert( parents.dimention() > 0 )
        ccond= cc.DuDynamic_node_reinitWith_withDefault(
            self._cdynamic,
            c_digit(iVar),
            parents._ccode,
            defaultDistrib._cbench
        )
        parents._cmaster= False
        defaultDistrib._cmaster= False
        return Condition( ccondition= ccond )
         
    
    def node_setDependancy( self, iVar, parentList, defaultDistribList ):
        return self.node_setDependancyBm(
            iVar,
            Code( parentList ),
            Bench( [ ([o], [v]) for o, v in defaultDistribList ] )
        )
    
    # Processing
    def processBench( self, inputDistribution ):
        cc.DuDynamic_process(
            self._cdynamic,
            inputDistribution._cbench
        )
        distrib= self.distribution()
        return distrib
    
    def processFrom( self, inputList ):
        return self.processBench( Bench( [(inputList, 1.0)] ) )

    # Dump & Load
    def dump( self ):
        size= self.overallDimention()
        dumpNodes= []
        for i in range(1, size+1) :
            condDump= self.node(i).dump()
            dumpNodes.append({
                'nodeId': i,
                'parents': Code( ccode= cc.DuDynamic_node_parents( self._cdynamic, c_digit(i) ) ).asList(),
                'distributions': condDump['distributions'],
                'selector': condDump['selector']
            })
        return { 
            'inputs': self.inputs(),
            'outputs': self.outputs(),
            'shifts': self.shifts(),
            'nodes': dumpNodes
        }

    def load( self, dump ):
        self.initialize( dump['inputs'], dump['outputs'], dump['shifts'] )
        for nodeDump in dump['nodes'] :
            if len(nodeDump['parents']) > 0 :
                condition= self.node_setDependancy( 
                    nodeDump['nodeId'],
                    nodeDump['parents'],
                    nodeDump['distributions'][0]
                )
                # Generate all the distributions:
                for  distrib in nodeDump['distributions'][1:]:
                    condition.addDistribution( distrib )
                        
                # Generate the tree selector:
                Tree( ctree= cc.DuCondition_selector( condition._ccondition ) ).load( nodeDump['selector'] )
        return self
