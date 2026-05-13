import sys
from pprint import pprint
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  M O D E L                     #
# ------------------------------------------------------------------------ #

from src.demuu import Model, Node
import json

def test_DuModel_init():
    model= Model()
    assert type(model) == Model
    assert( model.variables() == [] )
    assert( model.domains() == [] )

def test_DuModel_init2():
    model= Model(
        { "H": range(0, 3), "D": range(1, 7) },
        { "A": ["keep", "roll"] }
    )

    assert( model.digits( [1, 1, "roll"] ) == [2, 1, 2] )
    assert( model.digits( [0, 6, "keep"] ) == [1, 6, 1] )
    assert( model.digits( [None, 6, "keep"] ) == [0, 6, 1] )
    assert( model.digits( [None, 6, "-"] ) == [0, 6, 0] )

    assert( model.variables() == [ "H-0", "D-0", "A" , "H-1", "D-1" ] )
    assert( model.stateVariables() == [ "H", "D" ] )

    assert( model.actionVariables() == ["A"] )
    assert( model.shiftVariables() == [] )

    for dModel, dRef in zip( model.domains(), [range(0, 3), range(1, 7), ["keep", "roll"], range(0, 3), range(1, 7)] ) :
        assert( dModel == dRef )

    aNode= model.node('H-0')
    assert( type(aNode) == Node )
    assert( aNode.id() == 1 )
    assert( aNode.name() == 'H-0' )
    assert( aNode.domain() == range(0, 3) )
    assert( aNode.parents() == [] )
    assert( aNode.distribution() == [(0, 1.0)] )
    assert( model.node('A').distribution() == [("keep", 1.0)] )

    nodeA= model.node("A")
    assert( nodeA.domain() == ["keep", "roll"] )
    assert( nodeA.index("keep") == 1 )
    assert( nodeA.value(2) == "roll" )

def test_DuModel_construction_transition():
    model= Model(
        { "H": range(0, 3), "D": range(1, 7) },
        { "A": ["keep", "roll"] },
        numberOfCriteria= 2
    )

    nodeD= model.node("D-1")
    nodeD.initialize( ["A", "D-0"], [(1, 1/6), (2, 1/6), (3, 1/6), (4, 1/6), (5, 1/6), (6, 1/6)] )
    
    assert( nodeD.parents() == [ "A", "D-0" ] )
    assert( nodeD.distribution( ["roll", 1] ) == [(1, 1/6), (2, 1/6), (3, 1/6), (4, 1/6), (5, 1/6), (6, 1/6)] )
    assert( nodeD.distribution( ["keep", 5] ) == [(1, 1/6), (2, 1/6), (3, 1/6), (4, 1/6), (5, 1/6), (6, 1/6)] )

    nodeD.setConditionalDistribution( ["keep", 1], [(1, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 2], [(2, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 3], [(3, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 4], [(4, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 5], [(5, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 6], [(6, 1.0)] )
    
    assert( nodeD.distribution( ["roll", 1] ) == [(1, 1/6), (2, 1/6), (3, 1/6), (4, 1/6), (5, 1/6), (6, 1/6)] )
    assert( nodeD.distribution( ["keep", 5] ) == [(5, 1.0)]  )

    assert( [ model._varIds[p] for p in ["H-0"] ] == [1] )
    
    nodeH= model.node( "H-1" )
    nodeH.create( ["H-0"], lambda config: [(max( config[0]-1, 0 ), 1.0)] )
    
    assert( nodeH.distribution( [0] ) == [(0, 1.0)]  )
    assert( nodeH.distribution( [2] ) == [(1, 1.0)]  )

    assert( model.digits( [1, 5, "roll"] ) == [2, 5, 2] )
    
    buffer= model.dump()
    
    assert list( buffer.keys() ) == [ 'state', 'action', 'shift', 'numberOfCriteria', 'criteria' ]

    assert list( buffer['state'].keys() ) == [ 'H', 'D' ]
    assert list( buffer['action'].keys() ) == [ 'A' ]
    assert list( buffer['shift'].keys() ) == []

    assert buffer['state']['H'] == {
        'domain': [0, 1, 2],
        'parents': ['H-0'],
        'condition': {
            'range': 3,
            'distributions': [[(1, 1.0)], [(1, 1.0)], [(1, 1.0)], [(2, 1.0)]],
            'selector': {
                'input': [3],
                'branches': [
                    {'child': 0, 'iInput': 1, 'states': [('leaf', 2), ('leaf', 3), ('leaf', 4)]}
            ]
          }
        }
    }
    
    assert buffer['action']['A'] == {
        "domain": ["keep", "roll"],
        "parents": [],
        "condition": {
            "range": 2,
            "distributions": [ [ (1, 1.0) ] ],
            "selector": { "input": [1], "branches": [] }
        }
    }

    assert buffer['state']['D'] == {
      'domain': [1, 2, 3, 4, 5, 6],
      'parents': ["A", "D-0"],
      'condition': {
        'range': 6,
        'distributions': [
            [(1, 1/6), (2, 1/6), (3, 1/6), (4, 1/6), (5, 1/6), (6, 1/6)],
            [(1, 1.0)],
            [(2, 1.0)],
            [(3, 1.0)],
            [(4, 1.0)],
            [(5, 1.0)],
            [(6, 1.0)]
        ],
        'selector': {
            'input': [2, 6],
            'branches': [
                { 'child': 0, 'iInput': 1, 'states': [('child', 1), ('leaf', 1)] },
                {'child': 1, 'iInput': 2, 'states': [('leaf', 2), ('leaf', 3), ('leaf', 4), ('leaf', 5), ('leaf', 6), ('leaf', 7)]}
          ]
        }
      }
    }

    
def test_DuModel_construction_reward():
    model= Model(
        { "H": range(0, 3), "D": range(1, 7) },
        { "A": ["keep", "roll"] },
        numberOfCriteria= 2
    )

    crit= model.criterion(1).initialize( ['H-0', 'D-1'], [0.0, 1.1, 1.2, 3.1] )
    
    assert crit.outputs() == [0.0, 1.1, 1.2, 3.1]
    assert crit.from_set( [1, 1], 3.1 ) == 4

    crit.from_set( [1, 3], 1.1 )
    crit.from_set( [1, 4], 3.1 )
    crit.from_set( [1, 5], 1.1 )
    crit.from_set( [1, 6], 1.2 )
    
    crit= model.criterion(2).initialize( ['A'], [0.0, -1.0] )
    crit.from_set( ["roll"], -1.0 )
    crit. setWeight( 0.1 )

    buffer= model.dump()

    assert buffer['numberOfCriteria'] == 2
    assert buffer['numberOfCriteria'] == 2
    assert len( buffer['criteria'] ) == 2

    assert buffer['criteria'][0] == {
        'criterionId': 1,
        'weight': 1.0,
        'parents': [1, 5],
        'values': [0.0, 1.1, 1.2, 3.1],
        'selector': {
            'branches': [
                {'child': 0, 'iInput': 1, 'states': [('leaf', 1), ('child', 1), ('leaf', 1)]},
                {'child': 1, 'iInput': 2, 'states': [('leaf', 4), ('leaf', 1), ('leaf', 2), ('leaf', 4), ('leaf', 2), ('leaf', 3)]}
            ],
            'input': [3, 6]
        }
    }
    
    assert buffer['criteria'][1] == {
        'criterionId': 2,
        'weight': 0.1,
        'parents': [3],
        'values': [0.0, -1.0],
        'selector': {
            'input': [2],
            'branches': [{'child': 0, 'iInput': 1, 'states': [('leaf', 1), ('leaf', 2)]}]
        }
    }
    
    crit= model.criterion(1)
    assert crit.from_set( [1, 2], -10.0 ) == 5
    assert crit.outputs() == [0.0, 1.1, 1.2, 3.1, -10.0]
 
    pprint( model.dump() )

    assert model.reward( [2, 4], ["keep"], [1, 4] ) == 0.0
    assert model.reward( [2, 4], ["roll"], [1, 4] ) == -0.1
    assert model.reward( [1, 4], ["roll"], [0, 2] ) == -10.1
    assert model.reward( [1, 4], ["roll"], [0, 1] ) == 3.0

def test_DuModel_transition():
    model= Model(
        { "H": range(0, 3), "D": range(1, 7) },
        { "A": ["keep", "roll"] }
    )

    nodeD= model.node("D-1").initialize( ["A", "D-0"], [(1, 1/9), (2, 2/9), (3, 1/3), (4, 1/9), (5, 1/9), (6, 1/9)] )

    nodeD.setConditionalDistribution( ["keep", 1], [(1, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 2], [(2, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 3], [(3, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 4], [(4, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 5], [(5, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 6], [(6, 1.0)] )

    model.node( "H-1" ).create( ["H-0"], lambda config: [(max( config[0]-1, 0 ), 1.0)] )

    assert( model.digitTransition( [2, 5], [2] ) == [
        ([1, 1], 1/9),
        ([1, 2], 2/9),
        ([1, 3], 1/3),
        ([1, 4], 1/9),
        ([1, 5], 1/9),
        ([1, 6], 1/9)
    ])

    print( "---" )
    print( model.transition( [1, 5], ["roll"] ) )
    print( "---" )

    assert( model.digits( [1, 5, "roll"] ) == [2, 5, 2] )
    assert( model.transition( [1, 5], ["roll"] ) == [
        ([0, 1], 1/9),
        ([0, 2], 2/9),
        ([0, 3], 1/3),
        ([0, 4], 1/9),
        ([0, 5], 1/9),
        ([0, 6], 1/9)
    ])
    
    simu= model.step( [1, 5], ["roll"] )
    assert simu[0] == 0
    assert 1 <= simu[1] and simu[1] <= 6

    counters= [0 for i in range(7)]
    for i in range(10000) :
        simu= model.step( [1, 5], ["roll"] )
        assert simu[0] == 0
        assert 1 <= simu[1] and simu[1] <= 6
        counters[simu[1]] += 1

    counters=[ round(x/100, 1) for x in counters ]
    refs= [0.0, 11.11, 22.22, 33.33, 11.11,11.11, 11.11]
    print( counters )
    print( refs )
    
    for v, r in zip(counters, refs) :
        assert r-1 <= v and v <= r+1

def test_DuModel_simple421():
    import models.simple421 as m
    model= m.generate()
    
    #assert False

    #assert model.dump == {".json"}
