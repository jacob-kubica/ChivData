'''
Created on Aug 18, 2016

@author: Jacob
'''
''' 

Player level: Viz -> combatScore ratio (line graph, match by match), combatScore ratio relative (line graph, match by match) <- if this can be done easily, 
              List -> total kills, total assists, total deaths, combatScore ratio, combatScore relative

Team level: Viz -> team kill/death ratio (line graph, match by match), players combatScore ratio (bar graph)
            List -> wins, losses, winloss ratio, total kill/death ratio

Tournament level: Viz -> top teams in total kill/death ratio (bar graph), top archers in combatScore ratio (bar graph, all archers included), 
                         top 10 players in combatScore ratio (bar graph), top players 10 in combatScore relative (bar graph),
                         bottom 10 players in combatScore ratio (bar graph), bottom 10 players in combatScore relative (bar graph),
                         top teams in win/loss ratio (bar graph)
                
                 List -> none 
'''
import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [6,7,8,2,5]
plt.bar(x,y, label = 'Bars1')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show() 