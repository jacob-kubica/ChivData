'''
Created on Aug 15, 2016

@author: Jacob
'''
#===============================================================================
# Do not write new functions in this module this module should just be
# the initialize method for the program
#===============================================================================
from gui import run
from HCDC import Directory
if __name__ == '__main__':
    HCDC = Directory()
    run(HCDC)