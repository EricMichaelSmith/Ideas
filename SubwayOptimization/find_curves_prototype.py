# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 12:39:04 2014

@author: Eric Smith
"""

import numpy as np
from scipy.cluster.vq import *


def find_curves_prototype():
    """Run entire prototype of generating a population distribution, fitting curves to it, and plotting the output."""    

#   Define sample population distribution.
#   Create weight matrix from the distribution.
#   For each curve:
#       Find best-fit curve through logistic regression.
#       Calculate contribution of curve to weight matrix.
#       Subtract contribution from weight matrix.
#   Plot sample distribution.
#   Plot curves on top of distribution.
#   On separate figure, plot remainder of weight matrix.



def create_sample_distribution():
    distributionM = abs(np.random.randn(128, 128))
    
    cloudCenter2C = np.array([[30, 15],
                              [20, 30],
                              [100, 100]])
    cloudMagnitudeC = np.array([10, 7, 15])
    
    
    numClouds = shape(cloudCenter2C)[0]
    numXPoints = shape(distM)[0]
    numYPoints = shape(distM)[1]
    for lCloud in range(numClouds):
        distanceM = np.array(shape(distributionM))
        # Create empty distance array
        
        for lXPoint in range(numXPoints):
            for lYPoint in range(numYPoints):
                