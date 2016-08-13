'''
Created on Aug 12, 2016

@author: Jacob
'''
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys
from _ast import Pass

class Player(object):
    '''
    Player Object which contains info specific to the player
    and methods to update and calculate player specific values
    '''
    def __init__(self, name):
        '''
        Sets Attributes
        '''
        #Static Values
        self.playerName = name

        #Dynamic Values
        #MultiMatchValues
        self.killsTotal = 0
        self.deathsTotal = 0
        self.assistsTotal = 0
        self.kDRatioTotal = 0
    def updateValues(self, kills, deaths, assists):
        '''
        Updates values after match completion
        '''
        self.killsTotal = self.killsTotal + newValue
        self.deathsTotal = self.deathsTotal + newValue
        self.assistsTotal = self.assistsTotal + newValue
        self.kDRatioTotal = self.kills/self.deaths
class Team(object):
    '''
    Team Object which contains info specific to the team
    and methods to update and calculate team specific values
    also handles playerRooster a dictionary containing
    all player objects
    '''
    def __init__(self, teamName):
        '''
        Set Attributes
        '''
        #Static Values
        self.teamName = teamName
        self.playerList = []
        self.playerRooster = {}
        #Dynamic Values
        self.teamWinsTotal = 0
        self.teamLossTotal = 0
    def teamWin(self):
        '''
        Handles Case were team wins
        '''
        self.teamWinsTotal += 1
    def teamLoss(self):
        '''
        Handles Case were team loses
        '''
        self.teamLossTotal += 1
    def playerRoosterCreation(self):
        '''
        Creates a playerRooster specific to the team
        '''
        for player in self.playerList:
            x = Player(player)
            self.playerRooster[player] = x
class ChivData():
    '''
    Main program object most likely subject to further separation
    but currently will hold 
        importing from spreadsheet
        the initialization of teams, players, matches
        distributing the data from matches to required destinations
    '''
    def __init__(self):
        '''
        Constructor
        '''
        #Values pertaining to Matches
        self.matchNumber = 1
        self.matchHalfNumber = 1
        
        self.matchRooster = {}
        self.matchList = []
        self.matchWrs = SpreadSheet("https://docs.google.com/spreadsheets/d/1ia8PwjHRf4newhe7Gl5DEvMCjVFs0VswXSkH57lYT78/edit#gid=0")
        
        #Values pertaining to Teams 
        self.teamRooster = {}
        self.teamList = []
        self.teamWrs = SpreadSheet("https://docs.google.com/spreadsheets/d/1T6KWtWPa4UMvquZ_yuiaRN0PJBytHle7F8a4u3pzKtk/edit#gid=0")

        self.Main()
    def Main(self):
        '''
        Main sequence that while start everything else
        '''
        self.inputTeamWrs()
    def inputTeamWrs(self):
        '''
        Gather team names
        '''
        col = self.teamWrs.columnValues(1)
        for x in range(1, len(col)):
            self.teamList.append(col[x])
        
        counter = 1
        for (i, team) in enumerate(self.teamList):
            print(team)
            counter += 1
            print(counter)
            print(i)
            self.teamRooster[team] = Team(team)
            playerList = self.teamWrs.rowValues(i + 2)
            for x in range(1,len(playerList)):
                if playerList[x] == '':
                    break
                else:
                    self.teamRooster[team].playerList.append(playerList[x])
            self.teamRooster[team].playerRoosterCreation()

class SpreadSheet(object):
    '''
    Contains main spreadsheet object and methods required
    for error handling and data processing
    '''
    def __init__(self, url):
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('tutorial-b786124aec22.json', scope)
        gc = gspread.authorize(credentials)
        self.wks = gc.open_by_url(url)
        self.worksheet = self.wks.get_worksheet(0)
    def getCellValue(self, cellValue):
        return self.worksheet.acell(cellValue).value
    def changeValue(self, label, newValue):
        self.worksheet.update_acell(label, newValue)
    def columnValues(self, column):
        return self.worksheet.col_values(column)
    def rowValues(self, row):
        return self.worksheet.row_values(row)
DataChiv = ChivData()
print(DataChiv.teamRooster["Accolade"].playerRooster["Jangle"].killsTotal)  
