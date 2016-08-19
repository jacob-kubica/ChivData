'''
Created on Aug 16, 2016

@author: Jacob
'''
import time #for use in program timing
start_time = time.time()

from Half import Half
from Team import Team
from Player import Player

class Match(object):
    '''
    Match object which contains data specific to the match
    and methods to update and return half specific values
    '''
    def __init__(self, matchNum, matchWrs):
        '''
        Set Attributes
        '''
        #Match Create Variables
        self.matchNum = matchNum
        self.matchWrs = matchWrs
        #Determines Base Row
        self.row = ((self.matchNum - 1)*16 + 1)
        #Directories
        self.halfDir = {}
        self.teamDir = {}
        self.playerDir = {}
        #Lists
        self.halfList = [1, 2]
        #GatherData
        self.gatherData()
        self.objectCreator()
        self.ValueUpdater()
    def gatherData(self):
        '''
        Gather match specific data
        '''
        #Variables
        self.teamOne = self.matchWrs.getCellValue("A" + str(self.row + 4))
        self.teamTwo = self.matchWrs.getCellValue("A" + str(self.row + 6))
        self.map = self.matchWrs.getCellValue("A" + str(self.row + 8))
        self.winner = self.matchWrs.getCellValue("A" + str(self.row + 10))
        self.loser = self.matchWrs.getCellValue("A" + str(self.row + 12))
        
        #Lists
        self.teamList = [self.teamOne, self.teamTwo]
        self.playerListTeamOne = []
        self.playerListTeamTwo = []
        #fills player lists for each team
        for x in range(1, 7):
            row = str(self.row + 1 + x) #row calculation
            #get Values from spreadsheet
            self.playerListTeamOne.append(self.matchWrs.getCellValue("B" + row))
            self.playerListTeamTwo.append(self.matchWrs.getCellValue("G" + row))
        #gets a match specific list of players
        self.playerList = self.playerListTeamOne + self.playerListTeamTwo
    def objectCreator(self):
        '''
        Creates half, team, player objects and adds
        them to corresponding directories
        '''
        #=======================================================================
        # There has to be a way to remove redundancy here
        #=======================================================================
        #Half Object Creation
        for half in self.halfList:
            halfObj = Half(self.row, half, self.matchWrs, self.teamList, self.playerListTeamOne, self.playerListTeamTwo)
            self.halfDir[half] = halfObj
        #Team Object Creation
        for team in self.teamList:
            teamObj = Team(team)
            teamObj.playerList = self.halfDir[1].teamDir[team].playerList
            teamObj.ObjectCreator()
            self.teamDir[team] = teamObj
        #Player Object Creation
        for player in self.playerList:
            playerObj = Player(player)
            self.playerDir[player] = playerObj                
    def ValueUpdater(self):
        '''
        Updates match objects
        '''
        #Updates player objects
        for player in self.playerList:
            #calculates new values
            kills = self.halfDir[1].playerDir[player].kills + self.halfDir[2].playerDir[player].kills
            deaths = self.halfDir[1].playerDir[player].deaths + self.halfDir[2].playerDir[player].deaths
            assists = self.halfDir[1].playerDir[player].assists + self.halfDir[2].playerDir[player].assists
            #Updates team directory
            for team in self.teamList:
                try: #easier way to find player within team directory
                    self.teamDir[team].playerDir[player].updateValues(kills, deaths, assists, None)
                    break
                except:
                    pass
            self.playerDir[player].updateValues(kills, deaths, assists, None)
        #Updates team win/lose
        self.teamDir[self.winner].Win()
        self.teamDir[self.loser].Loss()
        self.teamDir[self.winner].updateValues()
        self.teamDir[self.loser].updateValues()