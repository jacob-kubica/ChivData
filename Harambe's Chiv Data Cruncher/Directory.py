'''
Created on Aug 16, 2016

@author: Jacob
'''
from SpreadSheet import SpreadSheet
from Match import Match
from Half import Half
from Team import Team
from Player import Player

import time #for use in program timing
start_time = time.time()
import operator
class Directory():
    '''
    Directory object which handles creation of
    player, team, half, match objects. Pulls data
    from google spreadsheet. Update values for
    pertaining objects.
    '''
    def __init__(self):
        '''
        Constructor
        '''
        #Directories
        self.playerDir = {}
        self.teamDir = {}
        self.matchDir = {}
        self.matchNumber = 1
        #Lists
        self.playerList = []
        self.teamList = []
        #Spreadsheets
        self.teamWrs = SpreadSheet("https://docs.google.com/spreadsheets/d/1T6KWtWPa4UMvquZ_yuiaRN0PJBytHle7F8a4u3pzKtk/edit#gid=0")
        self.teamWrs.worksheetDirBuild(0)
        x = time.time() - start_time
        
        self.loadSpreadSheet()
        
        #Main Sequence of program
        self.inputTeamWrs()
        self.playerCreate()
        self.loadSpreadSheet()
    def matchCreate(self, matchNumber):
        '''
        Create match object and add to match directory
        '''
        self.setMatchNumber(matchNumber)
        match = Match(self.matchNumber, self.matchWrs)
        self.matchDir[self.matchNumber] = match
        self.ValueUpdater(self.matchNumber)
        #Updates tournament wide values
    def playerCreate(self):
        '''
        Create player object and add to player directory
        '''
        for player in self.playerList:
            playerObj = Player(player)
            self.playerDir[player] = playerObj
    def inputTeamWrs(self):
        '''
        Gather data for and creates teamDir
        '''
        col = self.teamWrs.columnValues(1)
        #Gathers all the team names
        for x in range(1, len(col)):
            if col[x] != "":
                self.teamList.append(col[x])
            else:
                break
        #Creates team objects for each
        for (i, team) in enumerate(self.teamList):
            self.teamDir[team] = Team(team)
            #finds all the players on a specific team
            playerList = self.teamWrs.rowValues(i + 1)
            for x in range(1,len(playerList)):
                #ensures blank cells are ignored
                if playerList[x] == '':
                    break
                else:
                    #updates team object player list 
                    self.teamDir[team].playerList.append(playerList[x])
                    #updates tournament object player list 
                    self.playerList.append(playerList[x])
            #creates player objects for each team
            self.teamDir[team].ObjectCreator()
    def ValueUpdater(self, matchNumber):
        '''
        Updates tournament wide values
        '''
        #Updates Player Values
        playerList = self.matchDir[matchNumber].playerList
        for player in playerList:
            #Gets player values from certain match
            kills = self.matchDir[matchNumber].playerDir[player].kills
            deaths = self.matchDir[matchNumber].playerDir[player].deaths
            assists = self.matchDir[matchNumber].playerDir[player].assists
            #Updates player object
            self.playerDir[player].updateValues(kills, deaths, assists, None)
            #Updates team object's player objects
            for team in self.matchDir[matchNumber].teamList:
                try:
                    self.teamDir[team].playerDir[player].updateValues(kills, deaths, assists, None)
                except:
                    pass
        #Updates Team Values
        self.teamDir[self.matchDir[matchNumber].winner].Win()
        self.teamDir[self.matchDir[matchNumber].loser].Loss()
        self.teamDir[self.matchDir[matchNumber].winner].updateValues()
        self.teamDir[self.matchDir[matchNumber].loser].updateValues()
    def dirPull(self, *args):
        '''
        method to pull data from directory
        ensure args are placed in order of largest to smallest object
        '''
        #=======================================================================
        # Don't mess with this
        #=======================================================================
        argNum = len(args)
        if any(x in self.playerList for x in args):
            if any(x in self.teamList for x in args):
                if argNum == 4:
                    return self.matchDir[args[0]].halfDir[args[1]].teamDir[args[2]].playerDir[args[3]]
                else:
                    return self.matchDir[args[0]].teamDir[args[1]].playerDir[args[2]]
            else:
                if argNum == 3:
                    return self.matchDir[args[0]].halfDir[args[1]].playerDir[args[2]]
                if argNum == 2:
                    return self.matchDir[args[0]].playerDir[args[1]]
                if argNum == 1:
                    return self.playerDir[args[0]]
        elif any(x in self.teamList for x in args):
            if argNum == 3:
                return self.matchDir[args[0]].halfDir[args[1]].teamDir[args[2]]
            if argNum == 2:
                return self.matchDir[args[0]].teamDir[args[1]]
            if argNum == 1:
                return self.teamDir[args[0]]
        else:
            if argNum == 2:
                return self.matchDir[args[0]].halfDir[args[1]]
            elif argNum == 1:
                return self.matchDir[args[0]]
            else:
                pass
    def reloadMatches(self, matchNumber):
        '''
        Reloads entire directory overwriting existing objects
        '''
        self.clearTopDirectory()
        self.setMatchNumber(matchNumber)
        numMatches = self.matchNumber
        for x in range (0, numMatches):
            try:
                self.matchCreate(x + 1)
            except:
                break
        self.bottomTenPlayerCombatScoreRelative = None
        self.bottomTenPlayersCombatScore = None
        self.topTenPlayerCombatScore = None
        self.topTenPlayerCombatScoreRelative = None
        self.sortedCombatScore()
        self.sortedCombatScoreRelative()
    def loadSpreadSheet(self):
        self.matchWrs = SpreadSheet("https://docs.google.com/spreadsheets/d/1ia8PwjHRf4newhe7Gl5DEvMCjVFs0VswXSkH57lYT78/edit#gid=0")
        self.matchWrs.worksheetDirBuild(1) 
    def setMatchNumber(self, newValue):
        if newValue != 0:
            self.matchNumber = newValue
    def clearTopDirectory(self):
        '''
        Clears tournament wide directories
        '''
        for team in self.teamList:
            self.teamDir[team].clearValues()
            for player in self.teamDir[team].playerList:
                self.teamDir[team].playerDir[player]
        for player in self.playerList:
            self.playerDir[player].clearValues()
    def sortedCombatScore(self):
        """
        # regular unsorted dictionary
            d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
            
            # dictionary sorted by value
            OrderedDict(sorted(d.items(), key=lambda t: t[1]))
            # OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
        """
        d = {}
        for player in self.playerList:
            d[player] = self.playerDir[player].combatScoreRatio
        sorted_d = sorted(d.items(), key=operator.itemgetter(1))
        self.topTenPlayerCombatScore = []
        self.bottomTenPlayersCombatScore = []
        for x in range(0, len(sorted_d)):
            c = sorted_d[x]
            if c[1] > 0:
                if len(self.bottomTenPlayersCombatScore) <10:
                    self.bottomTenPlayersCombatScore.append(c[0])
            if x >= (len(sorted_d) - 10):
                self.topTenPlayerCombatScore.append(c[0])
    def sortedCombatScoreRelative(self):
        d = {}
        for team in self.teamList:
            for player in self.teamDir[team].playerList:
                d[player] = self.playerDir[player].combatScoreRatio - self.teamDir[team].teamCDRatio
        sorted_d = sorted(d.items(), key=operator.itemgetter(1))
        self.topTenPlayerCombatScoreRelative = []
        self.bottomTenPlayerCombatScoreRelative = []
        for x in range(0, len(sorted_d)):
            c = sorted_d[x]
            if c[1] != 0:
                if len(self.bottomTenPlayerCombatScoreRelative) <10:
                    self.bottomTenPlayerCombatScoreRelative.append(c)
            if x >= (len(sorted_d) - 10):
                self.topTenPlayerCombatScoreRelative.append(c)
    