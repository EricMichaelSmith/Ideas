# -*- coding: utf-8 -*-
"""
@author: Eric Smith
Created 2014-03-03

Reads in 2012 US election results, from http://www.theguardian.com/news/datablog/2012/nov/07/us-2012-election-county-results-download#data
"""

import config

import numpy as np
import os
from pandas import Series, DataFrame
import pandas as pd



def main():
  
    # Read in 2012 election data
    filePathS = os.path.join(config.basePathS, "election_statistics",
                             "US_elect_county__2012.csv")
    fullTableDF = pd.read_table(filePathS)                              
                              
    # Remove entries that correspond to the voting records of the entire state
    validRowsLC = fullTableDF.FIPS_Code.astype(bool)
    countyTableDF = fullTableDF[validRowsLC]
    
    # Extract the correct information for each row
    for iRow in range(countyTableDF.shape[0]):
      countyTableDF[iRow].numDemVotes = extract_votes(countyTableDF[iRow], 1)
      countyTableDF[iRow].numGOPVotes = extract_votes(countyTableDF[iRow], 2)
      
    # Extract the important fields for each row: State Postal, FIPS Code, County Name, TOTAL VOTES CAST, numDemVotes, numGOPVotes
    # {{{}}}
    
#    return fullTableM
    return validRowsLC
    
    
    
def extract_votes(oneCountyDF, partyNum):
  if oneCountyDF.Order == partyNum:
    return oneCountyDF.Votes
  else:
    iParty = 0
    while True:
      iParty += 1
      if oneCountyDF["Order_" + str(iParty)] == partyNum:
        return oneCountyDF["Votes_" + str(iParty)]