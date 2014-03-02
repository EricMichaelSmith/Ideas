# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 07:56:38 2014

@author: Eric Smith

Determines whether a correlation exists between 2008/2012 voting shifts and unemployment shifts

2014-03-01: Figure out how to delete a particular row from every record in an np.recarray
"""

import config
import numpy as np
import os



def main():
    
    # Demo: reading in one of the unemployment files
    fileNameS = 'laucnty08.txt'
    unemployment08_M = read_unemployment_file(fileNameS)
    
    # Demo: reading in the 2012 election file
    election12_M = read_election_2012_file()
  
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
  
    # [[[obviously temporary]]]
    return (unemployment08_M, election12_M)
  
  
  
def read_election_2012_file():
    filePathS = os.path.join(config.basePathS, "election_statistics",
                             "US_elect_county__2012.csv")
    fullTableM = np.genfromtxt(filePathS,
                           delimiter=',',
                           dtype=None,
                           skip_header=1)
    fipsIndex = 3
    
    # Remove entries that correspond to the voting records of the entire state
    validFipsLC = fullTableM[:, fipsIndex].astype(bool)
#    fullTableM = fullTableM[validFipsLC][:]
    
    # {{{get the candidates to be in the right order}}}
#    return fullTableM
    return validFipsLC
  

def read_unemployment_file(fileNameS):
    pathS = os.path.join(config.basePathS, "unemployment_statistics")
    tableM = np.genfromtxt(os.path.join(pathS, fileNameS),
                           delimiter=[18, 7, 6, 50, 4, 14, 13, 11, 9], 
                           dtype=[('laus_code', 'S15'),
                                  ('state_fips_code', '<i4'),
                                  ('county_fips_code', '<i4'),
                                  ('county_and_state', 'S50'),
                                  ('year', '<i4'), 
                                  ('labor_force', 'S14'),
                                  ('employed', 'S13'), 
                                  ('unemployed_level', 'S11'), 
                                  ('unemployed_rate', '<f8')], 
                           skip_header=6,
                           skip_footer=2)
    tableM = tableM.view(np.recarray)
    return tableM