# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 07:42:36 2014

@author: Eric

Reloads all files in the current working directory.

2014-02-18: reload() won't work because it needs a module as an argument, not a string, and __import__ won't work because, well, when I try to load a module using it, the module doesn't seem to be recognized afterward.
"""

import os

def main():
  CWD_S = os.getcwd()
  fileSL = os.listdir(CWD_S)
  
  for fileS in fileSL:
    try:
      reload(fileS)
    except ImportError:
      __import__(fileS)
  

  
if __name__ == "__main__":
  main()