# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 12:39:04 2014

@author: Eric Smith

Run the entire prototype of generating a population distribution, fitting curves to it, and plotting the output.
"""

import calculate_curve_weighting, create_sample_distribution, find_best_fit_curve



def main():
  
  # Parameters
  numCurves = 2  
  
  # Create the sample distribution.
  distributionM = create_sample_distribution.main()
  
  # Create weight matrix from the distribution.
  # [[[So, right now I'm going to use the distribution itself as the weight matrix. I'll think about what this means later.]]]
  
  for lCurve in range(numCurves):
    
    # Find the best-fit curve through logistic regression.
    curvePoints2C = find_best_fit_curve.main(distributionM)
    
    # Calculate contribution of curve to weight matrix.
    weightContributionM = calculate_curve_weighting.main(curvePoints2C, distributionM.shape)
    
    # Subtract contribution from weight matrix.
    distributionM -= weightContributionM
    # {{{make sure that distributionM is never less than zero}}}
  
  # Plot sample distribution.
  # {{{}}}
    
  # Plot curves on top of distribution.
  # {{{}}}
    
  # On separate figure, plot remainder of weight matrix.
  # {{{}}}
  
  # [[[Obviously this is temporary]]]
  return distributionM