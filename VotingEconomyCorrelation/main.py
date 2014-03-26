# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 07:56:38 2014

@author: Eric Smith

Determines whether a correlation exists between 2008/2012 voting shifts and unemployment shifts

2014-03-25: Think about whether you really want to include shapefiles in the same DataFrame as your stats: another way to do it would be to bind FIPS codes to shapefiles in a separate DataFrame in election2008() and then just read all matching shapes for a given FIPS code every time you want to plot. Assign color values to the DataFrame properly and finish the test of plotting election 2008 data from fullDF. Once that's done, see which counties aren't being plotted and take care of all of the idiosyncrasies in the data: missing values, misaligned counties, etc. Probably just delete all of the Alaska data. Do you want to eventually change all of the inner joins back to outer joins, or will it not matter in the end?
"""

from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import numpy as np
import os
import pdb

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
#    fullDF = fipsDF.join(election2008_DF, how='outer')
#    fullDF = fullDF.join(election2012_DF, how='outer')
#    for unemploymentDF in unemploymentDF_L:
#        fullDF = fullDF.join(unemploymentDF, how='outer')
    fullDF = fipsDF.join(election2008_DF, how='inner')
    fullDF = fullDF.join(election2012_DF, how='inner')
    for unemploymentDF in unemploymentDF_L:
        fullDF = fullDF.join(unemploymentDF, how='inner')
    
    # [[[save to csv file]]]
    fullDF.to_csv(os.path.join(config.basePathS, 'fullDF.csv'))
    
    # [[[testing plotting]]]
#    colorDF = pd.DataFrame(np.empty((fullDF.shape[0], 3)),
#                           columns=['Red','Green','Blue'],
#                           index=fullDF.index)
#    fullDF = pd.concat([fullDF, colorDF], axis=1)
    fullDF.loc[:, 'DemIsHigher2008'] = (fullDF.loc[:, 'Election2008Dem'] >
                                        fullDF.loc[:, 'Election2008Rep'])
    fullDF.to_csv(os.path.join(config.basePathS, 'fullDFWithBool.csv'))
#    fullDF.loc[fullDF.loc[:, 'DemIsHigher2008'], ['Red','Green','Blue']] = \
#        [(0, 0, 1)] * np.sum(fullDF.loc[:, 'DemIsHigher2008'])
#    fullDF.loc[~fullDF.loc[:, 'DemIsHigher2008'], ['Red', 'Green', 'Blue']] = \
#        [(1, 0, 0)] * np.sum(~fullDF.loc[:, 'DemIsHigher2008'])
#    fullDF.to_csv(os.path.join(config.basePathS, 'fullDFWithColors.csv'))
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    for lFIPS in fullDF.index:
        print(lFIPS)
        print(fullDF.loc[lFIPS, 'DemIsHigher2008'])
        pdb.set_trace()
        if fullDF.loc[lFIPS, 'DemIsHigher2008']:
            shapeColorT = (0, 0, 1)
        else:
            shapeColorT = (1, 0, 0)      
        ax.add_collection(PatchCollection(fullDF.loc[lFIPS, 'ShapePatches'],
                                          color=shapeColorT))
        ax.set_xlim(np.amin(fullDF.ShapeXMin), np.amax(fullDF.ShapeXMax))
        ax.set_ylim(np.amin(fullDF.ShapeYMin), np.amax(fullDF.ShapeYMax))
    
  # Transform all of that data into a usable form
  # {{{}}}
  
  # Calculate 2008/2012 electoral shift; 2008/2009, 2009/2010, 2010/2011, 2011/2012, and 2008/2012 unemployment shifts
  # {{{}}}
  
  # For the electoral shift and each unemployment shift, calculate the R-value, the p-value, and the normalized slope of the correlation
  # {{{}}}
  
  # Depending on the correlations you find, plot the most interesting results on a county map of the US
  # {{{}}}
  
    return fullDF