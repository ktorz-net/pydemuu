from .clibdemuu import c_digit, c_double
from . import clibdemuu as cc
from .code import Code
from .bench import Bench

# DuTree wrap:
class Tree :
    # Construction destruction:
    def __init__(self, space=[1], ctree= None):
        if ctree is None :
            codeSpace= Code( space )
            self._ctree= cc.newDuTreeWith( codeSpace._ccode )
            codeSpace._cmaster= False
            self._cmaster= True
        else: 
            self._ctree= ctree
            self._cmaster= False
    
    def __del__(self):
        if self._cmaster :
            cc.deleteDuTree( self._ctree )

    # Accessor
    def size(self):
        return cc.DuTree_size( self._ctree )
    
    def inputs(self):
        return Code( ccode=cc.DuTree_inputRanges( self._ctree ) ).asList()
    
    def atCode( self, code ):
        return cc.DuTree_at( self._ctree, code._ccode)
    
    def at( self, codeList ):
        code= Code(codeList)
        return self.atCode( code )

    # Generating
    def asBench( self ):
        bench= Bench( cbench= cc.DuTree_asNewBench( self._ctree ) )
        bench._cmaster= True
        return bench

    # Construction
    def initialize( self, inputRanges ):
        codeSpace= Code( inputRanges )
        self._ctree= cc.DuTree_reinitWith(
            self._ctree,
            codeSpace._ccode
        )
        codeSpace._cmaster= False
        return self
    
    def clear( self, defaultOutput=1, iInput=1 ):
        cc.DuTree_clearWhith_on( self._ctree, c_digit(iInput), c_digit(defaultOutput) )

    def atCode_set( self, code, option ):
        cc.DuTree_at_set( self._ctree, code._ccode, c_digit(option) )

    def at_set( self, codeList, option ):
        return self.atCode_set( Code( codeList ), option )

    def option_setValue( self, iOption, value ):
        cc.DuTree_option_setValue(
            self._ctree,
            c_digit(iOption),
            c_double(value)
        )
    
    # branch manipulation
    def iBranch_variable(self, iBranch):
        return cc.DuTree_branchVariable( self._ctree, c_digit(iBranch) )

    def iBranch_size(self, iBranch):
        return cc.DuTree_branchSize( self._ctree, c_digit(iBranch) )

    def iBranch_state(self, iBranch, index):
        key= cc.DuTree_branch_state( self._ctree, c_digit(iBranch), c_digit(index) )
        leaf= cc.DuTreeLeaf(key)
        if leaf > 0 :
            return ( "leaf", leaf )
        return ( "child", cc.DuTreeChild(key) )

    def iBranch_states(self, iBranch):
        return [
            self.iBranch_state( iBranch, i+1 )
            for i in range( self.iBranch_size(iBranch) )
        ]
    
    # dump and load:
    def dump(self):
        descriptor= {
            "input": self.inputs(),
            "branches": [
                { "child": i, "iInput": self.iBranch_variable(i), "states": self.iBranch_states(i) }
                for i in range( self.size() )
            ]
        }
        return descriptor
    
    def load(self, descriptor):
        self.initialize( descriptor["input"] )
        iBranch= 0
        for bDes in descriptor["branches"] :
            r= cc.DuTree_newBranch_full( self._ctree, c_digit( bDes["iInput"] ), c_digit(1))
            assert( int(r) == iBranch )
            index= 1
            for sType, sValue in bDes["states"] :
                if sType == 'leaf' :
                    cc.DuTree_branch_state_setOption( self._ctree, r, c_digit(index), c_digit(sValue) )
                else :
                    cc.DuTree_branch_state_connect( self._ctree, r, c_digit(index), c_digit(sValue) )
                index+= 1
            iBranch+= 1
        return self
