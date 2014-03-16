# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 07:56:38 2014

@author: Eric Smith

Determines whether a correlation exists between 2008/2012 voting shifts and unemployment shifts


2014-03-16: 

In election_2008.plot_county_results, read in the DataFrame from main, create a boolean value of whether Dem > Rep, and then color the counties using that
"""

import election_2008
reload(election_2008)
import election_2012
reload(election_2012)
import unemployment
reload(unemployment)



def main():
    
    # Reading in the unemployment files
    fileNameS_T = ("laucnty08.txt", "laucnty09.txt", "laucnty10.txt", "laucnty11.txt",
                  "laucnty12.txt")
    unemploymentDF_L = list()
    for fileNameS in fileNameS_T:
      unemploymentDF_L.append(unemployment.main(fileNameS))
      
    # Reading in the 2008 election file
    election2008_DF = election_2008.main()
    
    # Reading in the 2012 election file
    election2012_DF = election_2012.main()
    
    # [[[Test: plotting a map of counties]]]
    election_2008.plot_county_results
  
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
#    return (unemploymentDF_L, election2012_DF)
    return (unemploymentDF_L, election2008_DF, election2012_DF)