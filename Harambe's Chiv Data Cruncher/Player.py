'''
Created on Aug 16, 2016

@author: Jacob
'''
import time #for use in program timing
start_time = time.time()

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
        self.kills = 0
        self.deaths = 0
        self.assists = 0
        self.isArcher = False
        self.kDRatio = 0
        self.combatPoints = 0
    def updateValues(self, kills, deaths, assists, isArcher):
        '''
        Updates dynamic values
        '''
        self.kills = self.kills + int(kills)
        self.deaths = self.deaths + int(deaths)
        self.assists = self.assists + int(assists)
        self.combatPoints = self.combatPoints + (10*kills + 5*assists)
        if isArcher == "TRUE":
            self.isArcher = True
        self.kDRatio = self.kills/self.deaths
    def clearValues(self):
        self.kills = 0 
        self.deaths = 0
        self.assists = 0 
        self.kDRatio = 0