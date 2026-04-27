#!env python3
"""
Simple 421 game with bbmm.
"""

import src.demuu as bbmm

def generate():
    # InitialigenerateModelze The Domains:
    diceDomain= range(1,7)
    horizonDomain= range( 3 )
    actionDomain= ["roll", "keep"]

    # Initialize the model with the variables:
    model= bbmm.Model(
        stateVariables= {
            "H": horizonDomain,
            "D1": diceDomain,
            "D2": diceDomain,
            "D3": diceDomain
        },

        actionVariables= {
            "A1": actionDomain,
            "A2": actionDomain,
            "A3": actionDomain
        },

        shiftVariables= {
            "ID1": diceDomain,
            "ID2": diceDomain,
            "ID3": diceDomain
        }
    )

    # Initialize the horizon variable dependancies:
    model.node( "H-1" ).create(
        ["H-0"],
        lambda config: [(max( config[0]-1, 0 ), 1.0)] # decrizing horizon limited to 0
    )

    # Initialize the keep or roll dependancies:
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

    # Sort the output dices:
    def sortOutput( aList, x ):
        aList.sort()
        return [( aList[x], 1.0 )] # The Xime value in the order 

    # Initialize max value:
    model.node( f"D1-1").create(
        ["ID1", "ID2", "ID3" ], 
        lambda config: sortOutput(config, 2)
    )

    # Initialize medium value:
    model.node( f"D2-1").create(
        ["ID1", "ID2", "ID3" ],
        lambda config: sortOutput(config, 1)
    )

    # Initialize min value:
    model.node( f"D3-1").create(
        ["ID1", "ID2", "ID3" ], 
        lambda config: sortOutput(config, 0)
    )

    # reward
    crit= model.criterion().initialize( ['H-0', 'D1-1', 'D2-1', 'D3-1'], [0.0] )
    crit.from_set( [1, 4, 2, 1], 800.0 )
    crit.from_set( [1, 1, 1, 1], 700.0 )
    crit.from_set( [1, 2, 1, 1], 502.0 )
    crit.from_set( [1, 3, 1, 1], 503.0 )
    crit.from_set( [1, 4, 1, 1], 504.0 )
    crit.from_set( [1, 5, 1, 1], 505.0 )
    crit.from_set( [1, 6, 1, 1], 506.0 )
    crit.from_set( [1, 2, 2, 1], -100.0 )

    return model
