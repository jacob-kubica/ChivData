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
        #self.isArcher = isArcher
        
        #Dynamic Values
        #MultiMatchValues
        self.killsTotal = 0
        self.deathsTotal = 0
        self.assistsTotal = 0
        self.kDRatioTotal = 0
        
        #SingleMatchValues
        self.kills = 0
        self.deaths = 0
        self.assists = 0 
        self.kDRatioMatch = 0
    def updateValues(self, kills, deaths, assists):
        '''
        Updates values after match completion
        '''
        self.updateKills(kills)
        self.updateDeaths(deaths)
        self.updateAssist(assists)
        self.updateKDratio()
    def updateKills(self, newValue):
        '''
        Updates pertaining to kills
        '''
        self.killsTotal = self.killsTotal + newValue
        self.kills = newValue
    def updateDeaths(self, newValue):
        '''
        Updates pertaining to Deaths
        '''
        self.deathsTotal = self.deathsTotal + newValue
        self.deaths = newValue
    def updateAssist(self, newValue):
        '''
        Updates pertaining to Assists
        
        '''
        self.assistsTotal = self.assistsTotal + newValue
        self.assists = newValue
    def updateKDratio(self):
        '''
        Updates pertaining to Kill/Death ratio
        '''
        self.kDRatioTotal = self.kills/self.deaths
        self.kDRatioMatch = self.kills/self.deaths
    def returnValues(self):
        '''
        Returns all the player attributes
        '''
        valueReturnList = [self.playerName, self.killsTotal, self.deathsTotal, self.kDRatioTotal, self.kills, self.deaths, self.kDRatioMatch]
        return valueReturnList
    def clearValues(self):
        '''
        Clears values that are match dependent
        '''
        self.kills = 0
        self.deaths = 0 
        self.kDRatioMatch = 0
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
        self.teamLossTotal -= 1
    def playerRoosterCreation(self):
        '''
        Creates a playerRooster specific to the team
        '''
        
        for player in self.playerList:
            x = Player(player)
            self.playerRooster[player] = x
        print(self.playerRooster)
class Match():
    '''
    Match Object which contains info specific to the match
    and methods to update and calculate team specific values
    going to treat each half as a a seperate match for the time being
    '''
    def __init__(self, matchNumber, matchHalf, teamOne, teamTwo):
        '''
        Set Attributes
        '''
        self.matchNumber = matchNumber
        self.matchHalf = matchHalf
        self.matchSetup()
    def matchOutcomes(self, winner, loser):
        '''
        Create match specific variables
        '''
        #Match Specific Data
        self.winner = winner
        self.loser = loser
    def TeamOneCreate(self, TeamOneName, T1player1, T1player2, T1player3, T1player4, T1player5, T1player6):
        '''
        Creates Team One variables
        '''
        self.TeamOneName = TeamOneName
        self.T1player1 = T1player1
        self.T1player2 = T1player2
        self.T1player3 = T1player3
        self.T1player4 = T1player4
        self.T1player5 = T1player5
        self.T1player6 = T1player6
        self.TeamOne = [self.T1player1, self.T1player2, self.T1player3, self.T1player4, self.T1player5, self.T1player6]                
    def TeamTwoCreate(self, TeamTwoName, T2player1, T2player2, T2player3, T2player4, T2player5, T2player6):
        '''
        Creates Team Two variables
        '''
        #Team Two
        self.TeamTwoName = TeamTwoName
        self.T2player1 = T2player1
        self.T2player2 = T2player2
        self.T2player3 = T2player3
        self.T2player4 = T2player4
        self.T2player5 = T2player5
        self.T2player6 = T2player6        
        self.TeamTwo = [self.T2player1, self.T2player2, self.T2player3, self.T2player4, self.T2player5, self.T2player6]
class statisticalAnalysisMethods(object):
    '''
    contains statistical analysis methods
    attempt to keep statistical analysis to 
    this object for easier implementation into gui and for a clearer 
    more easier to navigate code base
    '''
    def average(self):
        '''
        finds the average
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
class DataViz(object):
    '''
    Contains methods specific to data visualization
    I'll leave this to you i don't know jack shit about this
    '''
    def __init__(self):
        self.dataVizType = ""
class GUI(object):
    '''
    Holds Gui Elements
    Look Up pyQt this is the GUI framework I have experience with
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
        pass
    def button(self):
        '''
        Handles New Button implements
        '''
        pass
    def text(self):
        '''
        Handles text implements
        '''
        pass
    def display(self):
        '''
        Handles Display implements
        '''
        pass
    def dropdownMenu(self):
        '''
        Handles drop down menu implements:
        '''
        pass
    def checkbox(self):
        '''
        Handles checkbox implements
        '''
        pass
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
        self.matchRooster = {}
        self.matchList = ["Import"]
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
        self.teamListCreate()
        self.teamListFill()
    def matchCreate(self, matchNumber, matchHalf):
        '''
        Method to create a match object
        '''
        match = Match(matchNumber, matchHalf)
        dictionaryName = "match" + str(match.matchNumber) + "." + str(match.matchHalf)
        self.matchRooster[dictionaryName] = match
    def newMatch(self, matchNumber, matchHalf):
        '''
        Handles what happens after the completion of a a match
        '''
        self.matchCreate(matchNumber, matchHalf)
        dictionaryName = "match" + str(matchNumber) + "." + str(matchHalf)
        self.match = self.matchRooster[dictionaryName]
        self.match.matchOutcomes("Winner", "Loser")
        self.match.TeamOneCreate("TeamName", "Player1", "player2", "player3", "player4", "player5", "player6")
        self.match.TeamTwoCreate("TeamName", "Player1", "player2", "player3", "player4", "player5", "player6")
    def TeamCreate(self, teamName):
        '''
        add a team to the team Rooster
        '''
        team = Team(teamName)
        self.teamRooster[teamName] = team        
    def teamListCreate(self):
        #values_list = worksheet.col_values(1)
        teamList = self.teamWrs.columnValues(1)
        for x in range(1, len(teamList)):
            self.teamList.append(teamList[x])
    def teamListFill(self):
        '''
        Handles Player Rooster Creation
        '''
        counter = 1
        for team in self.teamList:
            self.TeamCreate(team)
            counter += 1
            playerList = self.teamWrs.rowValues(counter)
            for x in range(1,len(playerList)):
                if playerList[x] == '':
                    break
                else:
                    self.teamRooster[team].playerList.append(playerList[x])
            self.teamRooster[team].playerRoosterCreation()
    def teamUpate(self, match):
        '''
        Handles updating team object after match completion
        '''
        self.match = self.matchRooster[match]
        self.winner = self.match.winner
        self.loser = self.match.loser
        self.teamRooster[self.winner].teamWin()
        self.teamRooster[self.loser].teamLoss()
    def playerUpdate(self, match):
        '''
        Handles updating player objects after match completion
        '''
        teamOne = self.match.TeamOne
        teamOneName = self.match.TeamOneName
        teamTwo = self.match.TeamTwo
        teamTwoName = self.match.TeamTwoName
        for player in teamOne:
            self.teamRooster[teamOneName].playerRooster[player].updateValues("Kills", "Deaths", "Assists")
        for player in teamTwo:
            self.teamRooster[teamTwoName].playerRooster[player].updateValues("Kills", "Deaths", "Assists")
    def updateRosters(self, match):
        '''
        Calls any update methods after match completion
        '''
        self.teamUpate(match)
        self.playerUpdate(match)
DataChiv = ChivData()
print(DataChiv.teamRooster["Accolade"].playerRooster["Jangle"].kills)  
