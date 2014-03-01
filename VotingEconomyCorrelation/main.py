# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 07:56:38 2014

@author: Eric Smith

Determines whether a correlation exists between 2008/2012 voting shifts and unemployment shifts

2014-03-01: See http://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html
"""

import numpy as np
import os



def main():
    
    # Demo
    fileNameS = 'laucnty08.txt'
    pathS = r'C:\E\GitHub\Computing\Ideas\VotingEconomyCorrelation\unemployment_statistics'
    tableM = read_unemployment_file(pathS, fileNameS)
    return tableM
  
  ## Load data: FIPS code, state name, county name, shape data, percentage voting for Obama in 2008 and 2012, percentage voting for McCain/Romney in 2008 and 2012, unemployment data per county for 2008, 2009, 2010, 2011, 2012
  
  # Load election data
  # {{{}}}
  
  # Transform all of that data into a usable form
  # {{{}}}
  
  # Calculate 2008/2012 electoral shift; 2008/2009, 2009/2010, 2010/2011, 2011/2012, and 2008/2012 unemployment shifts
  # {{{}}}
  
  # For the electoral shift and each unemployment shift, calculate the R-value, the p-value, and the normalized slope of the correlation
  # {{{}}}
  
  # Depending on the correlations you find, plot the most interesting results on a county map of the US
  # {{{}}}
  
  

def read_unemployment_file(pathS, fileNameS):
    tableM = np.genfromtxt(os.path.join(pathS, fileNameS), skip_header=6, skip_footer=3210)
    # {{{other stuff. Fix fields that didn't import correctly and obviously don't skip so many lines at the end.}}}
    return tableM