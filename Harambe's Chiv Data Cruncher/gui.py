'''
Created on Aug 15, 2016

@author: Jacob
'''
import sys
from PyQt4 import QtGui, QtCore
from HCDC import Directory

HCDC = Directory()

class Window(QtGui.QMainWindow):

    def __init__(self, Directory):
        super(Window, self).__init__()
        self.Directory = Directory
        self.setGeometry(50, 100, 500, 300)
        self.setWindowTitle("Harambe's Chiv Data Cruncher")
        self.setWindowIcon(QtGui.QIcon('Other Files\chivalrymedievalwarfare'))
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Create Match", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,0)
        self.show()

    def close_application(self):
        self.Directory.matchCreate()
    
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window(HCDC)
    sys.exit(app.exec_())


run()