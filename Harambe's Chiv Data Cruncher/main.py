'''
Created on Aug 15, 2016

@author: Jacob
'''
from gui import GUI
from HCDC import Directory

if __name__ == '__main__':
    HCDC = Directory()
    gui = GUI()
    print("--- %s seconds ---" % (time.time() - start_time))