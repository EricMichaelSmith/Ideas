# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 08:20:20 2014

@author: Eric

Uses regression to find the curve that best describes the input distribution.

Concerns:
- Will a simple polyfit allow for shapes that pass the vertical line test? If not we're biasing one dimension over the other
- Should I use splines instead? That's what the polyfit documentation recommends for when polyfits aren't satisfactory
"""

import numpy as np


def main(distributionM):
  
  return curvePoints2C