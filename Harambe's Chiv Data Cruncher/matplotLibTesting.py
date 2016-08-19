'''
Created on Aug 18, 2016

@author: Jacob
'''
''' 

Player level: Viz -> combatScore ratio (line graph, match by match), combatScore ratio relative (line graph, match by match) <- if this can be done easily, 
              List -> total kills, total assists, total deaths, combatScore ratio, combatScore relative

Team level: Viz -> team kill/death ratio (line graph, match by match), players combatScore ratio (bar graph) player combatScore relative 
            List -> wins, losses, winloss ratio, total kill/death ratio, 

Tournament level: Viz -> top teams in total kill/death ratio (bar graph), top archers in combatScore ratio (bar graph, all archers included), 
                         top 10 players in combatScore ratio (bar graph), top players 10 in combatScore relative (bar graph),
                         bottom 10 players in combatScore ratio (bar graph), bottom 10 players in combatScore relative (bar graph),
                         top teams in win/loss ratio (bar graph)
                
                 List -> none 2
'''
import matplotlib.pyplot as plt
import numpy as np

'''
x = [2,4,6,8,10]
y = [6,7,8,2,5]

x2=[1,3,5,7,9]
y2=[7,8,2,4,2]
plt.bar(x,y, label = 'Bars1', color = 'red')
plt.bar(x2,y2,label = "Bars2", color = 'blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
'''

class Graphs():    
    def teamLevelPlayerCombatScore(self):
        teamName = "G.W.A"
        playerList = ("Nathook", "Kylerr", "Sombo", "Waterboy", "Jared39", "Valkryaz")
        y = (18,12,13,18.5,16,14)
        
        numPlayers = len(playerList)
        fig,ax = plt.subplots()
        
        index = np.arange(numPlayers)
        
        opacity = 0.4
        error_config = {'ecolor':'0.3'}
        
        rects1 = plt.bar(index, y, alpha = opacity, color = 'b', error_kw = error_config, label = "Players", align = 'center')
        
        plt.ylabel('Combat Score Ratio')
        plt.title(teamName + " Player Level Combat Score Ratio")
        plt.xticks(index, playerList)
        plt.tight_layout()
        
        ax.set_ylim([0,max(y)+2.5])
        plt.subplots_adjust(wspace = 0.5)
        
        plt.show()
        
    def teamLevelPlayerCombatScoreRelative(self):
        
        teamName = "G.W.A"
        playerList = ("Nathook", "Kylerr", "Sombo", "Waterboy", "Jared39", "Valkryaz")
        y = (18,12,-2,18.5,16,-5)
        
        numPlayers = len(playerList)
        fig, ax = plt.subplots()
        
        index = np.arange(numPlayers)
        
        opacity = 0.4
        error_config = {'ecolor':'0.3'}
        
        rects1 = plt.bar(index, y, alpha = opacity, color = 'b', error_kw = error_config, label = "Players", align = 'center')
        

        plt.ylabel('Combat Score Relative')
        plt.title(teamName + ' Player Level Combat Score Relative')
        plt.xticks(index, playerList)
        plt.tight_layout()
        
        ax.set_ylim([-1*(max(y))-2.5,max(y)+2.5])
        plt.subplots_adjust(wspace = 0.5)
        plt.axhline(0, color = "black")
        
        plt.show()
    
    def tournamentLevelTopTeamKD(self):
        
        teamList = ("G.W.A", "Kila", "Fight Club", "Legion", "Serenity")
        y = (1.36, 0.82, 1.12, 1.26, 0.76)
        
        numTeams = len(teamList)
        fig, ax = plt.subplots()
        
        index = np.arange(numTeams)
        
        opacity = 0.4
        error_config = {'ecolor':'0.3'}
        
        rects1 = plt.bar(index, y, alpha = opacity, color = 'b', error_kw = error_config, label = "Players", align = 'center')
        

        plt.ylabel('Kill/Death Ratio')
        plt.title('Total Team K/D Ratios')
        plt.xticks(index, teamList)
        plt.tight_layout()
        
        ax.set_ylim([0,max(y)+0.25])
        plt.subplots_adjust(wspace = 0.5)
        
        plt.show()
        
    def tournamentLevelTopArcherCombatRatio(self):
        playerList = ("Russian Mafia", "Skillz", "Pnobio", "Digital", "Jared39", "Cervantes")
        y = (24,12,13,18.5,16,14)
        
        numPlayers = len(playerList)
        fig,ax = plt.subplots()
        
        index = np.arange(numPlayers)
        
        opacity = 0.4
        error_config = {'ecolor':'0.3'}
        
        rects1 = plt.bar(index, y, alpha = opacity, color = 'b', error_kw = error_config, label = "Players", align = 'center')
        
        plt.ylabel('Combat Score Ratio')
        plt.title(" Archer  Combat Score Ratio")
        plt.xticks(index, playerList)
        plt.tight_layout()
        
        ax.set_ylim([0,max(y)+2.5])
        plt.subplots_adjust(wspace = 0.5)
        
        plt.show()
        
    def tournamentLevelTopCombatRatio(self):
        playerList = ("Nathook", "Kylerr", "Sombo", "Waterboy", "Jared39", "Valkryaz", "Stinker", "Curly", "Wizardish", "Raw Boner")
        y = (18,12,13,18.5,16,14,21,19.8,17.6,15.3)
        
        numPlayers = len(playerList)
        fig,ax = plt.subplots()
        
        index = np.arange(numPlayers)
        
        opacity = 0.4
        error_config = {'ecolor':'0.3'}
        
        rects1 = plt.bar(index, y, alpha = opacity, color = 'b', error_kw = error_config, label = "Players", align = 'center')
        
        plt.ylabel('Combat Score Ratio')
        plt.title(" Top 10 Players in Combat Score Ratio")
        plt.xticks(index, playerList)
        plt.tight_layout()
        
        for label in ax.xaxis.get_ticklabels():
            label.set_rotation(45)
        
        ax.set_ylim([0,max(y)+2.5])
        plt.subplots_adjust(wspace = 0.25, bottom = 0.15)
        
        plt.show()
        
    def playerLevelCombatScore(self):
        playerName = "NathookGD"
        playerOpponentList = ("G.W.A", "Kila", "Legion","Serenity","Fight Club")
        playerCSmatchbymatch = (8.5,12.2,10.5,14,6)
        matchCount = 5
        playerCombatScoreRatio = 9.5
        n = np.arange(matchCount)
        plt.plot(n+1,playerCSmatchbymatch, marker = 'o', color = 'b')
        plt.subplot().set_ylim(0,max(playerCSmatchbymatch)+2.5)
        plt.subplot().set_xlim(0,matchCount+1)
        plt.axhline((playerCombatScoreRatio), color = "black")
        plt.ylabel('Combat Score Ratio')
        plt.xlabel('Opponent')
        plt.title(playerName + " Match by Match CS Ratio")
        plt.xticks(n + 1, playerOpponentList)
        plt.show()
        
Graph = Graphs()
#Graph.teamLevelPlayerCombatScore()
#Graph.teamLevelPlayerCombatScoreRelative()
#Graph.tournamentLevelTopTeamKD()
#Graph.tournamentLevelTopArcherCombatRatio()
#Graph.tournamentLevelTopCombatRatio()
Graph.playerLevelCombatScore()
                
            
        
        