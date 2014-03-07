# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 07:56:38 2014

@author: Eric Smith

Determines whether a correlation exists between 2008/2012 voting shifts and unemployment shifts

2014-03-07: Pass the correct column names to pd.read_table
"""

import numpy as np
import os
import pandas as pd

import config
import read_election_2012_file



def main():
    
    # Demo: reading in one of the unemployment files
    fileNameS_T = ('laucnty08.txt', 'laucnty09.txt', 'laucnty10.txt', 'laucnty11.txt',
                  'laucnty12.txt')
    unemploymentDF_T = list()
    for fileNameS in fileNameS_T:
      unemploymentDF_T.append(read_unemployment_file(fileNameS))
    
    # Demo: reading in the 2012 election file
    election2012_DF = read_election_2012_file.main()
  
  ## Load data: FIPS code, state name, county name, shape data, percentage voting for Obama in 2008 and 2012, percentage voting for McCain/Romney in 2008 and 2012, unemployment data per county for 2008, 2009, 2010, 2011, 2012
  
  # Load election data
  # {{{see https://code.google.com/p/pyshp/ and https://pypi.python.org/pypi/pyshp#id2 for working with shapefiles}}}
  
  # Transform all of that data into a usable form
  # {{{}}}
  
  # Calculate 2008/2012 electoral shift; 2008/2009, 2009/2010, 2010/2011, 2011/2012, and 2008/2012 unemployment shifts
  # {{{}}}
  
  # For the electoral shift and each unemployment shift, calculate the R-value, the p-value, and the normalized slope of the correlation
  # {{{}}}
  
  # Depending on the correlations you find, plot the most interesting results on a county map of the US
  # {{{}}}
  
    # [[[obviously temporary]]]
    return (unemploymentDF_T, election2012_DF)



def read_unemployment_file(fileNameS):
    pathS = os.path.join(config.basePathS, "unemployment_statistics")
    tableDF = pd.read_table(os.path.join(pathS, fileNameS))
#    tableM = np.genfromtxt(os.path.join(pathS, fileNameS),
#                           delimiter=[18, 7, 6, 50, 4, 14, 13, 11, 9], 
#                           dtype=[('laus_code', 'S15'),
#                                  ('state_fips_code', '<i4'),
#                                  ('county_fips_code', '<i4'),
#                                  ('county_and_state', 'S50'),
#                                  ('year', '<i4'), 
#                                  ('labor_force', 'S14'),
#                                  ('employed', 'S13'), 
#                                  ('unemployed_level', 'S11'), 
#                                  ('unemployed_rate', '<f8')], 
#                           skip_header=6,
#                           skip_footer=2)

    # Combine FIPS codes
    numRows = tableDF.state_fips_code.shape[0]
    tableDF["fips_code"] = np.empty(numRows)
    for lRow in range(numRows):
      tableDF.fips_code[lRow] = int(str(tableDF.state_fips_code[lRow]) +
                                   str(tableDF.county_fips_code[lRow]))
                                   
    return tableDF