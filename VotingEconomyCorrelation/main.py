# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 07:56:38 2014

@author: Eric Smith

Determines whether a correlation exists between 2008/2012 voting shifts and unemployment shifts

2014-03-27: Play around with more sophisticated color maps and plotting other things: obviously, whether counties with more employment have less of a rightward shift in 2012! Maybe also plot state borders.
"""

from matplotlib.collections import PatchCollection
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
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
    (election2008_DF, shapeIndexL, shapeL) = election2008.main()
    
    # Reading in the 2012 election file
    election2012_DF = election2012.main()

    # Reading in the unemployment files
    fileNameS_L = ["laucnty08.txt", "laucnty09.txt", "laucnty10.txt", "laucnty11.txt",
                  "laucnty12.txt"]
    yearL = range(2008, 2013)
    unemploymentDF_L = list()
    for fileNameS, year in zip(fileNameS_L, yearL):
      unemploymentDF_L.append(unemployment.main(fileNameS, year))
    
    # Merging DataFrames
    fullDF = fipsDF.join(election2008_DF, how='inner')
    fullDF = fullDF.join(election2012_DF, how='inner')
    for unemploymentDF in unemploymentDF_L:
        fullDF = fullDF.join(unemploymentDF, how='inner')
    
    # [[[save to csv file]]]
    fullDF.to_csv(os.path.join(config.basePathS, 'fullDF.csv'))
    
    # [[[testing plotting]]]
    fullDF.loc[:, 'DemIsHigher2008'] = (fullDF.loc[:, 'Election2008Dem'] >
                                        fullDF.loc[:, 'Election2008Rep'])
    fullDF.to_csv(os.path.join(config.basePathS, 'fullDFWithBool.csv'))
    # [[[probably delete this?]]]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    shapeBoundsAllShapesL = [float('inf'), float('inf'), float('-inf'), float('-inf')]
    for lFIPS in fullDF.index:
        if fullDF.loc[lFIPS, 'DemIsHigher2008']:
            shapeColorT = (0, 0, 1)
        else:
            shapeColorT = (1, 0, 0)
        
        iShapeL = [i for i,j in enumerate(shapeIndexL) if j==lFIPS]
        for iShape in iShapeL:            
            shapeBoundsThisShapeL = shapeL[iShape].bbox
            shapeBoundsAllShapesL[0] = \
                min(shapeBoundsThisShapeL[0], shapeBoundsAllShapesL[0])
            shapeBoundsAllShapesL[1] = \
                min(shapeBoundsThisShapeL[1], shapeBoundsAllShapesL[1])
            shapeBoundsAllShapesL[2] = \
                max(shapeBoundsThisShapeL[2], shapeBoundsAllShapesL[2])
            shapeBoundsAllShapesL[3] = \
                max(shapeBoundsThisShapeL[3], shapeBoundsAllShapesL[3])
            
            thisShapesPatches = []
            pointsA = np.array(shapeL[iShape].points)
            shapeFileParts = shapeL[iShape].parts
            allPartsL = list(shapeFileParts) + [pointsA.shape[0]]
            for lPart in xrange(len(shapeFileParts)):
                thisShapesPatches.append(patches.Polygon(
                    pointsA[allPartsL[lPart]:allPartsL[lPart+1]]))
            ax.add_collection(PatchCollection(thisShapesPatches,
                                              color=shapeColorT))
    ax.set_xlim(shapeBoundsAllShapesL[0], shapeBoundsAllShapesL[2])
    ax.set_ylim(shapeBoundsAllShapesL[1], shapeBoundsAllShapesL[3])
    
  # Transform all of that data into a usable form
  # {{{}}}
  
  # Calculate 2008/2012 electoral shift; 2008/2009, 2009/2010, 2010/2011, 2011/2012, and 2008/2012 unemployment shifts
  # {{{}}}
  
  # For the electoral shift and each unemployment shift, calculate the R-value, the p-value, and the normalized slope of the correlation
  # {{{}}}
  
  # Depending on the correlations you find, plot the most interesting results on a county map of the US
  # {{{}}}
  
    return fullDF