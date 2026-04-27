import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#               T E S T   p y B b M m  C l i b C o r e                     #
# ------------------------------------------------------------------------ #
from src.demuu.clib import clibdemuu as cc

# ------------------------------------------------------------------------ #
#   STRUCTURE MODULE:
# ------------------------------------------------------------------------ #

def test_ccCode_init():
    cCode= cc.newDuCode_all(2, 3)
    assert cc.DuCode_dimention( cCode ) == 2
    for i in range(1, 3) :
        assert cc.DuCode_digit( cCode, i ) == 3
    cc.deleteDuCode( cCode )

def test_ccVector_init():
    cVector= cc.newDuVector_all(2, 3.0)
    assert cc.DuVector_dimention( cVector ) == 2
    for i in range(1, 3) :
        assert cc.DuVector_value( cVector, i ) == 3.0
    cc.deleteDuVector( cVector )

def test_ccBench_init():
    cBench= cc.newDuBench(2)
    assert cc.DuBench_size(cBench) == 0
    cc.deleteDuBench( cBench )

def test_ccTree_init():
    cTree= cc.newDuTree(2)
    assert cc.DuTree_size(cTree) == 0
    cc.deleteDuTree(cTree)


# ------------------------------------------------------------------------ #
#   FUNCTION MODULE:
# ------------------------------------------------------------------------ #

def test_ccValueFct_init():
    cValueFct= cc.newDuValueFctBasic(4, 8)
    assert cc.DuValueFct_inputDimention(cValueFct) == 4
    assert cc.DuValueFct_outputSize(cValueFct) == 8
    cc.deleteDuValueFct(cValueFct)

def test_ccFunction_init():
    cFunction= cc.newDuFunctionBasic(4)
    assert cc.DuFunction_inputDimention(cFunction) == 4
    assert cc.DuFunction_outputSize(cFunction) == 0
    cc.deleteDuFunction(cFunction)

# ------------------------------------------------------------------------ #
#   FUNCTION MODULE:
# ------------------------------------------------------------------------ #

def test_ccCondition_init():
    cCondition= cc.newDuConditionBasic(4)
    assert cc.DuCondition_range(cCondition) == 4
    cc.deleteDuCondition(cCondition)

def test_ccDynamic_init():
    cCode= cc.newDuCode_all(3, 3)
    cInf= cc.newDuDynamic( cCode, 2, 1)
    assert cc.DuDynamic_inputDimention(cInf) == 2
    assert cc.DuDynamic_outputDimention(cInf) == 1
    cc.deleteDuDynamic(cInf)
    cc.deleteDuCode( cCode )

def test_ccEvaluator_init():
    cEval= cc.newDuEvaluatorBasic(3, 2)
    assert cc.DuEvaluator_numberOfCriteria(cEval) == 2
    cc.deleteDuEvaluator(cEval)

# ------------------------------------------------------------------------ #
#   SOLVER MODULE:
# ------------------------------------------------------------------------ #

# Activate sprcific test :
if __name__ == '__main__':
    test_ccDynamic_init()