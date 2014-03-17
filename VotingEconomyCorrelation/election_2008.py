# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 08:41:32 2014

@author: Eric

Reads in 2008 county election data (2008 Presidential General Election, County Results, National Atlas of the United States, http://nationalatlas.gov/atlasftp.html?openChapters=chphist#chphist)
"""

from matplotlib.collections import PatchCollection
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import shapefile
import sys

import config

sys.path.append(config.GeoDaSandboxPathS)
from pyGDsandbox.dataIO import dbf2df


def main():
    """
    Read in the election data shapefile as a DataFrame
    """
    
    filePathS = os.path.join(config.basePathS, "election_statistics", "2008",
                             "elpo08p020.dbf")
    fullDF = dbf2df(filePathS)
    
    return fullDF
    
    

def plot_county_results():
    """
    Reads in the shapefile and plots a full map of all counties, colored red or blue according to vote totals
    
    See http://stackoverflow.com/questions/15968762/shapefile-and-matplotlib-plot-polygon-collection-of-shapefile-coordinates for how to quickly plot shapes from a shapefile
    """
    
    # Read in shapedata    
    filePathS = os.path.join(config.basePathS, "election_statistics", "2008",
                             "elpo08p020")
    fullSF = shapefile.Reader(filePathS)
    shapeL = fullSF.shapes()
    numShapes = len(shapeL)
    
    # Read in election data
    fullDF = main()
    fullDF.loc[:, 'DemIsHigher'] = (fullDF.loc[:, u'VOTE_DEM'] > fullDF.loc[:, u'VOTE_REP'])
    # {{{probably read in the records of fullSF? or somehow locate the fips codes such that for every lShape below, you can look up the fips code and use that to determine whether, from fullDF.DemIsHigher, the shape should be blue or red}}}    

    # Plot figure
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    shapeBoundsA = np.empty((numShapes, 4))
    shapeBoundsA[:] = np.nan
    for lShape in range(numShapes):
        shapeBoundsA[lShape, :] = shapeL[lShape].bbox

        thisShapesPatches = []
        pointsA = np.array(shapeL[lShape].points)
        shapeFileParts = shapeL[lShape].parts
        allPartsL = list(shapeFileParts) + [pointsA.shape[0]]
        for lPart in range(len(shapeFileParts)):
            thisShapesPatches.append(patches.Polygon(
                pointsA[allPartsL[lPart]:allPartsL[lPart+1]]))
        
        ax.add_collection(PatchCollection(thisShapesPatches,
                                          facecolor=(0, 0, 1)))
    
    shapeBoundsR = np.empty(4)
    shapeBoundsR[0] = np.amin(shapeBoundsA[:, 0], 0)
    shapeBoundsR[1] = np.amin(shapeBoundsA[:, 1], 0)
    shapeBoundsR[2] = np.amax(shapeBoundsA[:, 2], 0)
    shapeBoundsR[3] = np.amax(shapeBoundsA[:, 3], 0)    
    ax.set_xlim(shapeBoundsR[0], shapeBoundsR[2])
    ax.set_ylim(shapeBoundsR[1], shapeBoundsR[3])