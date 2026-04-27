import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  C R I T E R I O N             #
# ------------------------------------------------------------------------ #

import src.demuu.clib as du
from src.demuu.clib import clibdemuu as cc

def test_DuValueFct_init():
    instance= du.ValueFct()
    assert type(instance) == du.ValueFct
    assert instance.inputs() == [1]
    assert instance.outputs() == [0.0]

def test_DuValueFct_init2():
    instance= du.ValueFct( [2, 4], [0.0, 1.0, 0.5] )
    assert type(instance) == du.ValueFct
    assert instance.inputs() == [2, 4]
    assert instance.outputs() == [0.0, 1.0, 0.5]

def test_DuValueFct_construction():
    instance= du.ValueFct()
    instance.initialize( [2, 3], [0.01, 0.02, 0.03, 0.04] )

    assert instance.inputs() == [2, 3]
    assert instance.outputs() == [0.01, 0.02, 0.03, 0.04]

    assert instance.asList() == [([1, 0, 1], 0.01), ([2, 0, 1], 0.01)]

    assert instance.inputs() == [2, 3]
    assert instance.outputs() == [0.01, 0.02, 0.03, 0.04]

    instance.from_set( [1, 0], 1 )
    instance.from_set( [2, 0], 2 )
    instance.from_set( [1, 3], 3 )
    
    assert instance.asList() == [([1, 1, 1], 0.01), ([1, 2, 1], 0.01), ([1, 3, 3], 0.03), ([2, 0, 2], 0.02)]

if __name__ == "__main__" :
    test_DuValueFct_construction()