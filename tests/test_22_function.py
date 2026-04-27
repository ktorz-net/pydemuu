import sys
sys.path.insert( 1, __file__.split('tests')[0] )

# ------------------------------------------------------------------------ #
#                T E S T   p y B b M m  : :  C R I T E R I O N             #
# ------------------------------------------------------------------------ #

import src.demuu.clib as du
from src.demuu.clib import clibdemuu as cc

def test_DuFunction_init():
    instance= du.Function()
    assert type(instance) == du.Function