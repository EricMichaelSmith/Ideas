# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 12:39:04 2014

@author: Eric Smith

2014-02-16: I suppose I import this other file?
"""



def find_curves_prototype():
    """Run entire prototype of generating a population distribution, fitting curves to it, and plotting the output."""    

initialDistributionM = create_sample_distribution()
#   Create weight matrix from the distribution.
#   For each curve:
#       Find best-fit curve through logistic regression.
#       Calculate contribution of curve to weight matrix.
#       Subtract contribution from weight matrix.
#   Plot sample distribution.
#   Plot curves on top of distribution.
#   On separate figure, plot remainder of weight matrix.