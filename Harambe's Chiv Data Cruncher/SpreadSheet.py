'''
Created on Aug 16, 2016

@author: Jacob
'''
import gspread #Handles google sheet pulls
from oauth2client.service_account import ServiceAccountCredentials #handles google api credentials 
import time #for use in program timing
start_time = time.time()
json = {
  "type": "service_account",
  "project_id": "tutorial-140201",
  "private_key_id": "b786124aec2235cfb1b2aa379cbd668df6d91e6d",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC+haJOt37P50ye\nSVdbagT/SyEwcb5kBNJyIkr7b4Trk1zgWJixwVa2HObmchbAV5ruuL/orrD/EyZp\nhjjF86HB76Z4/opOFvi4A9i2FT4agnTSzVnQfjJhd58gkeWGcgn77v/wM7lOjgPb\n0DhvDv9fEmArGEaTztnP05acRviAUz9nq+xLSlEX9EBmmBxhLua2SNeJOgubEG0M\nw/B/T/XxJf6ixqYJyL7aQ6cDCdOX5/ZEiSlTTlhAJulPzU06flinj9JvvbdIHire\nH+Qxm4AGGCrP2XY/vFtDHuS8bUB5xYA4Loh7OebIqRZKjhHzqCY5r2f8Xak530nc\nIb+ftTwjAgMBAAECggEAWx3wLPNnC6lUJFNxGwAOWcYlnlSXuJ/xwbIS6ENCb6Pv\nhD/67vBHNxuFdmrT5LNBHrBu36pEbglLkqYlms5U6zphBHa/0G7+DouQZiysoeMI\nWhTpwmPIVoLuMJZ2DiGWEs4Py2IBWsdiowrnIn4qtd5E7fdTMbd4xgMsgZsTl9Lj\nvh7xz3niXY7yVKH9K3nqnRW9nF1YA2+rhrLw8UzZJUjImwb26F5I7+mEvwJ8Wtzm\nKOktbxPEcPsCstrQb1x9VgC4obzCqFgy/Qt3BfPM0Qe9uGpqzNf/T1dFlVty2BAf\ncSYEgTDergG/pHU6wrShU6qS08RRZO4IIk5iKuVRCQKBgQD4zZEnYt9rf2yGuGrS\nbVEMIVvMVJyHa0N1rdIltFo5PGtJNefJJjaJ8F/K6qZySyJB3H1dp32wrombUD2R\n5KpXgwRHZD1QFxhgBr9QEIuihZ08OgLOOcVAChpOhoJJ2F75wXH3oNMq7XUDTtqf\nED52soRrdNzLoPSMWrks4X8F9QKBgQDECHw+M+4tb2ts15e5RCuw83S4RRkbVv//\nk46VBd31FAwArP+mBAL5vLHLaZsY25cqPkgrGbOZDHgequhEZ3A0taTIx+DHVSIX\nNyXeYutl/EPkVWTvj97IHRqqJqbzCmmsgbfnqFzq1GVvM/PygDq2hnl3POox4spO\nSptyJtHStwKBgB+paVNtzajMam8qgM2Og8XbaOczzUeeatNK73dE4EZwXebPKVP7\nvO0I3efgvJXG4fEnsfx9GA2n6HMPXwZ15weD8MN1CihrB/sQYMA7mslv33aOm1TL\nHULtBjQAAgyLsGpwJ6Svnq/T0BQ/sKqVUp2gUiGqmX6AWR6TXQVNHPERAoGBAIk8\nR35kbIFyVwpDg/w3NT8TsMqv1PvG1EDf1BmPmetQtXZjpjVa6Zpb9zwoGmQ0locE\nQxGpVIn4qL8PdrssjujXoRzOkRX7C3qlKOWe6pzjFcRr49WyKox9k4U6ufW7fG9A\nALc0rpfXSYuoG0fRbUkKq05GXs29r1NP97LaalnRAoGBALweJiudgSMoHIRAh+AL\nWsOBqfCyyduP8cyg2c3Dg5P55cToxrNU8ldlNeoOrjq3X5pfrS6cpPg8+F/5cL4a\nkKSuIlrUGTE7mO9IiL5ZzTUU7naJ2+xlHjDEIs41psvYQV9jyFCWxLLYwCKUeEJp\nNjOTYv7ACB6vzPOcRY+OSRKx\n-----END PRIVATE KEY-----\n",
  "client_email": "tutorial@tutorial-140201.iam.gserviceaccount.com",
  "client_id": "101034349180373588287",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/tutorial%40tutorial-140201.iam.gserviceaccount.com"
}
class SpreadSheet(object):
    '''
    Contains main spreadsheet object and methods required
    for error handling and data processing
    '''
    def __init__(self, url, ):
        '''
        '''
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(json, scope)
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