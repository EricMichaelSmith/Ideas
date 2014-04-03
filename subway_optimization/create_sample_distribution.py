# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:42:03 2014

@author: Eric

2014-02-16: okay, you have the Gaussian cloud, but add some noise to it!
"""

import math
import matplotlib.pyplot as plt
import numpy as np



def main(plotDistributionL = True):
    """Creates a simple distribution comprised of three Gaussian-noise, Gaussian-shaped probability clouds with a Gaussian-noise background."""

    numXPoints = 128
    numYPoints = 128
    distributionM = abs(0.3*np.random.randn(numXPoints, numYPoints))
    
    # Add background noise
    cloudCenter2C = np.array([[40, 15],
                              [20, 60],
                              [100, 100]])
    cloudMagnitudeC = np.array([100, 70, 150])
    cloudWidthC = np.array([7, 7, 7])
    
    # Add Gaussian clouds with Gaussian noise
    numClouds = cloudCenter2C.shape[0]
    for lCloud in range(numClouds):
        additionalDistributionM = np.zeros(distributionM.shape)
        additionalDistributionM.fill(np.nan)
        # Create empty array containing the amount by which this cloud adds onto the existing distribution
        
        for lXPoint in range(numXPoints):
            for lYPoint in range(numYPoints):
                
                # Setting up the exponential
                squaredDistance = \
                    math.sqrt((lXPoint-cloudCenter2C[lCloud, 0])**2 +
                    (lYPoint-cloudCenter2C[lCloud, 1])**2)
                sigma = cloudWidthC[lCloud]
                magnitude = cloudMagnitudeC[lCloud]
                additionalDistributionM[lXPoint, lYPoint] = \
                    magnitude/(sigma*math.sqrt(2*math.pi)) * \
                    math.exp(-squaredDistance/(2*sigma**2))
                    
        distributionM += additionalDistributionM
        
    if plotDistributionL:
        plot_sample_distribution(distributionM)
        
    return distributionM
    
    
    
def plot_sample_distribution(distributionM):
    plt.imshow(distributionM)
    
    

if __name__ == "__main__":
    main(plotDistributionL = True)