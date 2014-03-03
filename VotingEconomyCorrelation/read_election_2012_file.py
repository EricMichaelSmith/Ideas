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
                              
#    fullTableM = np.genfromtxt(filePathS,
#                           delimiter=',',
#                           dtype=None,
#                           skip_header=1)
                              
    # Remove entries that correspond to the voting records of the entire state
    validRowsLC = fullTableRA.FIPS_Code.astype(bool)
    
    # {{{get the candidates to be in the right order}}}
#    return fullTableM
    return validRowsLC