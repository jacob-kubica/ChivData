'''
Created on Aug 16, 2016

@author: Jacob
'''
import gspread #Handles google sheet pulls
from oauth2client.service_account import ServiceAccountCredentials #handles google api credentials 
import time #for use in program timing
start_time = time.time()

class SpreadSheet(object):
    '''
    Contains main spreadsheet object and methods required
    for error handling and data processing
    '''
    def __init__(self, url, ):
        '''
        '''
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('Other Files/tutorial-b786124aec22.json', scope)
        gc = gspread.authorize(credentials)
        self.wks = gc.open_by_url(url)
        self.worksheet = self.wks.get_worksheet(0)
         
    def getCellValue(self, cellValue):
        '''
        get cell value based on alpha numerical cell position
        '''
        return self.worksheetDir[cellValue]
    
    def columnValues(self, column):
        '''
        gets all values from column
        this should be changed to pull from worksheetDir not google drive
        '''
        return self.worksheet.col_values(column)
    def rowValues(self, row):
        '''
        gets all values from row
        this should be changed to pull from worksheetDir not google drive
        '''
        return self.allvalues[row]

    def worksheetDirBuild(self, orientation):
        '''
        Builds a worksheet directory
        '''
        #used to create cell keys
        alphanumassignment = {
                              "0":"A",
                              "1":"B",
                              "2":"C",
                              "3":"D",
                              "4":"E",
                              "5":"F",
                              "6":"G",
                              "7":"H",
                              "8":"I",
                              "9":"J",
                              "10":"K"
                            }
        #generates or clears the worksheetDir
        self.worksheetDir = {}
        #List of lists of all cell values
        self.allvalues = self.worksheet.get_all_values()
        for (y, row) in enumerate(self.allvalues):
            for (x, column) in enumerate(row):
                #realigns spreadsheet so that primary iterator is numbers not letters
                if orientation == 0:
                    self.worksheetDir[alphanumassignment[str(y)] + str(x + 1)] = column
                if orientation == 1:
                    self.worksheetDir[alphanumassignment[str(x)] + str(y + 1)] = column