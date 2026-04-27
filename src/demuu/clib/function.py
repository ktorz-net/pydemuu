from ctypes import c_uint, c_double, c_void_p, c_ulong
import os

from numpy import empty
from . import clibdemuu as cc
from .code import Code
from .bench import Bench
from .bench import Bench
from .tree import Tree

class Function:
    # Construction destruction:
    def __init__(self, inputRanges=[1], outputs=[([0], [0.0])], cfunction= None):
        if cfunction is None :
            inputCode= Code( inputRanges )
            outputBench= Bench( outputs )
            self._cfunction= cc.newDuFunctionWith(
                inputCode._ccode,
                outputBench._cbench
            )
            inputCode._cmaster= False
            outputBench._cmaster= False
            self._cmaster= True
        else: 
            self._cfunction= cfunction
            self._cmaster= False
    
    def __del__(self):
        if self._cmaster :
            cc.deleteDuFunction( self._cfunction )