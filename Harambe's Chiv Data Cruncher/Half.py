'''
Created on Aug 16, 2016

@author: Jacob
'''
import time #for use in program timing
start_time = time.time()

from Team import Team
from Player import Player

class Half(object):
    '''
    Half object which contains data specific to the Half
    and methods to update and return half specific values
    '''
    def __init__(self, row, half, matchWrs, teamList, playerListTeamOne, playerListTeamTwo):
        '''
        Set Attributes
        '''
        #Input Variables
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
        #Main Sequence
        self.gatherData()
        self.objectCreator()
        self.ValueUpdater()
    def gatherData(self):
        '''
        Gather data specific to half
        '''
        self.attacking = self.matchWrs.getCellValue("C" + str(self.row))
        self.defending = self.matchWrs.getCellValue("E" + str(self.row))
        self.objectiveReached = self.matchWrs.getCellValue("G" + str(self.row))
        self.objectiveTime = self.matchWrs.getCellValue("I" + str(self.row))    
    def objectCreator(self):
        '''
        Creates Team objects and Player objects 
        '''
        def TeamObjectCreate(team, playerList):
            teamObj = Team(team) #generates a Team object
            teamObj.playerList = playerList #updates player list for team object
            teamObj.ObjectCreator() #creates player objects for the team object
            self.teamDir[team] = teamObj #adds to directory
        TeamObjectCreate(self.teamList[0], self.playerListTeamOne) #Team Object for team one
        TeamObjectCreate(self.teamList[1], self.playerListTeamTwo) #Team Object for team one
        #Creates and adds player objects to player directory
        for player in self.playerList:
            playerObj = Player(player) #generates a player object
            self.playerDir[player] = playerObj #adds to directory
    def ValueUpdater(self):
        '''
        Creates player object specific to half and places them into the playerDir 
        also fills out info for teams playerDir
        '''
        #=======================================================================
        # this block of code needs to be fixed for redundancy
        #=======================================================================
        for (i, player) in enumerate(self.playerList): #iterates over player list and creates a counter
            if self.half == 1: #if first half
                if i < 6: #column #1
                    row = str(self.row + i + 2) #determines the row the player data is on
                    #Gather data from spreadsheet
                    x = time.time() - start_time
                    kills = self.matchWrs.getCellValue("C" + row) 
                    deaths = self.matchWrs.getCellValue("D" + row)
                    assists = self.matchWrs.getCellValue("E" + row)
                    isArcher = self.matchWrs.getCellValue("F" + row)
                    #Update player Values in team directory
                    self.teamDir[self.attacking].playerDir[player].updateValues(kills, deaths, assists, isArcher)
                else: #column #2
                    row = str(self.row + (i-5) + 1) #determines the row the player data is on
                    #Gather data from spreadsheet
                    kills = self.matchWrs.getCellValue("H" + row)
                    deaths = self.matchWrs.getCellValue("I" + row)
                    assists = self.matchWrs.getCellValue("J" + row)
                    isArcher = self.matchWrs.getCellValue("K" + row)
                    #Update player Values in team directory
                    self.teamDir[self.defending].playerDir[player].updateValues(kills, deaths, assists, isArcher)
                #Update player Values in player directory
                self.playerDir[player].updateValues(kills, deaths, assists, isArcher)
            else: #if second half
                if i < 6: #column #1
                    row = str(self.row + i + 2) #determines the row the player data is on
                    #Gather data from spreadsheet
                    kills = self.matchWrs.getCellValue("H" + row)
                    deaths = self.matchWrs.getCellValue("I" + row)
                    assists = self.matchWrs.getCellValue("J" + row)
                    isArcher = self.matchWrs.getCellValue("K" + row)
                    #Update player Values in team directory
                    self.teamDir[self.defending].playerDir[player].updateValues(kills, deaths, assists, isArcher)
                else: #column #2
                    row = str(self.row + (i-5) + 1) #determines the row the player data is on
                    #Gather data from spreadsheet
                    kills = self.matchWrs.getCellValue("C" + row)
                    deaths = self.matchWrs.getCellValue("D" + row)
                    assists = self.matchWrs.getCellValue("E" + row)
                    isArcher = self.matchWrs.getCellValue("F" + row)
                    #Update player Values in team directory
                    self.teamDir[self.attacking].playerDir[player].updateValues(kills, deaths, assists, isArcher)
                #Update player Values in player directory
                self.playerDir[player].updateValues(kills, deaths, assists, isArcher)
        for team in self.teamList:
            self.teamDir[team].updateValues()