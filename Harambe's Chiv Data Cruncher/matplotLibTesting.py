'''
Created on Aug 18, 2016

@author: Jacob
'''
''' 

Player level: Viz -> combatScore ratio (line graph, match by match), combatScore ratio relative (line graph, match by match) <- if this can be done easily, 
              List -> total kills, total assists, total deaths, combatScore ratio, combatScore relative

Team level: Viz -> team kill/death ratio (line graph, match by match), players combatScore ratio (bar graph)
            List -> wins, losses, winloss ratio, total kill/death ratio, player combatScore relative 

Tournament level: Viz -> top teams in total kill/death ratio (bar graph), top archers in combatScore ratio (bar graph, all archers included), 
                         top 10 players in combatScore ratio (bar graph), top players 10 in combatScore relative (bar graph),
                         bottom 10 players in combatScore ratio (bar graph), bottom 10 players in combatScore relative (bar graph),
                         top teams in win/loss ratio (bar graph)
                
                 List -> none 2
'''
import matplotlib.pyplot as plt

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
        x = [2,4,6]
        y = [16.9, 12.8, 6.9]
        labels = ["NathookGD","Kylerr","Sombo"]
        plt.bar(x,y)
        plt.xticks(x,labels)
        plt.xlabel('Players')
        plt.ylabel('Combat Score')
        plt.title('Player Combat Score')
        plt.show()

Graph = Graphs()
Graph.teamLevelPlayerCombatScore()
                
                
            
        
        