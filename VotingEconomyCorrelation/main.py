# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 07:56:38 2014

@author: Eric Smith

Determines whether a correlation exists between 2008/2012 voting shifts and unemployment shifts


2014-03-20:

Figure out how to find the counties corresponding to the FIPS codes in one but not the other. Look in http://pandas.pydata.org/pandas-docs/stable/merging.html for documentation on merges.

FIPS codes in 2008 but not in 2012: set([53000, 42000, 55000, 23000, 18000, 39000, 17000, 27000, 26000, 15005, 36000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040])

FIPS codes in 2012 but not in 2008: set([2000])
"""

import election2008
reload(election2008)
import election2012
reload(election2012)
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
    election2008_DF = election2008.main()
    
    # Reading in the 2012 election file
    election2012_DF = election2012.main()
    
    # [[[Test: plotting a map of counties]]]
#    election2008.plot_county_results
    
    # [[[finding which elements are in election2008 but not in election2012 and vice versa]]]
    
  
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