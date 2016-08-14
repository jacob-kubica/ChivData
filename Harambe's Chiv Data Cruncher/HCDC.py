'''
Created on Aug 12, 2016

@author: Jacob
'''
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys

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
        self.killsTotal = self.killsTotal + int(kills)
        self.deathsTotal = self.deathsTotal + int(deaths)
        self.assistsTotal = self.assistsTotal + int(assists)
        self.kDRatioTotal = self.killsTotal/self.deathsTotal
class Team(object):
    '''
    Team Object which contains info specific to the team
    and methods to update and calculate team specific values
    also handles playerDir a dictionary containing
    all player objects
    '''
    def __init__(self, teamName):
        '''
        Set Attributes
        '''
        #Static Values
        self.teamName = teamName #Identifier
        self.playerList = [] #List of player identifiers
        self.playerDir = {} #Player object container
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
    def ObjectCreator(self):
        '''
        Creates a playerList specific to the team
        '''
        for player in self.playerList:
            playerObj = Player(player)
            self.playerDir[player] = playerObj
class Half(object):
    '''
    Half object which contains data specific to the Half
    and methods to update and return half specific values
    '''
    def __init__(self, halfIdentifer, row, half, matchWrs, teamList, playerListTeamOne, playerListTeamTwo):
        '''
        Set Attributes
        '''
        #Input Variables
        self.halfIdentifer = halfIdentifer
        self.row = row + (half - 1)*8
        self.half = half
        self.matchWrs = matchWrs
        
        #Lists
        self.teamList = teamList
        self.playerListTeamOne = playerListTeamOne
        self.playerListTeamTwo = playerListTeamTwo
        self.playerList = self.playerListTeamOne + self.playerListTeamTwo
        
        #Directories
        self.teamDir = {}
        self.playerDir = {}
        
        self.gatherData()
        self.objectCreator()
        self.ValueUpdater()
    def gatherData(self):
        self.attacking = self.matchWrs.getCellValue("C" + str(self.row))
        self.defending = self.matchWrs.getCellValue("E" + str(self.row))
        self.objectiveReached = self.matchWrs.getCellValue("G" + str(self.row))
        self.objectiveTime = self.matchWrs.getCellValue("I" + str(self.row))    
        
    def objectCreator(self):
        if self.half == 1:
            teamOneObj = Team(self.teamList[0])
            teamOneObj.playerList = self.playerListTeamOne
            teamOneObj.ObjectCreator()
            self.teamDir[self.teamList[0]] = teamOneObj
            
            teamTwoObj = Team(self.teamList[1])
            teamTwoObj.playerList = self.playerListTeamTwo
            teamTwoObj.ObjectCreator()
            self.teamDir[self.teamList[1]] = teamTwoObj
        else:
            teamOneObj = Team(self.teamList[0])
            teamOneObj.playerList = self.playerListTeamOne
            teamOneObj.ObjectCreator()
            self.teamDir[self.teamList[0]] = teamOneObj
            
            teamTwoObj = Team(self.teamList[1])
            teamTwoObj.playerList = self.playerListTeamTwo
            teamTwoObj.ObjectCreator()
            self.teamDir[self.teamList[1]] = teamTwoObj
        for player in self.playerList:
            playerObj = Player(player)
            self.playerDir[player] = playerObj
            
    def teamCreate(self, teamName, playerList):
        '''
        Creates team object specific to half and places them into the teamDir
        '''
        team = Team(teamName)
        
        team.playerList = playerList
        team.playerDirCreation()
        self.teamDir[teamName] = team
    def ValueUpdater(self):
        '''
        Creates player object specific to half and places them into the playerDir 
        also fills out info for teams playerDir
        '''
        
        #Use Cases?
        for (i, player) in enumerate(self.playerList):
            if self.half == 1:
                if i < 6:
                    row = str(self.row + i + 2)
                    kills = self.matchWrs.getCellValue("C" + row)
                    deaths = self.matchWrs.getCellValue("D" + row)
                    assists = self.matchWrs.getCellValue("E" + row)
                    self.teamDir[self.attacking].playerDir[player].updateValues(kills, deaths, assists)
                else:
                    row = str(self.row + (i-5) + 1)
                    kills = self.matchWrs.getCellValue("H" + row)
                    deaths = self.matchWrs.getCellValue("I" + row)
                    assists = self.matchWrs.getCellValue("J" + row)
                    self.teamDir[self.defending].playerDir[player].updateValues(kills, deaths, assists)
                self.playerDir[player].updateValues(kills, deaths, assists)
            else:
                if i < 6:
                    row = str(self.row + i + 2)
                    kills = self.matchWrs.getCellValue("H" + row)
                    deaths = self.matchWrs.getCellValue("I" + row)
                    assists = self.matchWrs.getCellValue("J" + row)
                    self.teamDir[self.defending].playerDir[player].updateValues(kills, deaths, assists)
                else:
                    row = str(self.row + (i-5) + 1)
                    kills = self.matchWrs.getCellValue("C" + row)
                    deaths = self.matchWrs.getCellValue("D" + row)
                    assists = self.matchWrs.getCellValue("E" + row)
                    self.teamDir[self.attacking].playerDir[player].updateValues(kills, deaths, assists) 
                self.playerDir[player].updateValues(kills, deaths, assists)
class Match(object):
    '''
    Match object which contains data specific to the match
    and methods to update and return half specific values
    '''
    def __init__(self, matchNum, matchWrs, matchIdentifier):
        '''
        Set Attributes
        '''
        #Match Create Variables
        self.matchNum = matchNum
        self.matchWrs = matchWrs
        self.matchIdentifier = matchIdentifier
        
        #Determines Base Row
        self.row = ((self.matchNum - 1)*16 + 1)
        
        #GatherData
        self.gatherData()
        
        #Directories
        self.halfDir = {}
        self.teamDir = {}
        self.playerDir = {}
        
        #Lists
        self.halfList = [1, 2]
        self.teamList = [self.TeamOne, self.TeamTwo]
        
        self.objectCreator()
        self.ValueUpdater()
    def gatherData(self):
        self.TeamOne = self.matchWrs.getCellValue("A" + str(self.row + 4))
        self.TeamTwo = self.matchWrs.getCellValue("A" + str(self.row + 6))
        self.Map = self.matchWrs.getCellValue("A" + str(self.row + 8))
        self.Winner = self.matchWrs.getCellValue("A" + str(self.row + 10))
        self.Loser = self.matchWrs.getCellValue("A" + str(self.row + 12))
        self.gatherplayerList()
    def gatherplayerList(self):
        self.playerList = []
        self.playerListTeamOne = []
        self.playerListTeamTwo = []
        for x in range(1, 7):
            row = str(self.row + 1 + x)
            self.playerListTeamOne.append(self.matchWrs.getCellValue("B" + row))
            self.playerListTeamTwo.append(self.matchWrs.getCellValue("G" + row))
        self.playerList = self.playerListTeamOne + self.playerListTeamTwo
    def objectCreator(self):
        for half in self.halfList:
            halfIdentifier = "match_" + str(self.matchNum) + "_" + str(half)
            halfObj = Half(halfIdentifier, self.row, half, self.matchWrs, self.teamList, self.playerListTeamOne, self.playerListTeamTwo)
            self.halfDir[half] = halfObj
        for team in self.teamList:
            teamObj = Team(team)
            teamObj.playerList = self.halfDir[1].teamDir[team].playerList
            teamObj.ObjectCreator()
            self.teamDir[team] = teamObj
        for player in self.playerList:
            playerObj = Player(player)
            self.playerDir[player] = playerObj                
    def ValueUpdater(self):
        for player in self.playerList:
            kills = self.halfDir[1].playerDir[player].killsTotal + self.halfDir[2].playerDir[player].killsTotal
            deaths = self.halfDir[1].playerDir[player].deathsTotal + self.halfDir[2].playerDir[player].deathsTotal
            assists = self.halfDir[1].playerDir[player].assistsTotal + self.halfDir[2].playerDir[player].assistsTotal
            for team in self.teamList:
                try:
                    self.teamDir[team].playerDir[player].updateValues(kills, deaths, assists)
                except:
                    pass
            self.playerDir[player].updateValues(kills, deaths, assists)
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
        self.MatchNumber = 1
        #Values pertaining to Teams 
        self.teamRoster = {}
        self.teamList = []
        self.teamWrs = SpreadSheet("https://docs.google.com/spreadsheets/d/1T6KWtWPa4UMvquZ_yuiaRN0PJBytHle7F8a4u3pzKtk/edit#gid=0")
        self.inputTeamWrs()
        
        #Master Dictionary
        self.matchWrs = SpreadSheet("https://docs.google.com/spreadsheets/d/1ia8PwjHRf4newhe7Gl5DEvMCjVFs0VswXSkH57lYT78/edit#gid=0")
        self.matchList = []
        self.matchDir = {}
        
        self.matchCreate()
    def matchCreate(self):
        '''
        Gather data for and create Match Rooster match by match
        Also either contains or calls method to update player objects and team objects
        '''
        matchIdentifier = "match_" + str(self.MatchNumber)
        match = Match(self.MatchNumber, self.matchWrs, matchIdentifier)
        self.matchDir[matchIdentifier] = match
        
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
            self.teamRoster[team].ObjectCreator()
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


print(HCDC.matchDir['match_1'].halfDir[2].playerDir["Crimson King"].killsTotal)
print(HCDC.matchDir['match_1'].halfDir[2].playerDir["Crimson King"].deathsTotal)
print(HCDC.matchDir['match_1'].halfDir[2].playerDir["Crimson King"].assistsTotal)
print(HCDC.matchDir['match_1'].halfDir[2].playerDir["Crimson King"].kDRatioTotal)
print(HCDC.matchDir['match_1'].halfDir[1].teamDir["Accolade"].playerDir["Crimson King"].killsTotal)
print(HCDC.matchDir['match_1'].halfDir[1].teamDir["Accolade"].playerDir["Crimson King"].deathsTotal)
print(HCDC.matchDir['match_1'].halfDir[1].teamDir["Accolade"].playerDir["Crimson King"].assistsTotal)
print(HCDC.matchDir['match_1'].halfDir[1].teamDir["Accolade"].playerDir["Crimson King"].kDRatioTotal)
print(HCDC.matchDir['match_1'].halfDir[2].teamDir["Accolade"].playerDir["Crimson King"].killsTotal)
print(HCDC.matchDir['match_1'].halfDir[2].teamDir["Accolade"].playerDir["Crimson King"].deathsTotal)
print(HCDC.matchDir['match_1'].halfDir[2].teamDir["Accolade"].playerDir["Crimson King"].assistsTotal)
print(HCDC.matchDir['match_1'].halfDir[2].teamDir["Accolade"].playerDir["Crimson King"].kDRatioTotal)
print(HCDC.matchDir['match_1'].playerDir["Crimson King"].killsTotal)
print(HCDC.matchDir['match_1'].playerDir["Crimson King"].deathsTotal)
print(HCDC.matchDir['match_1'].playerDir["Crimson King"].assistsTotal)
print(HCDC.matchDir['match_1'].playerDir["Crimson King"].kDRatioTotal)


'''
Testing
print(HCDC.matchDir['match_1'].playerList)
print(HCDC.matchDir['match_1'].teamDir)
print(HCDC.matchDir['match_1'].halfDir)
print(HCDC.matchDir['match_1'].teamDir["Accolade"].playerDir)
print(HCDC.matchDir['match_1'].teamDir["The Void"].playerDir)
print(HCDC.matchDir['match_1'].halfDir["match_1_1"].playerDir)
print(HCDC.matchDir['match_1'].halfDir["match_1_2"].playerDir)
print(HCDC.matchDir['match_1'].halfDir["match_1_1"].teamDir)
print(HCDC.matchDir['match_1'].halfDir["match_1_1"].teamDir["Accolade"].playerDir)
print(HCDC.matchDir['match_1'].halfDir["match_1_1"].teamDir["The Void"].playerDir)
print(HCDC.matchDir['match_1'].halfDir["match_1_2"].teamDir)
print(HCDC.matchDir['match_1'].halfDir["match_1_2"].teamDir["Accolade"].playerDir)
print(HCDC.matchDir['match_1'].halfDir["match_1_2"].teamDir["The Void"].playerDir)
'''