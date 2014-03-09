# -*- coding: utf-8 -*-
"""
Created on Sun Mar 09 13:34:28 2014

@author: Eric
"""

import os
import pandas as pd

import config



def main(fileNameS):
    pathS = os.path.join(config.basePathS, "unemployment_statistics")
    conversionD = {'state_fips_code': (lambda x: str(x)),
                   'county_fips_code': (lambda x: str(x)),
                   'year': (lambda x: int(x)),
                   'labor_force': (lambda x: int(str(x).translate(None, ','))),
                   'employed': (lambda x: int(str(x).translate(None, ','))),
                   'unemployed_level': (lambda x: int(str(x).translate(None, ',')))}
    tableDF = pd.read_fwf(os.path.join(pathS, fileNameS),
                          converters=conversionD,                          
                          names=["laus_code", "state_fips_code",
                                 "county_fips_code", "county_and_state",
                                 "year", "labor_force", "employed",
                                 "unemployed_level", "unemployed_rate"],
                          skipfooter=3,
                          skiprows=6,
                          widths=[18, 7, 6, 50, 4, 14, 13, 11, 9])
    tableDF.fips_code = tableDF.state_fips_code + tableDF.county_fips_code
                                   
    return tableDF