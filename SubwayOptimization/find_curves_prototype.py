# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 12:39:04 2014

@author: Eric Smith

Run the entire prototype of generating a population distribution, fitting curves to it, and plotting the output.

2014-02-17: See http://pyunit.sourceforge.net/notes/reloading.html for how to load and reload imported modules automatically. Or maybe just dump everything into the same script for now.
"""

import create_sample_distribution



def main():
  
  initialDistributionM = create_sample_distribution.main()
#   Create weight matrix from the distribution.
#   For each curve:
#       Find best-fit curve through logistic regression.
#       Calculate contribution of curve to weight matrix.
#       Subtract contribution from weight matrix.
#   Plot sample distribution.
#   Plot curves on top of distribution.
#   On separate figure, plot remainder of weight matrix.