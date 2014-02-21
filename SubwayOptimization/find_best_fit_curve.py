# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 08:20:20 2014

@author: Eric

Uses regression to find the curve that best describes the input distribution.

Concerns:
- Will a simple polyfit allow for shapes that pass the vertical line test? If not we're biasing one dimension over the other
- Should I use splines instead? That's what the polyfit documentation recommends for when polyfits aren't satisfactory
"""

import numpy as np



def main(distributionM):
  
  # Smooth the distribution
  smoothedDistributionM = smooth_image(distributionM)
  
  # {{{have flag to plot smoothed image}}}
  
  # {{{find curve(s) through image}}}
  
  return curvePoints2C
  


def smooth_image(distributionM, ShapeParam = 1):
  """Algorithm from A. Ardeshir Goshtasby, http://cecs.wright.edu/~agoshtas/stmalo.pdf"""
  
  ShapeT = distributionM.shape
  smoothedDistributionM = np.zeros(ShapeT)
  smoothedDistributionM.fill(np.nan)
  
  # Loop over every pixel
  for lSmoothedColumn in range(ShapeT[0]):
    for lSmoothedRow in range(ShapeT[1]):
      weightedDistanceM = np.zeros(ShapeT)
      for lOrigColumn in range(ShapeT[0]):
        for lOrigRow in range(ShapeT[1]):
          weightedDistanceM[lOrigColumn, lOrigRow] = \
            distributionM[lOrigColumn, lOrigRow] * \
            ((lOrigColumn-lSmoothedColumn)**2 + (lOrigRow-lSmoothedRow)**2 + \
            ShapeParam**2) ** (-1/2)
      smoothedDistributionM = np.sum(np.sum(weightedDistanceM))
            
  return smoothedDistributionM