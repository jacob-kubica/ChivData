'''
Created on Aug 16, 2016

@author: Jacob
'''
import time #for use in program timing
start_time = time.time()

from Player import Player

class Team(object):
    '''
    Team object which contains info specific to the team
    and methods to update and calculate team specific values
    '''
    def __init__(self, teamName):
        '''
        Set Attributes
        '''
        #Static Values
        self.teamName = teamName #Identifier
        #player Values
        self.playerList = []
        #player directory
        self.playerDir = {} 
        #Dynamic Values
        self.teamWins = 0
        self.teamLoss = 0
        self.wLRatio = 0
        self.teamDeaths = 0
        self.teamKills = 0
        self.teamKDRatio = 0
        self.teamCDRatio = 0 
    def ObjectCreator(self):
        '''
        Fills player directory with player objects
        '''
        for player in self.playerList:
            playerObj = Player(player)
            self.playerDir[player] = playerObj
    def Win(self):
        '''
        Handles Case were team wins
        '''
        self.teamWins += 1
    def Loss(self):
        '''
        Handles Case were team loses
        '''
        self.teamLoss += 1
    def WLRatio(self):
        '''
        Returns Win loss ratio
        '''
        if self.teamLoss != 0:
            self.wLRatio = self.teamWins/self.teamLoss
        else:
            self.wLRatio = self.teamWins
    def KDRatio(self):
        if self.teamDeaths != 0:
            self.teamKDRatio = self.teamKills/self.teamDeaths
        else:
            self.teamKDRatio = self.teamKills 
    def Kills(self):
        playerKills = []
        for player in self.playerList:
            playerKills.append(int(self.playerDir[player].kills))
        self.teamKills = sum(playerKills)
    def Deaths(self):
        playerDeaths = []
        for player in self.playerList:
            playerDeaths.append(int(self.playerDir[player].deaths))
        self.teamDeaths = sum(playerDeaths)
    def cDRatio(self):
        playerCDRatio = []
        for player in self.playerList:
            playerCDRatio.append(int(self.playerDir[player].combatScoreRatio))
        playerCDRatio[:] = (value for value in playerCDRatio if value != 0)
        self.teamCDRatio = sum(playerCDRatio)/len(playerCDRatio)
    def updateValues(self):
        self.WLRatio()
        self.Kills()
        self.Deaths()
        self.KDRatio()
        self.cDRatio()
    def clearValues(self):
        self.teamWins = 0
        self.teamLoss = 0 
        self.wLRatio = 0
        self.teamDeaths = 0
        self.teamKills = 0
        self.teamKDRatio = 0
        self.teamCDRatio = 0 
        