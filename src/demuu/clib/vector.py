from .clibdemuu import c_digit, c_double
from . import clibdemuu as cc

# DuVector wrap:
class Vector :

    # Construction destruction:
    def __init__(self, aList=[], cvector= None ):
        if cvector is None :
            size= len(aList)
            if size == 0 :
                self._cvector= cc.newDuVector( c_digit(0) )
            else :
                self._cvector= cc.newDuVector_values(
                    c_digit(size),
                    cc.makeCArrayAs( c_double, size, aList )
                )
            self._cmaster= True
        else : 
            self._cvector= cvector
            self._cmaster= False


    def __del__(self):
        if self._cmaster :
            cc.deleteDuVector( self._cvector )

    # initialize:
    def initialize(self, aList):
        size= len(aList)
        cc.DuVector_reinit( self._cvector, c_digit(size) )
        cc.DuVector_setValues( self._cvector, cc.makeCArrayAs( c_double, size, aList ) )
        return self
    
    def copy(self):
        cpy= Vector()
        cc.DuVector_copy( cpy._cvector, self._cvector )
        return cpy

    # Accessor
    def dimention(self):
        return (int)(cc.DuVector_dimention( self._cvector ) )

    def value(self, i):
        assert( 0 < i and i <= self.dimention() )
        return (float)(cc.DuVector_value( self._cvector, (c_digit)(i) ) )    

    def asList(self):
        return [ self.value(i) for i in range(1, self.dimention()+1) ]
    
    # comparizon:
    def __eq__(a, b):
        return (int)( cc.DuVector_isEqualTo(a._cvector, b._cvector) ) != 0
    def __ne__(a, b):
        return (int)( cc.DuVector_isEqualTo(a._cvector, b._cvector) ) == 0
    def __lt__(a, b):
        return (int)( cc.DuVector_isSmallerThan(a._cvector, b._cvector) ) != 0
    def __gt__(a, b):
        return (int)( cc.DuVector_isGreaterThan(a._cvector, b._cvector) ) != 0
    def __le__(a, b):
        return (int)( cc.DuVector_isGreaterThan(a._cvector, b._cvector) ) == 0
    def __ge__(a, b):
        return (int)( cc.DuVector_isSmallerThan(a._cvector, b._cvector) ) == 0

    # Modification
    def resize(self, size):
        cc.DuVector_redimention(self._cvector, c_digit(size))
    
    def at_set(self, i, value):
        assert( 0 < i and i <= self.dimention() )
        cc.DuVector_at_set(self._cvector, c_digit(i), c_double(value) )

    # dump and load:
    def dump(self):
        descriptor= self.asList()
        return descriptor
    
    def load(self, descriptor):
        return self.initialize( descriptor )