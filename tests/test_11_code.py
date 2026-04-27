import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                 T E S T   p y B b M m  : :  C O D E                      #
# ------------------------------------------------------------------------ #

import src.demuu.clib as du

def test_DuCode_init():
    code= du.Code()
    assert str(code) == "code[]"
    assert code.dimention() == 0

def test_DuCode_init2():
    code= du.Code([1, 2, 3])
    assert code.dimention() == 3
    assert code.digit(1) == 1
    assert code.digit(2) == 2
    assert code.digit(3) == 3
    assert str(code) == "code[1, 2, 3]"
    assert code.asList() == [1, 2, 3]

def test_DuCode_copy():
    code= du.Code([1, 2, 3])
    cpy= code.copy()
    assert cpy.dimention() == 3
    assert cpy.digit(1) == 1
    assert cpy.digit(2) == 2
    assert cpy.digit(3) == 3
    assert cpy.asList() == [1, 2, 3]
    code.initialize([3, 2])
    assert code.asList() == [3, 2]
    assert cpy.asList() == [1, 2, 3]

def test_DuCode_compare():
    code1= du.Code([1, 42, 3])
    code2= du.Code([1, 42, 3])
    assert code1 == code2
    assert code1 <= code2
    assert code1 >= code2
    code2.initialize( [1, 43, 3] )
    assert code1 < code2
    assert code1 <= code2
    assert code2 > code1
    assert code2 >= code1
    assert code1 != code2

def test_DuCode_modify():
    code= du.Code([1, 2, 3])
    assert code.asList() == [1, 2, 3]
    code.resize(2)
    assert code.asList() == [1, 2]
    code.resize(4)
    assert code.asList() == [1, 2, 0, 0]
    code.at_set(1, 2)
    code.at_set(4, 6)
    code.at_set(2, 3)
    code.at_set(3, 1)
    assert code.asList() == [2, 3, 1, 6]

def test_DuCode_iterate():
    code= du.Code([2, 3, 2])
    iCode= iter(code)
    assert next(iCode) == [1, 1, 1]
    assert next(iCode) == [2, 1, 1]
    assert next(iCode) == [1, 2, 1]
    assert next(iCode) == [2, 2, 1]
    assert next(iCode) == [1, 3, 1]
    assert next(iCode) == [2, 3, 1]
    assert next(iCode) == [1, 1, 2]
    assert next(iCode) == [2, 1, 2]
    assert next(iCode) == [1, 2, 2]
    assert next(iCode) == [2, 2, 2]
    assert next(iCode) == [1, 3, 2]
    assert next(iCode) == [2, 3, 2]
    count= 0
    for lst in iter(code) :
        count+= 1
    assert count == 2*3*2
    count= 0
    for lst in code :
        count+= 1
    assert count == 2*3*2

def test_DuCode_print():
    assert str( du.Code([1, 2, 3]) ) == "code[1, 2, 3]"


def test_DuCode_dump():
    code= du.Code([1, 2, 3])
    assert code.dump() == [1, 2, 3]

def test_DuCode_load():
    code= du.Code().load( du.Code([1, 2, 3]).dump() )
    assert code.dump() == [1, 2, 3]

def test_DuCode_print():
    assert str( du.Code([1, 2, 3]) ) == "code[1, 2, 3]"

if __name__ == '__main__':
    test_DuCode_iterate()
