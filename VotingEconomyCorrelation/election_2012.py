# -*- coding: utf-8 -*-
"""
@author: Eric Smith
Created 2014-03-03

Reads in 2012 US election results, from http://www.theguardian.com/news/datablog/2012/nov/07/us-2012-election-county-results-download#data
"""

import numpy as np
import os
import pandas as pd

import config



def main():
  
    # Read in 2012 election data
    filePathS = os.path.join(config.basePathS, "election_statistics",
                             "US_elect_county__2012.csv")
    fullDF = pd.read_csv(filePathS,
                              low_memory=False)
    
    # Remove entries that correspond to the voting records of the entire state
    validRowsLC = fullDF["FIPS Code"].astype(bool)
    countyDF = fullDF[validRowsLC]
    
    # Extract the correct information for each row
    countyDF.loc[:, "numDemVotes"] = np.nan
    countyDF.loc[:, "numGOPVotes"] = np.nan
    for iRow in countyDF.index:
      countyDF.loc[iRow, "numDemVotes"] = extract_votes(countyDF.loc[iRow], "Dem")
      countyDF.loc[iRow, "numGOPVotes"] = extract_votes(countyDF.loc[iRow], "GOP")
      
    # Extract the important fields for each row: State Postal, FIPS Code, County Name, TOTAL VOTES CAST, numDemVotes, numGOPVotes
    desiredColumnsL = ["State Postal", "FIPS Code", "County Name", "TOTAL VOTES CAST",
                       "numDemVotes", "numGOPVotes"]
    finalDF = countyDF.reindex(columns=desiredColumnsL)
    
    return finalDF
    
    
    
def extract_votes(oneCountyDF, partyS):
  if oneCountyDF.Party == partyS:
    return oneCountyDF.Votes
  else:
    iParty = 0
    while True:
      iParty += 1
      if oneCountyDF["Party." + str(iParty)] == partyS:
        return oneCountyDF["Votes." + str(iParty)]