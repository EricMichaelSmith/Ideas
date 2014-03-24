# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 07:56:38 2014

@author: Eric Smith

Determines whether a correlation exists between 2008/2012 voting shifts and unemployment shifts

2014-03-23: Take care of all of the idiosyncrasies in the data: missing values, misaligned counties, etc. Probably just delete all of the Alaska data.
"""

import os

import config
reload(config)
import fips
reload(fips)
import election2008
reload(election2008)
import election2012
reload(election2012)
import unemployment
reload(unemployment)



def main():
    
    # Reading in county and state names
    fipsDF = fips.main()
    
    # Reading in the 2008 election file
    election2008_DF = election2008.main()
    
    # Reading in the 2012 election file
    election2012_DF = election2012.main()

    # Reading in the unemployment files
    fileNameS_L = ["laucnty08.txt", "laucnty09.txt", "laucnty10.txt", "laucnty11.txt",
                  "laucnty12.txt"]
    yearL = range(2008, 2013)
    unemploymentDF_L = list()
    for fileNameS, year in zip(fileNameS_L, yearL):
      unemploymentDF_L.append(unemployment.main(fileNameS, year))    
    
    # [[[Test: plotting a map of counties]]]
#    election2008.plot_county_results
    
    # Merging DataFrames
    fullDF = fipsDF.join(election2008_DF, how='outer')
    fullDF = fullDF.join(election2012_DF, how='outer')
    for unemploymentDF in unemploymentDF_L:
        fullDF = fullDF.join(unemploymentDF, how='outer')
    
    # [[[save to csv file]]]
    fullDF.to_csv(os.path.join(config.basePathS, 'mergedDF.csv'))
    
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