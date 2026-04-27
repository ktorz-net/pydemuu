import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                 T E S T   p y B b M m  : :  V E C T O R                  #
# ------------------------------------------------------------------------ #

import src.demuu.clib as du

def test_DuVector_init():
    vector= du.Vector()
    assert vector.dimention() == 0

def test_DuVector_init2():
    vector= du.Vector([1, 2, 3])
    assert vector.dimention() == 3
    assert vector.value(1) == 1
    assert vector.value(2) == 2
    assert vector.value(3) == 3
    assert vector.asList() == [1, 2, 3]

def test_DuVector_copy():
    vector= du.Vector([1, 2, 3])
    cpy= vector.copy()
    assert cpy.dimention() == 3
    assert cpy.value(1) == 1
    assert cpy.value(2) == 2
    assert cpy.value(3) == 3
    assert cpy.asList() == [1, 2, 3]
    vector.initialize([3, 2])
    assert vector.asList() == [3, 2]
    assert cpy.asList() == [1, 2, 3]

def test_DuVector_compare():
    v1= du.Vector([1.0, 42.0, 3.0])
    v2= du.Vector([1.0, 42.0, 3.0])
    assert v1 == v2
    assert v1 <= v2
    assert v1 >= v2
    v2.initialize( [1.0, 43.0, 3.0] )
    assert v1 < v2
    assert v1 <= v2
    assert v2 > v1
    assert v2 >= v1
    assert v1 != v2

def test_DuVector_modify():
    vector= du.Vector([1.0, 2.0, 3.0])
    assert vector.asList() == [1.0, 2.0, 3.0]
    vector.resize(2)
    assert vector.asList() == [1.0, 2.0]
    vector.resize(4)
    assert vector.asList() == [1.0, 2.0, 0.0, 0.0]
    vector.at_set(1, 2.0)
    vector.at_set(4, 6.0)
    vector.at_set(2, 3.0)
    vector.at_set(3, 1.0)
    assert vector.asList() == [2.0, 3.0, 1.0, 6.0]

def test_DuVector_dump():
    vect= du.Vector([1.0, 2.1, 3.0])
    assert vect.dump() == [1.0, 2.1, 3.0]

def test_DuVect_load():
    vect= du.Vector().load( du.Vector([1.0, 2.1, 3.0]).dump() )
    assert vect.dump() == [1.0, 2.1, 3.0]

if __name__ == '__main__':
    test_DuVector_modify()
