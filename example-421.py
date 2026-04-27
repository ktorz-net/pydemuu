#!/usr/bin/python3
"""
Simple 421 game with demuu.
"""

#------ System :
import platform
print( f"Machine on {platform.system()}-{platform.machine()}" )

#------
import demuu

# Initialize the varible Domains:
diceDomain= range(1, 7)
horizonDomain= range(3)
actionDomain= ["roll", "keep"]

# Initialize the model with the variables:
model= demuu.Model(
    stateVariables= { # The state varibales - name: domain
        "H": horizonDomain,
        "D1": diceDomain,
        "D2": diceDomain,
        "D3": diceDomain
    },

    actionVariables= { # The action varibales - name: domain
        "A1": actionDomain,
        "A2": actionDomain,
        "A3": actionDomain
    },

    shiftVariables= { # The shift varibales - name: domain
        "ID1": diceDomain,
        "ID2": diceDomain,
        "ID3": diceDomain
    }
)
# Shift varibales are intermediate variables used to build state transitions
# For 421, the tuple (ID1, ID2, ID3) models the rolled dices before sort step.
# At the end D1' is the smallest value of ID1, ID2 or ID3, D2' the medium and D3' the higher.

# Initialize the horizon variable dependancies:
model.node( "H-1" ).create(
    ["H-0"],
    lambda config: [(max( config[0]-1, 0 ), 1.0)] # Decrizing horizon limited to 0
)

# Initialize the 3 (keep or roll) dependancies on the shift varibales:
for i in range(1, 4) :
    # a random value by default
    nodeD= model.node( f"ID{i}").initialize( [f"A{i}", f"D{i}-0"], [(1, 1/6), (2, 1/6), (3, 1/6), (4, 1/6), (5, 1/6), (6, 1/6)] ) 
    # The keeped value with a probability 1.0 :
    nodeD.setConditionalDistribution( ["keep", 1], [(1, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 2], [(2, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 3], [(3, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 4], [(4, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 5], [(5, 1.0)] )
    nodeD.setConditionalDistribution( ["keep", 6], [(6, 1.0)] )

# A function for sorting the shift dices:
def sortOutput( aList, x ):
    aList.sort()
    return [( aList[x], 1.0 )] # The Xime value in the order 

# Initialize max dice ouput (D1-1 variable):
model.node( f"D1-1").create(
    ["ID1", "ID2", "ID3" ], 
    lambda config: sortOutput(config, 2)
)

# Initialize medium dice ouput (D2-1 variable):
model.node( f"D2-1").create(
    ["ID1", "ID2", "ID3" ],
    lambda config: sortOutput(config, 1)
)

# Initialize min dice ouput (D3-1 variable):
model.node( f"D3-1").create(
    ["ID1", "ID2", "ID3" ], 
    lambda config: sortOutput(config, 0)
)

# reward depending on the horizon, and the final obtained dices (Default on 0)
crit= model.criterion().initialize( ['H-0', 'D1-1', 'D2-1', 'D3-1'], [0.0] )
crit.from_set( [1, None, None, None], 100.0 ) # Default on 100.0 at the end (H==1), without condition on the dice confifuration
# Set more specific reward at H==1
crit.from_set( [1, 4, 2, 1], 800.0 )
crit.from_set( [1, 1, 1, 1], 600.0 )
for v in range(2, 7):
    crit.from_set( [1, v, 1, 1], 400.0 + v )
    crit.from_set( [1, v, v, v], 300.0 + v )
for v in range(3, 7):
    crit.from_set( [1, v, v-1, v-2], 200.0 + v )
crit.from_set( [1, 2, 2, 1], 0.0 )

# Tests: 
def printTransition( state, action ):
    print( f"transition from {state}, {action}:")
    for future, proba in model.transition( state, action ):
        print( f"- P({future})= {round(proba, 3)}, reward= {model.reward(state, action, future)} " )

printTransition( [2, 3, 3, 1], ['keep', 'keep', 'keep'] )
printTransition( [1, 3, 3, 1], ['roll', 'roll', 'keep'] )
