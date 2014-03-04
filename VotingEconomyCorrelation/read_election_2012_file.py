# -*- coding: utf-8 -*-
"""
@author: Eric Smith
Created 2014-03-03

Reads in 2012 US election results, from http://www.theguardian.com/news/datablog/2012/nov/07/us-2012-election-county-results-download#data
"""

import config
import numpy as np
import os



def main():
    filePathS = os.path.join(config.basePathS, "election_statistics",
                             "US_elect_county__2012.csv")
                              
    fullTableRA = np.recfromcsv(filePathS,
                              delimiter=',',
                              case_sensitive=True,
                              deletechars='',
                              replace_space='_')
                              
                              
    # Remove entries that correspond to the voting records of the entire state
    validRowsLC = fullTableRA.FIPS_Code.astype(bool)
    
    # {{{get the candidates to be in the right order and create a subtable with only the rows and fields you need}}}
    
#    return fullTableM
    return validRowsLC
    
    
    
def extract_votes(fullTableRA, iRow):
  numDemVotes = run_extract_votes_loop(fullTableRA, iRow, "Dem")
  numGOPVotes = run_extract_votes_loop(fullTableRA, iRow, "GOP")
  
  return (numDemVotes, numGOPVotes)
  
  
  
def run_extract_votes_loop(fullTableRA, iRow, partyS):
  if fullTableRA.Party[iRow] == partyS:
    return fullTableRA.Votes[iRow]
  else:
    iParty = 0
    while True:
      iParty += 1
      if fullTableRA("Party_" + str(iParty)) == partyS:
        return fullTableRA("Votes_" + str(iParty))[iRow]