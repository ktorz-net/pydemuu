import os, ctypes, platform

# ------------------------------------------------------------------------ #
#            P Y T H O N   W R A P E R   O F   l i b D e m u u
#
# - generated with bin/generate-c-binding
# - Binding of src/demuu/clib/demuu.h
# 
#                /!\ THIS FILE SHOULD NOT BE MODIFIED /!\
# ------------------------------------------------------------------------ #

# Usefull ctype types:

from ctypes import c_ushort, c_ulong, c_double, c_void_p

# Usefull Demuu basis types:

c_digit, c_hash= c_ushort, c_ulong

# CArray tools :

def makeCArray( c_type, size, value ):
    Array= c_type * size
    cArray= Array()
    for i in range(size) :
        cArray[i]= (c_type)( value )
    return cArray

def makeCArrayAs( c_type, size, pythonLst ):
    Array= c_type * size
    cArray= Array()
    for i in range(size) :
        cArray[i]= (c_type)( pythonLst[i] )
    return cArray

def readCArray( py_type, c_type, size, arrayPointer ):
    pLst= ctypes.cast(arrayPointer, ctypes.POINTER(c_type))
    return [ (py_type)(pLst[i]) for i in range(size) ]

# Load C Demuu librairy : 

demuuDir= os.path.dirname(os.path.realpath(__file__))
demuuCLib= demuuDir+f"/{platform.system()}-{platform.machine()}/libDemuu.so"
print( f"BbMm>>>> LOAD: {demuuCLib} <<<" )
core = ctypes.cdll.LoadLibrary( demuuCLib )

# src/demuu/clib/demuu.h wrap :


# DuCode* newDuCode( digit dimension );
newDuCode= core.newDuCode
newDuCode.restype= c_void_p
newDuCode.argtypes= [c_digit]

# DuCode* newDuCode_numbers( digit dimension, digit* numbers );
newDuCode_numbers= core.newDuCode_numbers
newDuCode_numbers.restype= c_void_p
newDuCode_numbers.argtypes= [c_digit, c_void_p]

# DuCode* newDuCode_all( digit dimension, digit defaultValue );
newDuCode_all= core.newDuCode_all
newDuCode_all.restype= c_void_p
newDuCode_all.argtypes= [c_digit, c_digit]

# DuCode* newDuCodeAs( DuCode* model );
newDuCodeAs= core.newDuCodeAs
newDuCodeAs.restype= c_void_p
newDuCodeAs.argtypes= [c_void_p]

# DuCode* DuCode_create( DuCode* self, digit dimension );
DuCode_create= core.DuCode_create
DuCode_create.restype= c_void_p
DuCode_create.argtypes= [c_void_p, c_digit]

# DuCode* DuCode_create_numbers( DuCode* self, digit dimension, digit* numbers );
DuCode_create_numbers= core.DuCode_create_numbers
DuCode_create_numbers.restype= c_void_p
DuCode_create_numbers.argtypes= [c_void_p, c_digit, c_void_p]

# DuCode* DuCode_create_all( DuCode* self, digit dimension, digit defaultValue );
DuCode_create_all= core.DuCode_create_all
DuCode_create_all.restype= c_void_p
DuCode_create_all.argtypes= [c_void_p, c_digit, c_digit]

# DuCode* DuCode_createAs( DuCode* self, DuCode* model );
DuCode_createAs= core.DuCode_createAs
DuCode_createAs.restype= c_void_p
DuCode_createAs.argtypes= [c_void_p, c_void_p]

# DuCode* DuCode_createMerge( DuCode* self, digit numberOfCodes, DuCode ** codes );
DuCode_createMerge= core.DuCode_createMerge
DuCode_createMerge.restype= c_void_p
DuCode_createMerge.argtypes= [c_void_p, c_digit, c_void_p]

# void deleteDuCode( DuCode* instance );
deleteDuCode= core.deleteDuCode
deleteDuCode.restype= c_void_p
deleteDuCode.argtypes= [c_void_p]

# DuCode* DuCode_destroy( DuCode* self );
DuCode_destroy= core.DuCode_destroy
DuCode_destroy.restype= c_void_p
DuCode_destroy.argtypes= [c_void_p]

# digit DuCode_dimention( DuCode* self );
DuCode_dimention= core.DuCode_dimention
DuCode_dimention.restype= c_digit
DuCode_dimention.argtypes= [c_void_p]

# digit DuCode_digit( DuCode* self, digit index );
DuCode_digit= core.DuCode_digit
DuCode_digit.restype= c_digit
DuCode_digit.argtypes= [c_void_p, c_digit]

# digit DuCode_count( DuCode* self, digit value );
DuCode_count= core.DuCode_count
DuCode_count.restype= c_digit
DuCode_count.argtypes= [c_void_p, c_digit]

# hash DuCode_sum( DuCode* self );
DuCode_sum= core.DuCode_sum
DuCode_sum.restype= c_hash
DuCode_sum.argtypes= [c_void_p]

# hash DuCode_product( DuCode* self );
DuCode_product= core.DuCode_product
DuCode_product.restype= c_hash
DuCode_product.argtypes= [c_void_p]

# DuCode* DuCode_reinit( DuCode* self, digit newDimension );
DuCode_reinit= core.DuCode_reinit
DuCode_reinit.restype= c_void_p
DuCode_reinit.argtypes= [c_void_p, c_digit]

# DuCode* DuCode_copy( DuCode* self, DuCode* model );
DuCode_copy= core.DuCode_copy
DuCode_copy.restype= c_void_p
DuCode_copy.argtypes= [c_void_p, c_void_p]

# DuCode* DuCode_copyNumbers( DuCode* self, DuCode* model );
DuCode_copyNumbers= core.DuCode_copyNumbers
DuCode_copyNumbers.restype= c_void_p
DuCode_copyNumbers.argtypes= [c_void_p, c_void_p]

# DuCode* DuCode_redimention( DuCode* self, digit newDimension );
DuCode_redimention= core.DuCode_redimention
DuCode_redimention.restype= c_void_p
DuCode_redimention.argtypes= [c_void_p, c_digit]

# DuCode* DuCode_setAll( DuCode* self, digit value );
DuCode_setAll= core.DuCode_setAll
DuCode_setAll.restype= c_void_p
DuCode_setAll.argtypes= [c_void_p, c_digit]

# DuCode* DuCode_at_set( DuCode* self, digit index, digit value );
DuCode_at_set= core.DuCode_at_set
DuCode_at_set.restype= c_void_p
DuCode_at_set.argtypes= [c_void_p, c_digit, c_digit]

# DuCode* DuCode_at_increment( DuCode* self, digit index, digit value );
DuCode_at_increment= core.DuCode_at_increment
DuCode_at_increment.restype= c_void_p
DuCode_at_increment.argtypes= [c_void_p, c_digit, c_digit]

# DuCode* DuCode_at_decrement( DuCode* self, digit index, digit value );
DuCode_at_decrement= core.DuCode_at_decrement
DuCode_at_decrement.restype= c_void_p
DuCode_at_decrement.argtypes= [c_void_p, c_digit, c_digit]

# DuCode* DuCode_setNumbers( DuCode* self, digit* numbers );
DuCode_setNumbers= core.DuCode_setNumbers
DuCode_setNumbers.restype= c_void_p
DuCode_setNumbers.argtypes= [c_void_p, c_void_p]

# void DuCode_sort( DuCode* self );
DuCode_sort= core.DuCode_sort
DuCode_sort.restype= c_void_p
DuCode_sort.argtypes= [c_void_p]

# void DuCode_switch( DuCode* self, DuCode* anotherCode );
DuCode_switch= core.DuCode_switch
DuCode_switch.restype= c_void_p
DuCode_switch.argtypes= [c_void_p, c_void_p]

# digit DuCode_search( DuCode* self, digit value );
DuCode_search= core.DuCode_search
DuCode_search.restype= c_digit
DuCode_search.argtypes= [c_void_p, c_digit]

# bool DuCode_isEqualTo( DuCode* self, DuCode* another );
DuCode_isEqualTo= core.DuCode_isEqualTo
DuCode_isEqualTo.restype= c_digit
DuCode_isEqualTo.argtypes= [c_void_p, c_void_p]

# bool DuCode_isGreaterThan( DuCode* self, DuCode* another );
DuCode_isGreaterThan= core.DuCode_isGreaterThan
DuCode_isGreaterThan.restype= c_digit
DuCode_isGreaterThan.argtypes= [c_void_p, c_void_p]

# bool DuCode_isSmallerThan( DuCode* self, DuCode* another );
DuCode_isSmallerThan= core.DuCode_isSmallerThan
DuCode_isSmallerThan.restype= c_digit
DuCode_isSmallerThan.argtypes= [c_void_p, c_void_p]

# hash DuCode_keyOf( DuCode* self, DuCode* code );
DuCode_keyOf= core.DuCode_keyOf
DuCode_keyOf.restype= c_hash
DuCode_keyOf.argtypes= [c_void_p, c_void_p]

# DuCode* DuCode_setCode_onKey( DuCode* self, DuCode* configuration, hash key );
DuCode_setCode_onKey= core.DuCode_setCode_onKey
DuCode_setCode_onKey.restype= c_void_p
DuCode_setCode_onKey.argtypes= [c_void_p, c_void_p, c_hash]

# DuCode* DuCode_setCodeFirst( DuCode* self, DuCode* configuration );
DuCode_setCodeFirst= core.DuCode_setCodeFirst
DuCode_setCodeFirst.restype= c_void_p
DuCode_setCodeFirst.argtypes= [c_void_p, c_void_p]

# DuCode* DuCode_setCodeLast( DuCode* self, DuCode* configuration );
DuCode_setCodeLast= core.DuCode_setCodeLast
DuCode_setCodeLast.restype= c_void_p
DuCode_setCodeLast.argtypes= [c_void_p, c_void_p]

# DuCode* DuCode_newDuCodeOnKey( DuCode* self, hash key );
DuCode_newDuCodeOnKey= core.DuCode_newDuCodeOnKey
DuCode_newDuCodeOnKey.restype= c_void_p
DuCode_newDuCodeOnKey.argtypes= [c_void_p, c_hash]

# DuCode* DuCode_newDuCodeFirst( DuCode* self );
DuCode_newDuCodeFirst= core.DuCode_newDuCodeFirst
DuCode_newDuCodeFirst.restype= c_void_p
DuCode_newDuCodeFirst.argtypes= [c_void_p]

# DuCode* DuCode_newDuCodeLast( DuCode* self );
DuCode_newDuCodeLast= core.DuCode_newDuCodeLast
DuCode_newDuCodeLast.restype= c_void_p
DuCode_newDuCodeLast.argtypes= [c_void_p]

# DuCode* DuCode_nextCode( DuCode* self, DuCode* configuration );
DuCode_nextCode= core.DuCode_nextCode
DuCode_nextCode.restype= c_void_p
DuCode_nextCode.argtypes= [c_void_p, c_void_p]

# DuCode* DuCode_previousCode( DuCode* self, DuCode* configuration );
DuCode_previousCode= core.DuCode_previousCode
DuCode_previousCode.restype= c_void_p
DuCode_previousCode.argtypes= [c_void_p, c_void_p]

# bool DuCode_isIncluding( DuCode* self, DuCode* configuration );
DuCode_isIncluding= core.DuCode_isIncluding
DuCode_isIncluding.restype= c_digit
DuCode_isIncluding.argtypes= [c_void_p, c_void_p]

# DuCode* DuCode_newDuCodeMask( DuCode* self, DuCode* mask );
DuCode_newDuCodeMask= core.DuCode_newDuCodeMask
DuCode_newDuCodeMask.restype= c_void_p
DuCode_newDuCodeMask.argtypes= [c_void_p, c_void_p]

# char* DuCode_print( DuCode* self, char* buffer );
DuCode_print= core.DuCode_print
DuCode_print.restype= c_void_p
DuCode_print.argtypes= [c_void_p, c_void_p]

# DuVector* newDuVector( digit dimension );
newDuVector= core.newDuVector
newDuVector.restype= c_void_p
newDuVector.argtypes= [c_digit]

# DuVector* newDuVector_values( digit dimension, double* values );
newDuVector_values= core.newDuVector_values
newDuVector_values.restype= c_void_p
newDuVector_values.argtypes= [c_digit, c_void_p]

# DuVector* newDuVector_all( digit dimension, double value );
newDuVector_all= core.newDuVector_all
newDuVector_all.restype= c_void_p
newDuVector_all.argtypes= [c_digit, c_double]

# DuVector* newDuVectorAs( DuVector* model );
newDuVectorAs= core.newDuVectorAs
newDuVectorAs.restype= c_void_p
newDuVectorAs.argtypes= [c_void_p]

# DuVector* DuVector_create( DuVector* self, digit dimension );
DuVector_create= core.DuVector_create
DuVector_create.restype= c_void_p
DuVector_create.argtypes= [c_void_p, c_digit]

# DuVector* DuVector_create_values( DuVector* self, digit dimension, double* values );
DuVector_create_values= core.DuVector_create_values
DuVector_create_values.restype= c_void_p
DuVector_create_values.argtypes= [c_void_p, c_digit, c_void_p]

# DuVector* DuVector_create_all( DuVector* self, digit dimension, double value );
DuVector_create_all= core.DuVector_create_all
DuVector_create_all.restype= c_void_p
DuVector_create_all.argtypes= [c_void_p, c_digit, c_double]

# DuVector* DuVector_createAs( DuVector* self, DuVector* model );
DuVector_createAs= core.DuVector_createAs
DuVector_createAs.restype= c_void_p
DuVector_createAs.argtypes= [c_void_p, c_void_p]

# DuVector* DuVector_destroy( DuVector* self );
DuVector_destroy= core.DuVector_destroy
DuVector_destroy.restype= c_void_p
DuVector_destroy.argtypes= [c_void_p]

# void deleteDuVector( DuVector* self );
deleteDuVector= core.deleteDuVector
deleteDuVector.restype= c_void_p
deleteDuVector.argtypes= [c_void_p]

# DuVector* DuVector_reinit( DuVector* self, digit newDimension );
DuVector_reinit= core.DuVector_reinit
DuVector_reinit.restype= c_void_p
DuVector_reinit.argtypes= [c_void_p, c_digit]

# DuVector* DuVector_copy( DuVector* self, DuVector* model );
DuVector_copy= core.DuVector_copy
DuVector_copy.restype= c_void_p
DuVector_copy.argtypes= [c_void_p, c_void_p]

# digit DuVector_dimention( DuVector* self );
DuVector_dimention= core.DuVector_dimention
DuVector_dimention.restype= c_digit
DuVector_dimention.argtypes= [c_void_p]

# double DuVector_value( DuVector* self, digit i );
DuVector_value= core.DuVector_value
DuVector_value.restype= c_double
DuVector_value.argtypes= [c_void_p, c_digit]

# DuVector* DuVector_redimention( DuVector* self, digit newDimension );
DuVector_redimention= core.DuVector_redimention
DuVector_redimention.restype= c_void_p
DuVector_redimention.argtypes= [c_void_p, c_digit]

# double DuVector_at_set( DuVector* self, digit i, double value );
DuVector_at_set= core.DuVector_at_set
DuVector_at_set.restype= c_double
DuVector_at_set.argtypes= [c_void_p, c_digit, c_double]

# DuVector* DuVector_setValues( DuVector* self, double* values );
DuVector_setValues= core.DuVector_setValues
DuVector_setValues.restype= c_void_p
DuVector_setValues.argtypes= [c_void_p, c_void_p]

# double DuVector_sum( DuVector* self );
DuVector_sum= core.DuVector_sum
DuVector_sum.restype= c_double
DuVector_sum.argtypes= [c_void_p]

# double DuVector_product( DuVector* self );
DuVector_product= core.DuVector_product
DuVector_product.restype= c_double
DuVector_product.argtypes= [c_void_p]

# bool DuVector_isEqualTo( DuVector* self, DuVector* another );
DuVector_isEqualTo= core.DuVector_isEqualTo
DuVector_isEqualTo.restype= c_digit
DuVector_isEqualTo.argtypes= [c_void_p, c_void_p]

# bool DuVector_isGreaterThan( DuVector* self, DuVector* another );
DuVector_isGreaterThan= core.DuVector_isGreaterThan
DuVector_isGreaterThan.restype= c_digit
DuVector_isGreaterThan.argtypes= [c_void_p, c_void_p]

# bool DuVector_isSmallerThan( DuVector* self, DuVector* another );
DuVector_isSmallerThan= core.DuVector_isSmallerThan
DuVector_isSmallerThan.restype= c_digit
DuVector_isSmallerThan.argtypes= [c_void_p, c_void_p]

# char* DuVector_print( DuVector* self, char* output );
DuVector_print= core.DuVector_print
DuVector_print.restype= c_void_p
DuVector_print.argtypes= [c_void_p, c_void_p]

# char* DuVector_format_print( DuVector* self, char* format, char* buffer );
DuVector_format_print= core.DuVector_format_print
DuVector_format_print.restype= c_void_p
DuVector_format_print.argtypes= [c_void_p, c_void_p, c_void_p]

# DuBench* newDuBench( digit capacity );
newDuBench= core.newDuBench
newDuBench.restype= c_void_p
newDuBench.argtypes= [c_digit]

# DuBench* newDuBench_codeDim_vectorDim( digit capacity, digit codeDim, digit vectorDim );
newDuBench_codeDim_vectorDim= core.newDuBench_codeDim_vectorDim
newDuBench_codeDim_vectorDim.restype= c_void_p
newDuBench_codeDim_vectorDim.argtypes= [c_digit, c_digit, c_digit]

# DuBench* newDuBench_startDigit_value( digit capacity, digit aDigit, double value );
newDuBench_startDigit_value= core.newDuBench_startDigit_value
newDuBench_startDigit_value.restype= c_void_p
newDuBench_startDigit_value.argtypes= [c_digit, c_digit, c_double]

# DuBench* newDuBench_startWithCode_vector( digit capacity, DuCode* newCode, DuVector* newVector );
newDuBench_startWithCode_vector= core.newDuBench_startWithCode_vector
newDuBench_startWithCode_vector.restype= c_void_p
newDuBench_startWithCode_vector.argtypes= [c_digit, c_void_p, c_void_p]

# DuBench* newDuBenchAs( DuBench* model );
newDuBenchAs= core.newDuBenchAs
newDuBenchAs.restype= c_void_p
newDuBenchAs.argtypes= [c_void_p]

# DuBench* DuBench_create( DuBench* self, digit capacity );
DuBench_create= core.DuBench_create
DuBench_create.restype= c_void_p
DuBench_create.argtypes= [c_void_p, c_digit]

# DuBench* DuBench_create_codeDim_vectorDim( DuBench* self, digit capacity, digit codeDim, digit vectorDim );
DuBench_create_codeDim_vectorDim= core.DuBench_create_codeDim_vectorDim
DuBench_create_codeDim_vectorDim.restype= c_void_p
DuBench_create_codeDim_vectorDim.argtypes= [c_void_p, c_digit, c_digit, c_digit]

# DuBench* DuBench_createAs( DuBench* self, DuBench* model );
DuBench_createAs= core.DuBench_createAs
DuBench_createAs.restype= c_void_p
DuBench_createAs.argtypes= [c_void_p, c_void_p]

# DuBench* DuBench_destroy( DuBench* self );
DuBench_destroy= core.DuBench_destroy
DuBench_destroy.restype= c_void_p
DuBench_destroy.argtypes= [c_void_p]

# void deleteDuBench( DuBench* self );
deleteDuBench= core.deleteDuBench
deleteDuBench.restype= c_void_p
deleteDuBench.argtypes= [c_void_p]

# DuBench* DuBench_reinit( DuBench* self, digit capacity );
DuBench_reinit= core.DuBench_reinit
DuBench_reinit.restype= c_void_p
DuBench_reinit.argtypes= [c_void_p, c_digit]

# digit DuBench_size( DuBench* self );
DuBench_size= core.DuBench_size
DuBench_size.restype= c_digit
DuBench_size.argtypes= [c_void_p]

# digit DuBench_codeDimention( DuBench* self );
DuBench_codeDimention= core.DuBench_codeDimention
DuBench_codeDimention.restype= c_digit
DuBench_codeDimention.argtypes= [c_void_p]

# digit DuBench_vectorDimention( DuBench* self );
DuBench_vectorDimention= core.DuBench_vectorDimention
DuBench_vectorDimention.restype= c_digit
DuBench_vectorDimention.argtypes= [c_void_p]

# DuCode* DuBench_codeAt( DuBench* self, digit i );
DuBench_codeAt= core.DuBench_codeAt
DuBench_codeAt.restype= c_void_p
DuBench_codeAt.argtypes= [c_void_p, c_digit]

# DuVector* DuBench_vectorAt( DuBench* self, digit i );
DuBench_vectorAt= core.DuBench_vectorAt
DuBench_vectorAt.restype= c_void_p
DuBench_vectorAt.argtypes= [c_void_p, c_digit]

# digit DuBench_digitAt( DuBench* self, digit i );
DuBench_digitAt= core.DuBench_digitAt
DuBench_digitAt.restype= c_digit
DuBench_digitAt.argtypes= [c_void_p, c_digit]

# double DuBench_valueAt( DuBench* self, digit i );
DuBench_valueAt= core.DuBench_valueAt
DuBench_valueAt.restype= c_double
DuBench_valueAt.argtypes= [c_void_p, c_digit]

# digit DuBench_at_digit( DuBench* self, digit i, digit j );
DuBench_at_digit= core.DuBench_at_digit
DuBench_at_digit.restype= c_digit
DuBench_at_digit.argtypes= [c_void_p, c_digit, c_digit]

# double DuBench_at_value( DuBench* self, digit i, digit j );
DuBench_at_value= core.DuBench_at_value
DuBench_at_value.restype= c_double
DuBench_at_value.argtypes= [c_void_p, c_digit, c_digit]

# void DuBench_resizeCapacity( DuBench* self, digit newCapacity );
DuBench_resizeCapacity= core.DuBench_resizeCapacity
DuBench_resizeCapacity.restype= c_void_p
DuBench_resizeCapacity.argtypes= [c_void_p, c_digit]

# digit DuBench_attachCode_vector( DuBench* self, DuCode* newCode, DuVector* newVector );
DuBench_attachCode_vector= core.DuBench_attachCode_vector
DuBench_attachCode_vector.restype= c_digit
DuBench_attachCode_vector.argtypes= [c_void_p, c_void_p, c_void_p]

# digit DuBench_attachFrontCode_vector( DuBench* self, DuCode* newCode, DuVector* newVector );
DuBench_attachFrontCode_vector= core.DuBench_attachFrontCode_vector
DuBench_attachFrontCode_vector.restype= c_digit
DuBench_attachFrontCode_vector.argtypes= [c_void_p, c_void_p, c_void_p]

# DuCode* DuBench_detach( DuBench* self );
DuBench_detach= core.DuBench_detach
DuBench_detach.restype= c_void_p
DuBench_detach.argtypes= [c_void_p]

# DuCode* DuBench_detachFront( DuBench* self );
DuBench_detachFront= core.DuBench_detachFront
DuBench_detachFront.restype= c_void_p
DuBench_detachFront.argtypes= [c_void_p]

# DuBench* DuBench_increase( DuBench* self, digit number );
DuBench_increase= core.DuBench_increase
DuBench_increase.restype= c_void_p
DuBench_increase.argtypes= [c_void_p, c_digit]

# DuBench* DuBench_increaseFront( DuBench* self, digit number );
DuBench_increaseFront= core.DuBench_increaseFront
DuBench_increaseFront.restype= c_void_p
DuBench_increaseFront.argtypes= [c_void_p, c_digit]

# digit DuBench_attachCode( DuBench* self, DuCode* newItem );
DuBench_attachCode= core.DuBench_attachCode
DuBench_attachCode.restype= c_digit
DuBench_attachCode.argtypes= [c_void_p, c_void_p]

# digit DuBench_attachVector( DuBench* self, DuVector* newItem );
DuBench_attachVector= core.DuBench_attachVector
DuBench_attachVector.restype= c_digit
DuBench_attachVector.argtypes= [c_void_p, c_void_p]

# void DuBench_switch( DuBench* self, DuBench* doppleganger );
DuBench_switch= core.DuBench_switch
DuBench_switch.restype= c_void_p
DuBench_switch.argtypes= [c_void_p, c_void_p]

# digit DuBench_addDigit_value( DuBench* self, digit d, double v );
DuBench_addDigit_value= core.DuBench_addDigit_value
DuBench_addDigit_value.restype= c_digit
DuBench_addDigit_value.argtypes= [c_void_p, c_digit, c_double]

# DuBench* DuBench_at_setDigit( DuBench* self, digit i, digit aDigit );
DuBench_at_setDigit= core.DuBench_at_setDigit
DuBench_at_setDigit.restype= c_void_p
DuBench_at_setDigit.argtypes= [c_void_p, c_digit, c_digit]

# DuBench* DuBench_at_setValue( DuBench* self, digit i, double value );
DuBench_at_setValue= core.DuBench_at_setValue
DuBench_at_setValue.restype= c_void_p
DuBench_at_setValue.argtypes= [c_void_p, c_digit, c_double]

# void DuBench_add_reducted( DuBench* self, DuBench* another, DuCode* mask );
DuBench_add_reducted= core.DuBench_add_reducted
DuBench_add_reducted.restype= c_void_p
DuBench_add_reducted.argtypes= [c_void_p, c_void_p, c_void_p]

# digit DuBench_sort( DuBench* self, fctptr_DuBench_compare compare );
DuBench_sort= core.DuBench_sort
DuBench_sort.restype= c_digit
DuBench_sort.argtypes= [c_void_p, c_void_p]

# digit DuBench_switchAt_at( DuBench* self, digit id1, digit id2 );
DuBench_switchAt_at= core.DuBench_switchAt_at
DuBench_switchAt_at.restype= c_digit
DuBench_switchAt_at.argtypes= [c_void_p, c_digit, c_digit]

# bool DuBench_is_codeGreater( DuBench* self, digit i1, digit i2 );
DuBench_is_codeGreater= core.DuBench_is_codeGreater
DuBench_is_codeGreater.restype= c_digit
DuBench_is_codeGreater.argtypes= [c_void_p, c_digit, c_digit]

# bool DuBench_is_codeSmaller( DuBench* self, digit i1, digit i2 );
DuBench_is_codeSmaller= core.DuBench_is_codeSmaller
DuBench_is_codeSmaller.restype= c_digit
DuBench_is_codeSmaller.argtypes= [c_void_p, c_digit, c_digit]

# bool DuBench_is_vectorGreater( DuBench* self, digit i1, digit i2 );
DuBench_is_vectorGreater= core.DuBench_is_vectorGreater
DuBench_is_vectorGreater.restype= c_digit
DuBench_is_vectorGreater.argtypes= [c_void_p, c_digit, c_digit]

# bool DuBench_is_vectorSmaller( DuBench* self, digit i1, digit i2 );
DuBench_is_vectorSmaller= core.DuBench_is_vectorSmaller
DuBench_is_vectorSmaller.restype= c_digit
DuBench_is_vectorSmaller.argtypes= [c_void_p, c_digit, c_digit]

# char* DuBench_print( DuBench* self, char* output );
DuBench_print= core.DuBench_print
DuBench_print.restype= c_void_p
DuBench_print.argtypes= [c_void_p, c_void_p]

# char* DuBench_printCodes( DuBench* self, char* output );
DuBench_printCodes= core.DuBench_printCodes
DuBench_printCodes.restype= c_void_p
DuBench_printCodes.argtypes= [c_void_p, c_void_p]

# char* DuBench_printNetwork( DuBench* self, char* output );
DuBench_printNetwork= core.DuBench_printNetwork
DuBench_printNetwork.restype= c_void_p
DuBench_printNetwork.argtypes= [c_void_p, c_void_p]

# DuTree* newDuTree( digit binarySpaceSize );
newDuTree= core.newDuTree
newDuTree.restype= c_void_p
newDuTree.argtypes= [c_digit]

# DuTree* newDuTreeWith( DuCode* newSpace );
newDuTreeWith= core.newDuTreeWith
newDuTreeWith.restype= c_void_p
newDuTreeWith.argtypes= [c_void_p]

# DuTree* DuTree_createWhith( DuTree* self, DuCode* input );
DuTree_createWhith= core.DuTree_createWhith
DuTree_createWhith.restype= c_void_p
DuTree_createWhith.argtypes= [c_void_p, c_void_p]

# DuTree* DuTree_destroy( DuTree* self );
DuTree_destroy= core.DuTree_destroy
DuTree_destroy.restype= c_void_p
DuTree_destroy.argtypes= [c_void_p]

# void deleteDuTree( DuTree* self );
deleteDuTree= core.deleteDuTree
deleteDuTree.restype= c_void_p
deleteDuTree.argtypes= [c_void_p]

# DuTree* DuTree_reinitWith( DuTree* self, DuCode* newSpace );
DuTree_reinitWith= core.DuTree_reinitWith
DuTree_reinitWith.restype= c_void_p
DuTree_reinitWith.argtypes= [c_void_p, c_void_p]

# DuTree* DuTree_clearWhith_on( DuTree* self, digit index, digit defaultOption );
DuTree_clearWhith_on= core.DuTree_clearWhith_on
DuTree_clearWhith_on.restype= c_void_p
DuTree_clearWhith_on.argtypes= [c_void_p, c_digit, c_digit]

# DuTree* DuTree_clearOn( DuTree* self, digit defaultOption );
DuTree_clearOn= core.DuTree_clearOn
DuTree_clearOn.restype= c_void_p
DuTree_clearOn.argtypes= [c_void_p, c_digit]

# digit DuTree_dimention( DuTree* self );
DuTree_dimention= core.DuTree_dimention
DuTree_dimention.restype= c_digit
DuTree_dimention.argtypes= [c_void_p]

# digit DuTree_size( DuTree* self );
DuTree_size= core.DuTree_size
DuTree_size.restype= c_digit
DuTree_size.argtypes= [c_void_p]

# DuCode* DuTree_inputRanges( DuTree* self );
DuTree_inputRanges= core.DuTree_inputRanges
DuTree_inputRanges.restype= c_void_p
DuTree_inputRanges.argtypes= [c_void_p]

# digit DuTree_at( DuTree* self, DuCode* code );
DuTree_at= core.DuTree_at
DuTree_at.restype= c_digit
DuTree_at.argtypes= [c_void_p, c_void_p]

# digit DuTreeChild( digit key );
DuTreeChild= core.DuTreeChild
DuTreeChild.restype= c_digit
DuTreeChild.argtypes= [c_digit]

# digit DuTreeLeaf( digit key );
DuTreeLeaf= core.DuTreeLeaf
DuTreeLeaf.restype= c_digit
DuTreeLeaf.argtypes= [c_digit]

# void DuTree_reziseCapacity( DuTree* self, digit newCapacity );
DuTree_reziseCapacity= core.DuTree_reziseCapacity
DuTree_reziseCapacity.restype= c_void_p
DuTree_reziseCapacity.argtypes= [c_void_p, c_digit]

# void DuTree_reziseCompleteCapacity( DuTree* self );
DuTree_reziseCompleteCapacity= core.DuTree_reziseCompleteCapacity
DuTree_reziseCompleteCapacity.restype= c_void_p
DuTree_reziseCompleteCapacity.argtypes= [c_void_p]

# digit DuTree_at_set( DuTree* self, DuCode* code, digit output );
DuTree_at_set= core.DuTree_at_set
DuTree_at_set.restype= c_digit
DuTree_at_set.argtypes= [c_void_p, c_void_p, c_digit]

# digit DuTree_at_readOrder_set( DuTree* self, DuCode* code, DuCode* codeOrder, digit output );
DuTree_at_readOrder_set= core.DuTree_at_readOrder_set
DuTree_at_readOrder_set.restype= c_digit
DuTree_at_readOrder_set.argtypes= [c_void_p, c_void_p, c_void_p, c_digit]

# digit DuTree_branchSize( DuTree* self, digit iBranch );
DuTree_branchSize= core.DuTree_branchSize
DuTree_branchSize.restype= c_digit
DuTree_branchSize.argtypes= [c_void_p, c_digit]

# digit DuTree_branch_stateIndex( DuTree* self, digit iBranch, digit state );
DuTree_branch_stateIndex= core.DuTree_branch_stateIndex
DuTree_branch_stateIndex.restype= c_digit
DuTree_branch_stateIndex.argtypes= [c_void_p, c_digit, c_digit]

# digit DuTree_branch_state( DuTree* self, digit iBranch, digit state );
DuTree_branch_state= core.DuTree_branch_state
DuTree_branch_state.restype= c_digit
DuTree_branch_state.argtypes= [c_void_p, c_digit, c_digit]

# digit DuTree_branch_stateIsLeaf( DuTree* self, digit iBranch, digit state );
DuTree_branch_stateIsLeaf= core.DuTree_branch_stateIsLeaf
DuTree_branch_stateIsLeaf.restype= c_digit
DuTree_branch_stateIsLeaf.argtypes= [c_void_p, c_digit, c_digit]

# digit DuTree_branch_stateOption( DuTree* self, digit iBranch, digit state );
DuTree_branch_stateOption= core.DuTree_branch_stateOption
DuTree_branch_stateOption.restype= c_digit
DuTree_branch_stateOption.argtypes= [c_void_p, c_digit, c_digit]

# digit DuTree_branch_stateLeaf( DuTree* self, digit iBranch, digit state );
DuTree_branch_stateLeaf= core.DuTree_branch_stateLeaf
DuTree_branch_stateLeaf.restype= c_digit
DuTree_branch_stateLeaf.argtypes= [c_void_p, c_digit, c_digit]

# digit DuTree_branchVariable( DuTree* self, digit iBranch );
DuTree_branchVariable= core.DuTree_branchVariable
DuTree_branchVariable.restype= c_digit
DuTree_branchVariable.argtypes= [c_void_p, c_digit]

# digit DuTree_branchStart( DuTree* self, digit iBranch );
DuTree_branchStart= core.DuTree_branchStart
DuTree_branchStart.restype= c_digit
DuTree_branchStart.argtypes= [c_void_p, c_digit]

# digit DuTree_branchBound( DuTree* self, digit iBranch );
DuTree_branchBound= core.DuTree_branchBound
DuTree_branchBound.restype= c_digit
DuTree_branchBound.argtypes= [c_void_p, c_digit]

# digit DuTree_branchStep( DuTree* self, digit iBranch );
DuTree_branchStep= core.DuTree_branchStep
DuTree_branchStep.restype= c_digit
DuTree_branchStep.argtypes= [c_void_p, c_digit]

# digit DuTree_branchNumberOfOutputs( DuTree* self, digit branch );
DuTree_branchNumberOfOutputs= core.DuTree_branchNumberOfOutputs
DuTree_branchNumberOfOutputs.restype= c_digit
DuTree_branchNumberOfOutputs.argtypes= [c_void_p, c_digit]

# digit DuTree_deepOf( DuTree* self, DuCode* code );
DuTree_deepOf= core.DuTree_deepOf
DuTree_deepOf.restype= c_digit
DuTree_deepOf.argtypes= [c_void_p, c_void_p]

# digit DuTree_newBranch( DuTree* self, digit iVariable, digit start, digit bound, digit step );
DuTree_newBranch= core.DuTree_newBranch
DuTree_newBranch.restype= c_digit
DuTree_newBranch.argtypes= [c_void_p, c_digit, c_digit, c_digit, c_digit]

# digit DuTree_newBranch_full( DuTree* self, digit iVariable, digit defaultOption );
DuTree_newBranch_full= core.DuTree_newBranch_full
DuTree_newBranch_full.restype= c_digit
DuTree_newBranch_full.argtypes= [c_void_p, c_digit, c_digit]

# digit DuTree_newBranch_binary_options( DuTree* self, digit iVariable, digit  afterValue, digit option1, digit option2 );
DuTree_newBranch_binary_options= core.DuTree_newBranch_binary_options
DuTree_newBranch_binary_options.restype= c_digit
DuTree_newBranch_binary_options.argtypes= [c_void_p, c_digit, c_void_p, c_digit, c_digit]

# digit DuTree_newBranch_pivot_options( DuTree* self, digit iVariable, digit onValue, digit optionBefore, digit optionOn, digit optionAfter );
DuTree_newBranch_pivot_options= core.DuTree_newBranch_pivot_options
DuTree_newBranch_pivot_options.restype= c_digit
DuTree_newBranch_pivot_options.argtypes= [c_void_p, c_digit, c_digit, c_digit, c_digit, c_digit]

# void DuTree_branch_state_connect( DuTree* self, digit branchA, digit stateA, digit branchB );
DuTree_branch_state_connect= core.DuTree_branch_state_connect
DuTree_branch_state_connect.restype= c_void_p
DuTree_branch_state_connect.argtypes= [c_void_p, c_digit, c_digit, c_digit]

# void DuTree_branch_state_setOption( DuTree* self, digit branchA, digit iState, digit outbut );
DuTree_branch_state_setOption= core.DuTree_branch_state_setOption
DuTree_branch_state_setOption.restype= c_void_p
DuTree_branch_state_setOption.argtypes= [c_void_p, c_digit, c_digit, c_digit]

# digit DuTree_cleanDeadBranches( DuTree* self );
DuTree_cleanDeadBranches= core.DuTree_cleanDeadBranches
DuTree_cleanDeadBranches.restype= c_digit
DuTree_cleanDeadBranches.argtypes= [c_void_p]

# digit DuTree_removeBranch( DuTree* self, digit iBranch );
DuTree_removeBranch= core.DuTree_removeBranch
DuTree_removeBranch.restype= c_digit
DuTree_removeBranch.argtypes= [c_void_p, c_digit]

# DuBench* DuTree_asNewBench( DuTree* self );
DuTree_asNewBench= core.DuTree_asNewBench
DuTree_asNewBench.restype= c_void_p
DuTree_asNewBench.argtypes= [c_void_p]

# void DuTree_fromBench( DuTree* self, DuBench* model );
DuTree_fromBench= core.DuTree_fromBench
DuTree_fromBench.restype= c_void_p
DuTree_fromBench.argtypes= [c_void_p, c_void_p]

# char* DuTree_branch_print( DuTree* self, digit iBranch, char* output );
DuTree_branch_print= core.DuTree_branch_print
DuTree_branch_print.restype= c_void_p
DuTree_branch_print.argtypes= [c_void_p, c_digit, c_void_p]

# char* DuTree_print( DuTree* self, char* output );
DuTree_print= core.DuTree_print
DuTree_print.restype= c_void_p
DuTree_print.argtypes= [c_void_p, c_void_p]

# char* DuTree_print_sep( DuTree* self, char* output, char* separator );
DuTree_print_sep= core.DuTree_print_sep
DuTree_print_sep.restype= c_void_p
DuTree_print_sep.argtypes= [c_void_p, c_void_p, c_void_p]

# char* DuTree_print( DuTree* self, char* output );
DuTree_print= core.DuTree_print
DuTree_print.restype= c_void_p
DuTree_print.argtypes= [c_void_p, c_void_p]

# char* DuTree_printInside( DuTree* self, char* output );
DuTree_printInside= core.DuTree_printInside
DuTree_printInside.restype= c_void_p
DuTree_printInside.argtypes= [c_void_p, c_void_p]

# DuValueFct* newDuValueFctBasic( digit inputSize, digit outputSize );
newDuValueFctBasic= core.newDuValueFctBasic
newDuValueFctBasic.restype= c_void_p
newDuValueFctBasic.argtypes= [c_digit, c_digit]

# DuValueFct* newDuValueFctWith( DuCode* newInputRanges, DuVector* newOutputs );
newDuValueFctWith= core.newDuValueFctWith
newDuValueFctWith.restype= c_void_p
newDuValueFctWith.argtypes= [c_void_p, c_void_p]

# DuValueFct* DuValueFct_createWith( DuValueFct* self, DuCode* newInputRanges, DuVector* newOutputs );
DuValueFct_createWith= core.DuValueFct_createWith
DuValueFct_createWith.restype= c_void_p
DuValueFct_createWith.argtypes= [c_void_p, c_void_p, c_void_p]

# DuValueFct* DuValueFct_destroy( DuValueFct* self );
DuValueFct_destroy= core.DuValueFct_destroy
DuValueFct_destroy.restype= c_void_p
DuValueFct_destroy.argtypes= [c_void_p]

# void deleteDuValueFct( DuValueFct* instance );
deleteDuValueFct= core.deleteDuValueFct
deleteDuValueFct.restype= c_void_p
deleteDuValueFct.argtypes= [c_void_p]

# digit DuValueFct_reinitWith( DuValueFct* self, DuCode* newInputRanges, DuVector* newOutputs );
DuValueFct_reinitWith= core.DuValueFct_reinitWith
DuValueFct_reinitWith.restype= c_digit
DuValueFct_reinitWith.argtypes= [c_void_p, c_void_p, c_void_p]

# DuTree* DuValueFct_selector( DuValueFct* self );
DuValueFct_selector= core.DuValueFct_selector
DuValueFct_selector.restype= c_void_p
DuValueFct_selector.argtypes= [c_void_p]

# digit DuValueFct_inputDimention( DuValueFct* self );
DuValueFct_inputDimention= core.DuValueFct_inputDimention
DuValueFct_inputDimention.restype= c_digit
DuValueFct_inputDimention.argtypes= [c_void_p]

# digit DuValueFct_outputSize( DuValueFct* self );
DuValueFct_outputSize= core.DuValueFct_outputSize
DuValueFct_outputSize.restype= c_digit
DuValueFct_outputSize.argtypes= [c_void_p]

# DuCode* DuValueFct_inputRanges( DuValueFct* self );
DuValueFct_inputRanges= core.DuValueFct_inputRanges
DuValueFct_inputRanges.restype= c_void_p
DuValueFct_inputRanges.argtypes= [c_void_p]

# DuVector* DuValueFct_outputs( DuValueFct* self );
DuValueFct_outputs= core.DuValueFct_outputs
DuValueFct_outputs.restype= c_void_p
DuValueFct_outputs.argtypes= [c_void_p]

# double DuValueFct_from( DuValueFct* self, DuCode* input );
DuValueFct_from= core.DuValueFct_from
DuValueFct_from.restype= c_double
DuValueFct_from.argtypes= [c_void_p, c_void_p]

# digit DuValueFct_addValue( DuValueFct* self, double ouputValue );
DuValueFct_addValue= core.DuValueFct_addValue
DuValueFct_addValue.restype= c_digit
DuValueFct_addValue.argtypes= [c_void_p, c_double]

# digit DuValueFct_ouputId_setValue( DuValueFct* self, digit ouputId, double ouputValue );
DuValueFct_ouputId_setValue= core.DuValueFct_ouputId_setValue
DuValueFct_ouputId_setValue.restype= c_digit
DuValueFct_ouputId_setValue.argtypes= [c_void_p, c_digit, c_double]

# digit DuValueFct_from_set( DuValueFct* self, DuCode* input, digit ouputId );
DuValueFct_from_set= core.DuValueFct_from_set
DuValueFct_from_set.restype= c_digit
DuValueFct_from_set.argtypes= [c_void_p, c_void_p, c_digit]

# void DuValueFct_switch( DuValueFct* self, DuValueFct* doppelganger );
DuValueFct_switch= core.DuValueFct_switch
DuValueFct_switch.restype= c_void_p
DuValueFct_switch.argtypes= [c_void_p, c_void_p]

# DuBench* DuValueFct_asNewBench( DuValueFct* self );
DuValueFct_asNewBench= core.DuValueFct_asNewBench
DuValueFct_asNewBench.restype= c_void_p
DuValueFct_asNewBench.argtypes= [c_void_p]

# char* DuValueFct_print( DuValueFct* self, char* buffer );
DuValueFct_print= core.DuValueFct_print
DuValueFct_print.restype= c_void_p
DuValueFct_print.argtypes= [c_void_p, c_void_p]

# char* DuValueFct_printSep( DuValueFct* self, char* buffer, char* separator );
DuValueFct_printSep= core.DuValueFct_printSep
DuValueFct_printSep.restype= c_void_p
DuValueFct_printSep.argtypes= [c_void_p, c_void_p, c_void_p]

# DuFunction* newDuFunctionBasic( digit inputSize );
newDuFunctionBasic= core.newDuFunctionBasic
newDuFunctionBasic.restype= c_void_p
newDuFunctionBasic.argtypes= [c_digit]

# DuFunction* newDuFunctionWith( DuCode* newInputRanges, DuBench* newOutputs );
newDuFunctionWith= core.newDuFunctionWith
newDuFunctionWith.restype= c_void_p
newDuFunctionWith.argtypes= [c_void_p, c_void_p]

# DuFunction* DuFunction_createWith( DuFunction* self, DuCode* newInputRanges, DuBench* newOutputs );
DuFunction_createWith= core.DuFunction_createWith
DuFunction_createWith.restype= c_void_p
DuFunction_createWith.argtypes= [c_void_p, c_void_p, c_void_p]

# DuFunction* DuFunction_destroy( DuFunction* self );
DuFunction_destroy= core.DuFunction_destroy
DuFunction_destroy.restype= c_void_p
DuFunction_destroy.argtypes= [c_void_p]

# void deleteDuFunction( DuFunction* instance );
deleteDuFunction= core.deleteDuFunction
deleteDuFunction.restype= c_void_p
deleteDuFunction.argtypes= [c_void_p]

# DuFunction* DuFunction_reinitWith( DuFunction* self, DuCode* newInputRanges, DuBench* newOutputs );
DuFunction_reinitWith= core.DuFunction_reinitWith
DuFunction_reinitWith.restype= c_void_p
DuFunction_reinitWith.argtypes= [c_void_p, c_void_p, c_void_p]

# DuFunction* DuFunction_reinitWithDefault( DuFunction* self, DuCode* newInputRanges, DuCode* newDefaultOutput, double defaultValue );
DuFunction_reinitWithDefault= core.DuFunction_reinitWithDefault
DuFunction_reinitWithDefault.restype= c_void_p
DuFunction_reinitWithDefault.argtypes= [c_void_p, c_void_p, c_void_p, c_double]

# DuTree* DuFunction_selector( DuFunction* self );
DuFunction_selector= core.DuFunction_selector
DuFunction_selector.restype= c_void_p
DuFunction_selector.argtypes= [c_void_p]

# digit DuFunction_inputDimention( DuFunction* self );
DuFunction_inputDimention= core.DuFunction_inputDimention
DuFunction_inputDimention.restype= c_digit
DuFunction_inputDimention.argtypes= [c_void_p]

# DuCode* DuFunction_inputRanges( DuFunction* self );
DuFunction_inputRanges= core.DuFunction_inputRanges
DuFunction_inputRanges.restype= c_void_p
DuFunction_inputRanges.argtypes= [c_void_p]

# digit DuFunction_outputSize( DuFunction* self );
DuFunction_outputSize= core.DuFunction_outputSize
DuFunction_outputSize.restype= c_digit
DuFunction_outputSize.argtypes= [c_void_p]

# DuBench* DuFunction_outputs( DuFunction* self );
DuFunction_outputs= core.DuFunction_outputs
DuFunction_outputs.restype= c_void_p
DuFunction_outputs.argtypes= [c_void_p]

# digit DuFunction_from( DuFunction* self, DuCode* input );
DuFunction_from= core.DuFunction_from
DuFunction_from.restype= c_digit
DuFunction_from.argtypes= [c_void_p, c_void_p]

# DuCode* DuFunction_codeFrom( DuFunction* self, DuCode* input );
DuFunction_codeFrom= core.DuFunction_codeFrom
DuFunction_codeFrom.restype= c_void_p
DuFunction_codeFrom.argtypes= [c_void_p, c_void_p]

# double DuFunction_valueFrom( DuFunction* self, DuCode* input );
DuFunction_valueFrom= core.DuFunction_valueFrom
DuFunction_valueFrom.restype= c_double
DuFunction_valueFrom.argtypes= [c_void_p, c_void_p]

# digit DuFunction_attachOuput( DuFunction* self, DuCode* newOuputCode, double ouputValue );
DuFunction_attachOuput= core.DuFunction_attachOuput
DuFunction_attachOuput.restype= c_digit
DuFunction_attachOuput.argtypes= [c_void_p, c_void_p, c_double]

# digit DuFunction_from_set( DuFunction* self, DuCode* input, digit ouputId );
DuFunction_from_set= core.DuFunction_from_set
DuFunction_from_set.restype= c_digit
DuFunction_from_set.argtypes= [c_void_p, c_void_p, c_digit]

# void DuFunction_switch( DuFunction* self, DuFunction* doppelganger );
DuFunction_switch= core.DuFunction_switch
DuFunction_switch.restype= c_void_p
DuFunction_switch.argtypes= [c_void_p, c_void_p]

# char* DuFunction_print( DuFunction* self, char* output );
DuFunction_print= core.DuFunction_print
DuFunction_print.restype= c_void_p
DuFunction_print.argtypes= [c_void_p, c_void_p]

# char* DuFunction_printSep( DuFunction* self, char* output, char* separator );
DuFunction_printSep= core.DuFunction_printSep
DuFunction_printSep.restype= c_void_p
DuFunction_printSep.argtypes= [c_void_p, c_void_p, c_void_p]

# DuCondition* newDuConditionBasic( digit domain );
newDuConditionBasic= core.newDuConditionBasic
newDuConditionBasic.restype= c_void_p
newDuConditionBasic.argtypes= [c_digit]

# DuCondition* newDuConditionWith( digit domain, DuCode* newInputRanges, DuBench* newDefaultDistrib );
newDuConditionWith= core.newDuConditionWith
newDuConditionWith.restype= c_void_p
newDuConditionWith.argtypes= [c_digit, c_void_p, c_void_p]

# DuCondition* DuCondition_createBasic( DuCondition* self, digit domain );
DuCondition_createBasic= core.DuCondition_createBasic
DuCondition_createBasic.restype= c_void_p
DuCondition_createBasic.argtypes= [c_void_p, c_digit]

# DuCondition* DuCondition_createWith( DuCondition* self, digit domain, DuCode* newInputRanges, DuBench* newDefaultDistrib );
DuCondition_createWith= core.DuCondition_createWith
DuCondition_createWith.restype= c_void_p
DuCondition_createWith.argtypes= [c_void_p, c_digit, c_void_p, c_void_p]

# DuCondition* DuCondition_destroy( DuCondition* self );
DuCondition_destroy= core.DuCondition_destroy
DuCondition_destroy.restype= c_void_p
DuCondition_destroy.argtypes= [c_void_p]

# void deleteDuCondition( DuCondition* instance );
deleteDuCondition= core.deleteDuCondition
deleteDuCondition.restype= c_void_p
deleteDuCondition.argtypes= [c_void_p]

# digit DuCondition_reinitWith( DuCondition* self, digit domain, DuCode* newInputRanges, DuBench* newDistrib );
DuCondition_reinitWith= core.DuCondition_reinitWith
DuCondition_reinitWith.restype= c_digit
DuCondition_reinitWith.argtypes= [c_void_p, c_digit, c_void_p, c_void_p]

# digit DuCondition_reinitDistributionsWith( DuCondition* self, DuBench* newDistrib );
DuCondition_reinitDistributionsWith= core.DuCondition_reinitDistributionsWith
DuCondition_reinitDistributionsWith.restype= c_digit
DuCondition_reinitDistributionsWith.argtypes= [c_void_p, c_void_p]

# digit DuCondition_range( DuCondition* self );
DuCondition_range= core.DuCondition_range
DuCondition_range.restype= c_digit
DuCondition_range.argtypes= [c_void_p]

# DuTree* DuCondition_selector( DuCondition* self );
DuCondition_selector= core.DuCondition_selector
DuCondition_selector.restype= c_void_p
DuCondition_selector.argtypes= [c_void_p]

# DuCode* DuCondition_parents( DuCondition* self );
DuCondition_parents= core.DuCondition_parents
DuCondition_parents.restype= c_void_p
DuCondition_parents.argtypes= [c_void_p]

# DuBench* DuCondition_from( DuCondition* self, DuCode* configuration );
DuCondition_from= core.DuCondition_from
DuCondition_from.restype= c_void_p
DuCondition_from.argtypes= [c_void_p, c_void_p]

# DuBench* DuCondition_fromKey( DuCondition* self, digit configKey );
DuCondition_fromKey= core.DuCondition_fromKey
DuCondition_fromKey.restype= c_void_p
DuCondition_fromKey.argtypes= [c_void_p, c_digit]

# digit DuCondition_distributionSize( DuCondition* self );
DuCondition_distributionSize= core.DuCondition_distributionSize
DuCondition_distributionSize.restype= c_digit
DuCondition_distributionSize.argtypes= [c_void_p]

# DuBench* DuCondition_distributionAt( DuCondition* self, digit iDistrib );
DuCondition_distributionAt= core.DuCondition_distributionAt
DuCondition_distributionAt.restype= c_void_p
DuCondition_distributionAt.argtypes= [c_void_p, c_digit]

# digit DuCondition_attach( DuCondition* self, DuBench* distribution );
DuCondition_attach= core.DuCondition_attach
DuCondition_attach.restype= c_digit
DuCondition_attach.argtypes= [c_void_p, c_void_p]

# digit DuCondition_from_attach( DuCondition* self, DuCode* configuration, DuBench* distribution );
DuCondition_from_attach= core.DuCondition_from_attach
DuCondition_from_attach.restype= c_digit
DuCondition_from_attach.argtypes= [c_void_p, c_void_p, c_void_p]

# void DuCondition_switch( DuCondition* self, DuCondition* doppelganger );
DuCondition_switch= core.DuCondition_switch
DuCondition_switch.restype= c_void_p
DuCondition_switch.argtypes= [c_void_p, c_void_p]

# DuBench* DuCondition_infer( DuCondition* self, DuBench* distribOverConfigurations );
DuCondition_infer= core.DuCondition_infer
DuCondition_infer.restype= c_void_p
DuCondition_infer.argtypes= [c_void_p, c_void_p]

# DuBench* DuCondition_newDistributionByInfering( DuCondition* self, DuBench* distribOverConfigurations );
DuCondition_newDistributionByInfering= core.DuCondition_newDistributionByInfering
DuCondition_newDistributionByInfering.restype= c_void_p
DuCondition_newDistributionByInfering.argtypes= [c_void_p, c_void_p]

# DuBench* DuCondition_newDistributionByInfering_mask( DuCondition* self, DuBench* longDistrib, DuCode* parentMask );
DuCondition_newDistributionByInfering_mask= core.DuCondition_newDistributionByInfering_mask
DuCondition_newDistributionByInfering_mask.restype= c_void_p
DuCondition_newDistributionByInfering_mask.argtypes= [c_void_p, c_void_p, c_void_p]

# char* DuCondition_print( DuCondition* self, char* output );
DuCondition_print= core.DuCondition_print
DuCondition_print.restype= c_void_p
DuCondition_print.argtypes= [c_void_p, c_void_p]

# char* DuCondition_printSep( DuCondition* self, char* output, char* separator );
DuCondition_printSep= core.DuCondition_printSep
DuCondition_printSep.restype= c_void_p
DuCondition_printSep.argtypes= [c_void_p, c_void_p, c_void_p]

# char* DuCondition_printExtend( DuCondition* self, char* output );
DuCondition_printExtend= core.DuCondition_printExtend
DuCondition_printExtend.restype= c_void_p
DuCondition_printExtend.argtypes= [c_void_p, c_void_p]

# char* DuCondition_printExtendSep( DuCondition* self, char* output, char* separator );
DuCondition_printExtendSep= core.DuCondition_printExtendSep
DuCondition_printExtendSep.restype= c_void_p
DuCondition_printExtendSep.argtypes= [c_void_p, c_void_p, c_void_p]

# char* DuCondition_printIdentity( DuCondition* self, char* output );
DuCondition_printIdentity= core.DuCondition_printIdentity
DuCondition_printIdentity.restype= c_void_p
DuCondition_printIdentity.argtypes= [c_void_p, c_void_p]

# DuInferer* newDuInferer( DuCode* variableSpace, digit inputDimention, digit outputDimention );
newDuInferer= core.newDuInferer
newDuInferer.restype= c_void_p
newDuInferer.argtypes= [c_void_p, c_digit, c_digit]

# DuInferer* newDuInfererStateAction( DuCode* stateSpace, DuCode* actionSpace );
newDuInfererStateAction= core.newDuInfererStateAction
newDuInfererStateAction.restype= c_void_p
newDuInfererStateAction.argtypes= [c_void_p, c_void_p]

# DuInferer* newDuInfererStateActionShift( DuCode* stateSpace, DuCode* actionSpace, DuCode* shiftSpace );
newDuInfererStateActionShift= core.newDuInfererStateActionShift
newDuInfererStateActionShift.restype= c_void_p
newDuInfererStateActionShift.argtypes= [c_void_p, c_void_p, c_void_p]

# DuInferer* DuInferer_create( DuInferer* self, DuCode* varDomains, digit inputDimention, digit outputDimention );
DuInferer_create= core.DuInferer_create
DuInferer_create.restype= c_void_p
DuInferer_create.argtypes= [c_void_p, c_void_p, c_digit, c_digit]

# DuInferer* DuInferer_destroy( DuInferer* self );
DuInferer_destroy= core.DuInferer_destroy
DuInferer_destroy.restype= c_void_p
DuInferer_destroy.argtypes= [c_void_p]

# void deleteDuInferer( DuInferer* self );
deleteDuInferer= core.deleteDuInferer
deleteDuInferer.restype= c_void_p
deleteDuInferer.argtypes= [c_void_p]

# DuBench* DuInferer_distribution( DuInferer* self );
DuInferer_distribution= core.DuInferer_distribution
DuInferer_distribution.restype= c_void_p
DuInferer_distribution.argtypes= [c_void_p]

# digit DuInferer_inputDimention( DuInferer* self );
DuInferer_inputDimention= core.DuInferer_inputDimention
DuInferer_inputDimention.restype= c_digit
DuInferer_inputDimention.argtypes= [c_void_p]

# digit DuInferer_outputDimention( DuInferer* self );
DuInferer_outputDimention= core.DuInferer_outputDimention
DuInferer_outputDimention.restype= c_digit
DuInferer_outputDimention.argtypes= [c_void_p]

# digit DuInferer_shiftDimention( DuInferer* self );
DuInferer_shiftDimention= core.DuInferer_shiftDimention
DuInferer_shiftDimention.restype= c_digit
DuInferer_shiftDimention.argtypes= [c_void_p]

# digit DuInferer_overallDimention( DuInferer* self );
DuInferer_overallDimention= core.DuInferer_overallDimention
DuInferer_overallDimention.restype= c_digit
DuInferer_overallDimention.argtypes= [c_void_p]

# DuCondition* DuInferer_node( DuInferer* self, digit iNode );
DuInferer_node= core.DuInferer_node
DuInferer_node.restype= c_void_p
DuInferer_node.argtypes= [c_void_p, c_digit]

# digit DuInferer_node_size( DuInferer* self, digit iVar );
DuInferer_node_size= core.DuInferer_node_size
DuInferer_node_size.restype= c_digit
DuInferer_node_size.argtypes= [c_void_p, c_digit]

# DuCode* DuInferer_node_parents( DuInferer* self, digit iVar );
DuInferer_node_parents= core.DuInferer_node_parents
DuInferer_node_parents.restype= c_void_p
DuInferer_node_parents.argtypes= [c_void_p, c_digit]

# DuCondition* DuInferer_reinitIndependantNode( DuInferer* self, digit index );
DuInferer_reinitIndependantNode= core.DuInferer_reinitIndependantNode
DuInferer_reinitIndependantNode.restype= c_void_p
DuInferer_reinitIndependantNode.argtypes= [c_void_p, c_digit]

# DuCondition* DuInferer_node_reinitWith( DuInferer* self, digit index, DuCode* newParents );
DuInferer_node_reinitWith= core.DuInferer_node_reinitWith
DuInferer_node_reinitWith.restype= c_void_p
DuInferer_node_reinitWith.argtypes= [c_void_p, c_digit, c_void_p]

# DuCondition* DuInferer_node_reinitWith_withDefault( DuInferer* self, digit index, DuCode* newDependenceList, DuBench* newDefaultDistrib );
DuInferer_node_reinitWith_withDefault= core.DuInferer_node_reinitWith_withDefault
DuInferer_node_reinitWith_withDefault.restype= c_void_p
DuInferer_node_reinitWith_withDefault.argtypes= [c_void_p, c_digit, c_void_p, c_void_p]

# DuBench* DuInferer_process( DuInferer* self, DuBench* inputDistribution );
DuInferer_process= core.DuInferer_process
DuInferer_process.restype= c_void_p
DuInferer_process.argtypes= [c_void_p, c_void_p]

# DuBench* DuInferer_process_newOverallDistribution( DuInferer* self, DuBench* inputDistribution );
DuInferer_process_newOverallDistribution= core.DuInferer_process_newOverallDistribution
DuInferer_process_newOverallDistribution.restype= c_void_p
DuInferer_process_newOverallDistribution.argtypes= [c_void_p, c_void_p]

# DuBench* DuInferer_processState_Action( DuInferer* self, DuCode* state, DuCode* action );
DuInferer_processState_Action= core.DuInferer_processState_Action
DuInferer_processState_Action.restype= c_void_p
DuInferer_processState_Action.argtypes= [c_void_p, c_void_p, c_void_p]

# char* DuInferer_print( DuInferer* self, char* output );
DuInferer_print= core.DuInferer_print
DuInferer_print.restype= c_void_p
DuInferer_print.argtypes= [c_void_p, c_void_p]

# char* DuInferer_printStateActionSignature( DuInferer* self, char* output );
DuInferer_printStateActionSignature= core.DuInferer_printStateActionSignature
DuInferer_printStateActionSignature.restype= c_void_p
DuInferer_printStateActionSignature.argtypes= [c_void_p, c_void_p]

# char* DuInferer_printDependency( DuInferer* self, char* output );
DuInferer_printDependency= core.DuInferer_printDependency
DuInferer_printDependency.restype= c_void_p
DuInferer_printDependency.argtypes= [c_void_p, c_void_p]

# DuEvaluator* newDuEvaluatorBasic( digit spaceDimention, digit numberOfCriteria );
newDuEvaluatorBasic= core.newDuEvaluatorBasic
newDuEvaluatorBasic.restype= c_void_p
newDuEvaluatorBasic.argtypes= [c_digit, c_digit]

# DuEvaluator* newDuEvaluatorWith( DuCode* newSpace, digit numberOfCriteria );
newDuEvaluatorWith= core.newDuEvaluatorWith
newDuEvaluatorWith.restype= c_void_p
newDuEvaluatorWith.argtypes= [c_void_p, c_digit]

# DuEvaluator* DuEvaluator_createWith( DuEvaluator* self, DuCode* newSpace, digit numberOfCriteria );
DuEvaluator_createWith= core.DuEvaluator_createWith
DuEvaluator_createWith.restype= c_void_p
DuEvaluator_createWith.argtypes= [c_void_p, c_void_p, c_digit]

# void deleteDuEvaluator( DuEvaluator* self );
deleteDuEvaluator= core.deleteDuEvaluator
deleteDuEvaluator.restype= c_void_p
deleteDuEvaluator.argtypes= [c_void_p]

# DuEvaluator* DuEvaluator_destroy( DuEvaluator* self );
DuEvaluator_destroy= core.DuEvaluator_destroy
DuEvaluator_destroy.restype= c_void_p
DuEvaluator_destroy.argtypes= [c_void_p]

# DuCode* DuEvaluator_space( DuEvaluator* self );
DuEvaluator_space= core.DuEvaluator_space
DuEvaluator_space.restype= c_void_p
DuEvaluator_space.argtypes= [c_void_p]

# digit DuEvaluator_numberOfCriteria( DuEvaluator* self );
DuEvaluator_numberOfCriteria= core.DuEvaluator_numberOfCriteria
DuEvaluator_numberOfCriteria.restype= c_digit
DuEvaluator_numberOfCriteria.argtypes= [c_void_p]

# DuValueFct* DuEvaluator_criterion( DuEvaluator* self, digit iCritirion );
DuEvaluator_criterion= core.DuEvaluator_criterion
DuEvaluator_criterion.restype= c_void_p
DuEvaluator_criterion.argtypes= [c_void_p, c_digit]

# DuVector* DuEvaluator_weights( DuEvaluator* self );
DuEvaluator_weights= core.DuEvaluator_weights
DuEvaluator_weights.restype= c_void_p
DuEvaluator_weights.argtypes= [c_void_p]

# double DuEvaluator_criterion_weight( DuEvaluator* self, digit iCritirion );
DuEvaluator_criterion_weight= core.DuEvaluator_criterion_weight
DuEvaluator_criterion_weight.restype= c_double
DuEvaluator_criterion_weight.argtypes= [c_void_p, c_digit]

# DuCode* DuEvaluator_criterion_mask( DuEvaluator* self, digit iCritirion );
DuEvaluator_criterion_mask= core.DuEvaluator_criterion_mask
DuEvaluator_criterion_mask.restype= c_void_p
DuEvaluator_criterion_mask.argtypes= [c_void_p, c_digit]

# double DuEvaluator_process( DuEvaluator* self, DuCode* input );
DuEvaluator_process= core.DuEvaluator_process
DuEvaluator_process.restype= c_double
DuEvaluator_process.argtypes= [c_void_p, c_void_p]

# double DuEvaluator_criterion_process( DuEvaluator* self, digit iCriterion, DuCode* input );
DuEvaluator_criterion_process= core.DuEvaluator_criterion_process
DuEvaluator_criterion_process.restype= c_double
DuEvaluator_criterion_process.argtypes= [c_void_p, c_digit, c_void_p]

# double DuEvaluator_processState_action( DuEvaluator* self, DuCode* state, DuCode* action );
DuEvaluator_processState_action= core.DuEvaluator_processState_action
DuEvaluator_processState_action.restype= c_double
DuEvaluator_processState_action.argtypes= [c_void_p, c_void_p, c_void_p]

# double DuEvaluator_processState_action_state( DuEvaluator* self, DuCode* state, DuCode* action, DuCode* statePrime );
DuEvaluator_processState_action_state= core.DuEvaluator_processState_action_state
DuEvaluator_processState_action_state.restype= c_double
DuEvaluator_processState_action_state.argtypes= [c_void_p, c_void_p, c_void_p, c_void_p]

# DuEvaluator* DuEvaluator_reinitCriterion( DuEvaluator* self, digit numberOfCriterion );
DuEvaluator_reinitCriterion= core.DuEvaluator_reinitCriterion
DuEvaluator_reinitCriterion.restype= c_void_p
DuEvaluator_reinitCriterion.argtypes= [c_void_p, c_digit]

# DuValueFct* DuEvaluator_criterion_reinitWith( DuEvaluator* self, digit iCrit, DuCode* newDependenceMask, DuVector* newValues );
DuEvaluator_criterion_reinitWith= core.DuEvaluator_criterion_reinitWith
DuEvaluator_criterion_reinitWith.restype= c_void_p
DuEvaluator_criterion_reinitWith.argtypes= [c_void_p, c_digit, c_void_p, c_void_p]

# void DuEvaluator_criterion_from_set( DuEvaluator* self, digit index, DuCode* option, digit output );
DuEvaluator_criterion_from_set= core.DuEvaluator_criterion_from_set
DuEvaluator_criterion_from_set.restype= c_void_p
DuEvaluator_criterion_from_set.argtypes= [c_void_p, c_digit, c_void_p, c_digit]

# void DuEvaluator_criterion_setWeight( DuEvaluator* self, digit iCritirion, double weight );
DuEvaluator_criterion_setWeight= core.DuEvaluator_criterion_setWeight
DuEvaluator_criterion_setWeight.restype= c_void_p
DuEvaluator_criterion_setWeight.argtypes= [c_void_p, c_digit, c_double]
