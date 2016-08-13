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
    also handles playerRoster a dictionary containing
    all player objects
    '''
    def __init__(self, teamName):
        '''
        Set Attributes
        '''
        #Static Values
        self.teamName = teamName #Identifier
        self.playerList = [] #List of player objects
        self.playerRoster = {} #Player object container
        #Dynamic Values
        self.teamWinsTotal = None
        self.teamLossTotal = None
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
    def playerRosterCreation(self):
        '''
        Creates a playerRoster specific to the team
        '''
        for player in self.playerList:
            x = Player(player)
            self.playerRoster[player] = x
"""
class ScoreBoard(object):
    '''
    ScoreBoard object which contains data specific to a 
    teams score at the end of a single game and methods 
    to update and return scoreBoard specific values
    '''
    def __init__(self, teamName):
        '''
        Set Attributes
        '''
        set.identifier = None
        self.teamList = {}
        self.playerList = {}
    def indentifierGenerator(self):
        '''
        Generates a specific identifier for each scoreBoard 
        object so that scoreBoard can be stored in a dictionary
        and easily called
        '''
        pass
    def playerListFill(self):
        '''
        Fills the playerList with player objects
        '''
        pass
"""
class Half(object):
    '''
    Half object which contains data specific to the Half
    and methods to update and return half specific values
    '''
    def __init__(self, teamName):
        '''
        Set Attributes
        '''
        self.identifier = None
        self.attacking  = None
        self.defending = None
        self.objective = None
        self.objectiveTime = None
        self.playerList = {}
        self.teamList = {}
        self.scoreBoards = {}
    def indentifierGenerator(self):
        '''
        Generates a specific identifier for each Half 
        Object so that the Half can be stored in a dictionary
        and easily called
        '''
        pass
    def scoreBoardGen(self):
        '''
        Generates a ScoreBoard Object
        '''
        pass
class Match(object):
    '''
    Match object which contains data specific to the match
    and methods to update and return half specific values
    '''
    def __init__(self, teamName):
        '''
        Set Attributes
        '''
        self.matchNum = None
        self.TeamOne = None
        self.TeamTwo = None
        self.Map = None
        self.Winner = None
        self.Loser = None
        
        self.playerList = {}
        self.teamList = {}
        self.halfList = {}
        self.scoreBoardList = {}
    def indentifierGenerator(self):
        '''
        Generates a specific identifier for each Match 
        object so that the match can be stored in a dictionary
        and easily called
        '''
        pass
    def HalfGen(self):
        '''
        Generates a Half Object
        '''
        pass
    def scoreBoardMatch(self):
        '''
        Generates a Scoreboard object for each team in the match
        '''
        pass
class Tourney():
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
        #Values pertaining to Teams 
        self.teamRoster = {}
        self.teamList = []
        self.teamWrs = SpreadSheet("https://docs.google.com/spreadsheets/d/1T6KWtWPa4UMvquZ_yuiaRN0PJBytHle7F8a4u3pzKtk/edit#gid=0")
        self.inputTeamWrs()
        
        #Master Dictionary
        self.matchWrs = SpreadSheet("https://docs.google.com/spreadsheets/d/1ia8PwjHRf4newhe7Gl5DEvMCjVFs0VswXSkH57lYT78/edit#gid=0")
        self.matchList = []
        self.matchRoster = {}
        
    def inputTeamWrs(self):
        '''
        Gather data for and creates teamRoster and PlayerRoster within team objects
        '''
        col = self.teamWrs.columnValues(1)
        for x in range(1, len(col)):
            self.teamList.append(col[x])
        for (i, team) in enumerate(self.teamList):
            self.teamRoster[team] = Team(team)
            playerList = self.teamWrs.rowValues(i + 2)
            for x in range(1,len(playerList)):
                if playerList[x] == '':
                    break
                else:
                    self.teamRoster[team].playerList.append(playerList[x])
            self.teamRoster[team].playerRosterCreation()
    def matchInput(self):
        '''
        Gather data for and create Match Rooster match by match
        Also either contains or calls method to update player objects and team objects
        '''
        pass
    def halfInput(self):
        '''
        Gather data for and create Match Rooster match by match
        Also either contains or calls method to update player objects and team objects
        '''
        pass
    def deterInput(self):
        '''
        Determine and call Input Method
        '''
        pass
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
HCDC = Tourney()
print(HCDC.teamRoster["Accolade"].playerRoster["Jangle"].killsTotal)  

#Tourney.matchRoster[""].halfList[""].teamList[""].playerList[""].killsTotal
