'''
Created on Aug 15, 2016

@author: Jacob
'''
import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    '''
    Windows object
    '''
    def __init__(self, Directory):
        self.Directory = Directory
        self.setGeometry(50, 100, 500, 300)
        self.setWindowTitle("Harambe's Chiv Data Cruncher")
        self.setWindowIcon(QtGui.QIcon('Other Files\chivalrymedievalwarfare'))
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Create Match", self)
        btn.clicked.connect(self.matchCreate)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,0)
        self.show()
    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QtGui.QMessageBox.question(self, 'Message', 
            quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def matchCreate(self):
        self.Directory.matchCreate()
    
def run(Directory):
    app = QtGui.QApplication([])
    GUI = Window(Directory)
    app.exec_()

    