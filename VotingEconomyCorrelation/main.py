# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 07:56:38 2014

@author: Eric Smith

Determines whether a correlation exists between 2008/2012 voting shifts and unemployment shifts


2014-03-21:

Okay, figure out how to do the merges properly... read up on how merges work. Perhaps you're using the wrong kind.

FIPS codes in 2008 but not in 2012: set([53000, 42000, 55000, 23000, 18000, 39000, 17000, 27000, 26000, 15005, 36000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040])

FIPS codes in 2012 but not in 2008: set([2000])
"""

import pandas as pd

import election2008
reload(election2008)
import election2012
reload(election2012)
import unemployment
reload(unemployment)



def main():
    
    # Reading in the unemployment files
    fileNameS_L = ["laucnty08.txt", "laucnty09.txt", "laucnty10.txt", "laucnty11.txt",
                  "laucnty12.txt"]
    yearL = range(2008, 2013)
    unemploymentDF_L = list()
    for fileNameS, year in zip(fileNameS_L, yearL):
      unemploymentDF_L.append(unemployment.main(fileNameS, year))
      
    # Reading in the 2008 election file
    election2008_DF = election2008.main()
    
    # Reading in the 2012 election file
    election2012_DF = election2012.main()
    
    # [[[Test: plotting a map of counties]]]
#    election2008.plot_county_results
    
    # Merging DataFrames
    fullDF = pd.merge(election2008_DF, election2012_DF, on='FIPS', how='outer')
    for unemploymentDF in unemploymentDF_L:
        fullDF = pd.merge(fullDF, unemploymentDF, on='FIPS', how='outer')
     
  # Transform all of that data into a usable form
  # {{{}}}
  
  # Calculate 2008/2012 electoral shift; 2008/2009, 2009/2010, 2010/2011, 2011/2012, and 2008/2012 unemployment shifts
  # {{{}}}
  
  # For the electoral shift and each unemployment shift, calculate the R-value, the p-value, and the normalized slope of the correlation
  # {{{}}}
  
  # Depending on the correlations you find, plot the most interesting results on a county map of the US
  # {{{}}}
  
    # [[[obviously temporary]]]
#    return (unemploymentDF_L, election2012_DF)
    return (fullDF, unemploymentDF_L, election2008_DF, election2012_DF)