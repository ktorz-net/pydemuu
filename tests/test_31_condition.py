import sys
sys.path.insert( 1, __file__.split('tests')[0] )
import pprint

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  C O N D I T I O N            #
# ------------------------------------------------------------------------ #

import src.demuu.clib as du

def test_DuCondition_init():
    cond= du.Condition()
    assert type(cond) == du.Condition
    assert cond.range() == 1
    assert cond.parentSpace().asList() == [1]
    assert cond.distributionSize() == 1
    assert cond.distributionAt(1) == [(1, 1.0)]
    assert cond.fromList([1]) == [(1, 1.0)]

def test_DuCondition_init2():
    cond= du.Condition( 4, [2, 3], [(1, 0.6), (2, 0.4)] )
    assert cond.range() == 4
    assert cond.parentSpace().asList() == [2, 3]
    assert cond.fromList([1, 3]) == [(1, 0.6), (2, 0.4)] 

def test_DuCondition_construction():
    cond= du.Condition( 4, [2, 3], [(1, 0.6), (2, 0.4)] )
    assert cond.fromList([1, 3]) == [(1, 0.6), (2, 0.4)]
    # From: parent-1 on 1 and whatever parent-2 Set: 3 certain. 
    cond.fromList_set( [1, 0], [(3, 1.0)] )
    # From: parent exactly on 1, 3 Set: 4 certain.
    cond.fromList_set( [1, 3], [(4, 1.0)] )
    assert cond.distributionSize() == 3
    # Test it:
    assert cond.fromList([1, 3]) == [(4, 1.0)]
    for parent in du.Code([2, 3]):
        if parent[0] != 1 :
            assert cond.fromList(parent) == [(1, 0.6), (2, 0.4)]
        elif parent != [1, 3] :
            assert cond.fromList(parent) == [(3, 1.0)]

def test_DuCondition_construction2():
    cond= du.Condition( 4, [2, 3], [(1, 0.6), (2, 0.4)] )
    cond.fromList_set( [1, 0], [(3, 1.0)] )
    assert cond.distributionSize() == 2
    cond.initialize( 4, [2, 3], [(1, 1.0)] )
    assert cond.distributionSize() == 1
    for parent in du.Code([2, 3]):
        assert cond.fromList(parent) == [(1, 1.0)]

def test_DuCindition_dump():
    cond= du.Condition( 4, [2, 3], [(1, 0.6), (2, 0.4)] )
    cond.fromList_set( [1, 0], [(3, 1.0)] )
    cond.fromList_set( [1, 3], [(4, 1.0)] )
    dump= cond.dump()
    pprint.pprint(dump)
    assert dump == {
        'range': 4,
        'selector': {
            'input': [2, 3],
            'branches': [
                {'child': 0, 'iInput': 1, 'states': [('child', 1), ('leaf', 1)] },
                {'child': 1, 'iInput': 2, 'states': [('leaf', 2), ('leaf', 2), ('leaf', 3)]}
            ]   
        },
        'distributions': [
            [(1, 0.6), (2, 0.4)],
            [(3, 1.0)],
            [(4, 1.0)]
        ]
    }

def test_DuCindition_load():
    dump= {
        'range': 4,
        'selector': {
            'input': [2, 3],
            'branches': [
                {'child': 0, 'iInput': 1, 'states': [('child', 1), ('leaf', 1)] },
                {'child': 1, 'iInput': 2, 'states': [('leaf', 2), ('leaf', 2), ('leaf', 3)]}
            ]   
        },
        'distributions': [
            [(1, 0.6), (2, 0.4)],
            [(3, 1.0)],
            [(4, 1.0)]
        ]
    }

    distribs= [
            benchDump
            for benchDump in dump['distributions']
        ]
    
    pprint.pprint( distribs )

    cond= du.Condition().load( dump )
    
    pprint.pprint( cond.dump() )
    
    assert cond.dump() == dump
