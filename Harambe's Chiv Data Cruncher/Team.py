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
        return self.teamWins/self.teamLoss
    def clearValues(self):
        self.teamWins = 0
        self.teamLoss = 0 
        