'''
Created on Aug 15, 2016

@author: Jacob
'''
import sys
from PyQt4 import QtGui

class GUI(QtGui.QMainWindow):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(GUI, self).__init__()
        self.setGeometry(50, 100, 800, 500)
        self.setWindowTitle("Harambe's Chivalry Data Cruncher")
        self.setWindowIcon(QtGui.QIcon('Other Files\chivalrymedievalwarfare.png'))
        
    def Home(self):
        '''
        '''
        btn = QtGui.QtPush("Quit", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.show()
        

app = QtGui.QApplication(sys.argv)
GUI = GUI()
GUI.show()
sys.exit(app.exec_())

"""

window =  QtGui.QWidget()
window.setGeometry(50, 100, 500, 300)
window.setWindowTitle("Harambe's Chiv Data Cruncher")

window.show()

"""