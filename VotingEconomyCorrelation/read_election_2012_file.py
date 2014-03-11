# -*- coding: utf-8 -*-
"""
@author: Eric Smith
Created 2014-03-03

Reads in 2012 US election results, from http://www.theguardian.com/news/datablog/2012/nov/07/us-2012-election-county-results-download#data
"""

import os
import pandas as pd

import config



def main():
  
    # Read in 2012 election data
    filePathS = os.path.join(config.basePathS, "election_statistics",
                             "US_elect_county__2012.csv")
    fullTableDF = pd.read_csv(filePathS,
                              low_memory=False)
    
    # Remove entries that correspond to the voting records of the entire state
    validRowsLC = fullTableDF["FIPS Code"].astype(bool)
    countyTableDF = fullTableDF[validRowsLC]
    
    # Extract the correct information for each row
    for iRow in range(countyTableDF.shape[0]):
      print iRow
      if iRow == 3160:
        print countyTableDF.iloc[iRow]
      countyTableDF.iloc[iRow].numDemVotes = extract_votes(countyTableDF.iloc[iRow], "Dem")
      countyTableDF.iloc[iRow].numGOPVotes = extract_votes(countyTableDF.iloc[iRow], "GOP")
      
    # Extract the important fields for each row: State Postal, FIPS Code, County Name, TOTAL VOTES CAST, numDemVotes, numGOPVotes
    desiredColumnsL = ["State Postal", "FIPS Code", "County Name", "TOTAL VOTES CAST",
                       "numDemVotes", "numGOPVotes"]
    finalTableDF = countyTableDF.reindex(columns=desiredColumnsL)
    
    return finalTableDF
    
    
    
def extract_votes(oneCountyDF, partyS):
  if oneCountyDF.Party == partyS:
    return oneCountyDF.Votes
  else:
    iParty = 0
    while True:
      iParty += 1
      if oneCountyDF["Party." + str(iParty)] == partyS:
        return oneCountyDF["Votes." + str(iParty)]