import sys
sys.path.insert( 1, __file__.split('tests')[0] )
from pprint import pprint

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  E V A L U A T O R            #
# ------------------------------------------------------------------------ #

import src.demuu.clib as du

def test_DuEvaluator_init():
    instance= du.Evaluator()
    assert type(instance) == du.Evaluator
    assert instance.inputs() == [1]
    assert instance.numberOfCriteria() == 1
    assert instance.weights() == [1.0]
    assert instance.criterion(1).inputs() == [2]
    assert instance.criterion(1).outputs() == [0.0]
    assert instance.criterionWeight(1) == 1.0
    assert instance.criterionParents(1) == []

def test_DuEvaluator_init2():
    instance= du.Evaluator(  [2, 4, 3], 2  )
    assert type(instance) == du.Evaluator
    assert instance.inputs() == [2, 4, 3]
    assert instance.numberOfCriteria() == 2
    assert instance.weights() == [1.0, 1.0]
    for i in range(1, instance.numberOfCriteria()+1) :
        assert instance.criterion(i).inputs() == [2]
        assert instance.criterion(i).outputs() == [0.0]
        assert instance.criterionWeight(i) == 1.0
        assert instance.criterionParents(i) == []

def test_DuEvaluator_construction():
    instance= du.Evaluator( [2, 4, 3], 2 )

    criterion= instance.criterion_intialize( 1, [1, 3], [0.01, 0.02, 0.03, 0.04] )
    
    assert type(instance) == du.Evaluator
    assert instance.inputs() == [2, 4, 3]
    assert instance.numberOfCriteria() == 2
    assert instance.weights() == [1.0, 1.0]

    criterion.from_set( [1, 0], 1 )
    instance.criterion(1).from_set( [2, 0], 2 )
    instance.criterion(1).from_set( [1, 3], 3 )

    criterion= instance.criterion_intialize( 2, [2], [3.0, -1.0, 0.0] )
    criterion.from_set( [1], 2 )

    assert instance.criterion(1).inputs() == [2, 3]
    assert instance.criterion(1).outputs() == [0.01, 0.02, 0.03, 0.04]
    assert instance.criterionWeight(1) == 1.0
    assert instance.criterionParents(1) == [1, 3]

    assert instance.criterion(2).inputs() == [4]
    assert instance.criterion(2).outputs() == [3.0, -1.0, 0.0]
    assert instance.criterionWeight(2) == 1.0
    assert instance.criterionParents(2) == [2]

    assert instance.criterion(1).asList() == [([1, 1, 1], 0.01), ([1, 2, 1], 0.01), ([1, 3, 3], 0.03), ([2, 0, 2], 0.02)]
    assert instance.criterion(2).asList() == [([1, 2], -1.0), ([2, 1], 3.0), ([3, 1], 3.0), ([4, 1], 3.0)]

def test_DuEvaluator_process():
    instance= du.Evaluator( [2, 4, 4], 2 )

    criterion= instance.criterion_intialize( 1, [1, 3], [0.01, 0.02, 0.03, 0.04] )
    criterion.from_set( [1, 0], 1 )
    criterion.from_set( [2, 0], 2 )
    criterion.from_set( [1, 3], 3 )
    
    instance.criterion_intialize( 2, [2], [3.0, -1.0, 0.0] )
    instance.criterion(2).from_set( [1], 2 )
    instance.criterion_setWeight( 2, 2.0 )

    assert instance.processMulti( [1, 2, 4] ) == [0.01, 3.0]
    assert instance.process( [1, 2, 4] ) == 6.01

def test_DuEvaluator_dump():
    instance= du.Evaluator( [2, 4, 4], 2 )

    criterion= instance.criterion_intialize( 1, [1, 3], [0.01, 0.02, 0.03, 0.04] )
    criterion.from_set( [1, 0], 1 )
    criterion.from_set( [2, 0], 2 )
    criterion.from_set( [1, 3], 3 )
    
    instance.criterion_intialize( 2, [2], [3.0, -1.0, 0.0] )
    instance.criterion(2).from_set( [1], 2 )
    instance.criterion_setWeight( 2, 2.0 )

    dump= instance.dump()

    #print("---")
    #pprint( dump )
    #print("---")
    
    refDump= {
        'inputs': [2, 4, 4],
        'numberOfCriteria': 2,
        'criteria': [
            {
                'criterionId': 1,
                'parents': [1, 3],
                'selector': {
                   'branches': [
                        {'child': 0, 'iInput': 1, 'states': [('child', 1), ('leaf', 2)]},
                        {'child': 1, 'iInput': 2, 'states': [('leaf', 1), ('leaf', 1), ('leaf', 3), ('leaf', 1)]}
                    ],
                    'input': [2, 4]
                },
                'values': [0.01, 0.02, 0.03, 0.04],
                'weight': 1.0
            },
            {
                'criterionId': 2,
                'parents': [2],
                'selector': {
                    'branches': [{'child': 0, 'iInput': 1, 'states': [('leaf', 2), ('leaf', 1), ('leaf', 1), ('leaf', 1)]}],
                    'input': [4]
                },
               'values': [3.0, -1.0, 0.0],
               'weight': 2.0
            }
        ]
    }

    assert instance.dump() == refDump

    instanceBis= du.Evaluator().load(refDump)
    assert instanceBis.dump() == refDump
    
    assert instanceBis.processMulti( [1, 2, 4] ) == [0.01, 3.0]
    assert instanceBis.process( [1, 2, 4] ) == 6.01
