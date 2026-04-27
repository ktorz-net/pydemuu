from . import clibdemuu as cc
from .clibdemuu import c_digit

# DuCode wrap:
class Code :

    # Construction destruction:
    def __init__(self, aList=[], ccode= None):
        
        if ccode is None :
            size= len(aList)
            if size == 0 :
                self._ccode= cc.newDuCode( c_digit(0) )
            else :
                self._ccode= cc.newDuCode_numbers(
                    c_digit(size),
                    cc.makeCArrayAs( c_digit, size, aList )
                )
            self._cmaster= True
        else : 
            self._ccode= ccode
            self._cmaster= False

    def __del__(self):
        if self._cmaster :
            cc.deleteDuCode( self._ccode )

    # initialize:
    def initialize(self, aList):
        size= len(aList)
        cc.DuCode_reinit( self._ccode, c_digit(size) )
        cc.DuCode_setNumbers( self._ccode, cc.makeCArrayAs( c_digit, size, aList ) )
        return self
    
    def copy(self):
        cpy= Code()
        cc.DuCode_copy( cpy._ccode, self._ccode )
        return cpy

    # Accessor
    def dimention(self):
        return (int)(cc.DuCode_dimention( self._ccode ) )

    def digit(self, i):
        assert( 0 < i and i <= self.dimention() )
        return (int)(cc.DuCode_digit( self._ccode, (c_digit)(i) ) )    

    def asList(self):
        return [ self.digit(i) for i in range(1, self.dimention()+1) ]

    # comparizon:
    def __eq__(a, b):
        return (int)( cc.DuCode_isEqualTo(a._ccode, b._ccode) ) != 0
    def __ne__(a, b):
        return (int)( cc.DuCode_isEqualTo(a._ccode, b._ccode) ) == 0
    def __lt__(a, b):
        return (int)( cc.DuCode_isSmallerThan(a._ccode, b._ccode) ) != 0
    def __gt__(a, b):
        return (int)( cc.DuCode_isGreaterThan(a._ccode, b._ccode) ) != 0
    def __le__(a, b):
        return (int)( cc.DuCode_isGreaterThan(a._ccode, b._ccode) ) == 0
    def __ge__(a, b):
        return (int)( cc.DuCode_isSmallerThan(a._ccode, b._ccode) ) == 0

    # Modification
    def resize(self, size):
        cc.DuCode_redimention(self._ccode, c_digit(size))
    
    def at_set(self, i, value):
        assert( 0 < i and i <= self.dimention() )
        cc.DuCode_at_set(self._ccode, c_digit(i), c_digit(value) )

    # Iterate
    def __iter__(self):
        self.a = 1
        return IterCode(self)
    
    # dump and load:
    def dump(self):
        descriptor= self.asList()
        return descriptor
    
    def load(self, descriptor):
        return self.initialize( descriptor )
    
    # Print 
    def __str__(self):
        size= self.dimention()
        if size == 0 :
            return "code[]"
        s= "code["+ str( self.digit(1) )
        for i in range(2, size+1) :
            s+= ", "+ str( self.digit(i) )
        return s+"]"

class IterCode :

    # Construction destruction:
    def __init__( self, aCode ):
        self.conf= Code( [1 for i in range(aCode.dimention())] )
        self.range= aCode

    # Iterate
    def __iter__(self):
        self.conf= Code( [1 for i in range(self.range.dimention())] )
        return self
    
    def __next__(self):
        if cc.DuCode_isIncluding( self.range._ccode, self.conf._ccode ) :
            lst= self.conf.asList()
            cc.DuCode_nextCode( self.range._ccode, self.conf._ccode )
            return lst
        else:
            raise StopIteration
