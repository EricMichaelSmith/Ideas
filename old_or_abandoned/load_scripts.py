# -*- coding: utf-8 -*-
"""
Created on Mon Mar 03 08:34:46 2014

@author: Eric
"""

import os



def main():
  """
  Imports or reloads all scripts in the current directory
  """
  fileNameL = [fileS for fileS in os.listdir('.') if os.path.isfile(fileS)]
  for nameS in fileNameL:
    if nameS.endswith(".py") and nameS != "main.py":
      exec("import " + nameS)
      exec("reload(" + nameS + ")")