'''
Created on Aug 15, 2016

@author: Jacob
'''
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Main Window Object
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1084, 813)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        #Object Grid Object
        self.dataTabLeft = QtGui.QWidget()        
        self.teamTabLeft = QtGui.QWidget()
        self.playerTabLeft = QtGui.QWidget()
        self.dataTabRight = QtGui.QWidget()
        self.teamTabRight = QtGui.QWidget()
        self.playerTabRight = QtGui.QWidget()
        
        self.ContainerBottom = QtGui.QWidget(self.centralwidget)
        self.tabsLeft = QtGui.QTabWidget(self.ContainerBottom)
        self.tabsLeft.addTab(self.dataTabLeft, _fromUtf8(""))
        self.tabsLeft.addTab(self.teamTabLeft, _fromUtf8(""))
        self.tabsLeft.addTab(self.playerTabLeft, _fromUtf8(""))
        
        self.tabsRight = QtGui.QTabWidget(self.ContainerBottom)        
        self.tabsRight.addTab(self.dataTabRight, _fromUtf8(""))
        self.tabsRight.addTab(self.teamTabRight, _fromUtf8(""))
        self.tabsRight.addTab(self.playerTabRight, _fromUtf8(""))
        #Match Input Group Box
        font = QtGui.QFont()
        self.MatchInputsGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.MatchInputsGroupBox.setFont(self.font(12, True, 75))
        #Match Number Label Object
        self.MatchNumberLabel = QtGui.QLabel(self.MatchInputsGroupBox)
        self.MatchNumberLabel.setFont(self.font(10, False, 50))
        #Match Number Spin Box Object
        self.matchNumberSpinBox = QtGui.QSpinBox(self.MatchInputsGroupBox)
        self.matchNumberSpinBox.setFont(self.font(10, False, 50))
        #Match Create Button Object
        self.CreateMatchPushBtn = QtGui.QPushButton(self.MatchInputsGroupBox)
        self.CreateMatchPushBtn.setFont(self.font(10, False, 50))
        #Reload Button Object
        self.ReloadDataPushBtn = QtGui.QPushButton(self.MatchInputsGroupBox)
        self.ReloadDataPushBtn.setFont(self.font(10, False, 50))
        #Progress Bar Object
        self.progressBar = QtGui.QProgressBar(self.MatchInputsGroupBox)
        self.progressBar.setFont(self.font(10, False, 50))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        #Error Test Box 
        self.ErrorTextLine = QtGui.QLineEdit(self.MatchInputsGroupBox)
        self.ErrorTextLine.setFont(self.font(10, False, 50))
        self.ErrorTextLine.setText("Error 1.242342")
        #Data Visualization Group Box Object
        self.DataVisualizationGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.DataVisualizationGroupBox.setFont(self.font(12, True, 75))
        #Create Graphs Objects
        self.graphicsViewLeft = QtGui.QGraphicsView(self.DataVisualizationGroupBox)
        self.graphicsViewRight = QtGui.QGraphicsView(self.DataVisualizationGroupBox)
        #Add graphics object to middle horizontal layout   
        self.DataSelectionGroupBoxLeft = QtGui.QGroupBox(self.dataTabLeft)
        self.DataSelectionGroupBoxLeft.setFont(self.font(12, True, 75))
        
        self.playerComboBoxLeft = QtGui.QComboBox(self.DataSelectionGroupBoxLeft)
        self.playerComboBoxLeft.setFont(self.font(10, False, 50))
        self.playerComboBoxLeft.addItem(_fromUtf8(""))
        self.playerComboBoxLeft.setItemText(0, _fromUtf8(""))
        self.playerComboBoxLeft.addItem(_fromUtf8(""))
        
        self.halfLabelLeft = QtGui.QLabel(self.DataSelectionGroupBoxLeft)
        self.halfLabelLeft.setFont(self.font(10, False, 50))
        
        self.teamComboBoxLeft = QtGui.QComboBox(self.DataSelectionGroupBoxLeft)
        self.teamComboBoxLeft.setFont(self.font(10, False, 50))
        self.teamComboBoxLeft.addItem(_fromUtf8(""))
        self.teamComboBoxLeft.setItemText(0, _fromUtf8(""))
        self.teamComboBoxLeft.addItem(_fromUtf8(""))

        self.matchLabelLeft = QtGui.QLabel(self.DataSelectionGroupBoxLeft)
        self.matchLabelLeft.setFont(self.font(10, False, 50))

        self.matchComboBoxLeft = QtGui.QComboBox(self.DataSelectionGroupBoxLeft)
        self.matchComboBoxLeft.setFont(self.font(10, False, 50))
        self.matchComboBoxLeft.addItem(_fromUtf8(""))
        self.matchComboBoxLeft.setItemText(0, _fromUtf8(""))
        self.matchComboBoxLeft.addItem(_fromUtf8(""))
        self.matchComboBoxLeft.addItem(_fromUtf8(""))
        
        self.findBtnLeft = QtGui.QPushButton(self.DataSelectionGroupBoxLeft)
        self.findBtnLeft.setFont(self.font(10, False, 50))
        
        self.teamLabelLeft = QtGui.QLabel(self.DataSelectionGroupBoxLeft)
        self.teamLabelLeft.setFont(self.font(10, False, 50))
        
        self.playerLabelLeft = QtGui.QLabel(self.DataSelectionGroupBoxLeft)
        self.playerLabelLeft.setFont(self.font(10, False, 50))

        self.halfComboBoxLeft = QtGui.QComboBox(self.DataSelectionGroupBoxLeft)
        self.halfComboBoxLeft.setFont(self.font(10, False, 50))
        self.halfComboBoxLeft.addItem(_fromUtf8(""))
        self.halfComboBoxLeft.setItemText(0, _fromUtf8(""))
        self.halfComboBoxLeft.addItem(_fromUtf8(""))
        self.halfComboBoxLeft.addItem(_fromUtf8(""))

        self.clearBtnLeft = QtGui.QPushButton(self.DataSelectionGroupBoxLeft)

        self.teamGroupBoxLeft = QtGui.QGroupBox(self.teamTabLeft)
        self.teamGroupBoxLeft.setFont(self.font(12, True, 75))
        
        self.teamNameLeft = QtGui.QLabel(self.teamGroupBoxLeft)
        self.teamNameLeft.setFont(self.font(14, False, 50))

        self.lineLeft = QtGui.QFrame(self.teamGroupBoxLeft)
        self.lineLeft.setFrameShape(QtGui.QFrame.HLine)
        self.lineLeft.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.winsLeft = QtGui.QLabel(self.teamGroupBoxLeft)
        self.winsLeft.setFont(self.font(10, False, 50))
        
        self.lossesLeft = QtGui.QLabel(self.teamGroupBoxLeft)
        self.lossesLeft.setFont(self.font(10, False, 50))

        self.wLRatioLeft = QtGui.QLabel(self.teamGroupBoxLeft)
        self.wLRatioLeft.setFont(self.font(10, False, 50))
        
        self.otherLeft = QtGui.QLabel(self.teamGroupBoxLeft)
        self.otherLeft.setFont(self.font(10, False, 50))

        self.dataVizTeamLeft_1 = QtGui.QPushButton(self.teamGroupBoxLeft)
        self.dataVizTeamLeft_1.setFont(self.font(10, False, 50))
        
        self.dataVizTeamLeft_2 = QtGui.QPushButton(self.teamGroupBoxLeft)
        self.dataVizTeamLeft_2.setFont(self.font(10, False, 50))

        self.dataVizTeamLeft_3 = QtGui.QPushButton(self.teamGroupBoxLeft)
        self.dataVizTeamLeft_3.setFont(self.font(10, False, 50))
        
        self.dataVizTeamLeft_4 = QtGui.QPushButton(self.teamGroupBoxLeft)
        self.dataVizTeamLeft_4.setFont(self.font(10, False, 50))

        self.PlayerGroupBoxLeft = QtGui.QGroupBox(self.playerTabLeft)
        self.PlayerGroupBoxLeft.setFont(self.font(12, True, 75))
        
        self.playerNameLabelLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
        self.playerNameLabelLeft.setFont(self.font(14, False, 50))

        self.lineLeft_2 = QtGui.QFrame(self.PlayerGroupBoxLeft)
        self.lineLeft_2.setFrameShape(QtGui.QFrame.HLine)
        self.lineLeft_2.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.killsLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
        self.killsLeft.setFont(self.font(10, False, 50))
        
        self.deathsLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
        self.deathsLeft.setFont(self.font(10, False, 50))
        
        self.assistsLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
        self.assistsLeft.setFont(self.font(10, False, 50))
        
        self.kDRatioLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
        self.kDRatioLeft.setFont(self.font(10, False, 50))
        
        self.isArcherLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
        self.isArcherLeft.setFont(self.font(10, False, 50))
        
        self.dataVizPlayerLeft_1 = QtGui.QPushButton(self.PlayerGroupBoxLeft)
        self.dataVizPlayerLeft_1.setFont(self.font(10, False, 50))
        
        self.dataVizPlayerLeft_2 = QtGui.QPushButton(self.PlayerGroupBoxLeft)
        self.dataVizPlayerLeft_2.setFont(self.font(10, False, 50))
        
        self.dataVizPlayerLeft_3 = QtGui.QPushButton(self.PlayerGroupBoxLeft)
        self.dataVizPlayerLeft_3.setFont(self.font(10, False, 50))
        
        self.dataVizPlayerLeft_4 = QtGui.QPushButton(self.PlayerGroupBoxLeft)
        self.dataVizPlayerLeft_4.setFont(self.font(10, False, 50))

        self.DataSelectionGroupBoxRight = QtGui.QGroupBox(self.dataTabRight)
        self.DataSelectionGroupBoxRight.setFont(self.font(12, True, 75))
        
        self.playerLabelRight = QtGui.QLabel(self.DataSelectionGroupBoxRight)
        self.playerLabelRight.setFont(self.font(10, False, 50))
        
        self.halfComboBoxRight = QtGui.QComboBox(self.DataSelectionGroupBoxRight)
        self.halfComboBoxRight.setFont(self.font(10, False, 50))
        self.halfComboBoxRight.addItem(_fromUtf8(""))
        self.halfComboBoxRight.setItemText(0, _fromUtf8(""))
        self.halfComboBoxRight.addItem(_fromUtf8(""))
        self.halfComboBoxRight.addItem(_fromUtf8(""))
        
        self.matchLabelRight = QtGui.QLabel(self.DataSelectionGroupBoxRight)
        self.matchLabelRight.setFont(self.font(10, False, 50))
        
        self.matchComboBoxRight = QtGui.QComboBox(self.DataSelectionGroupBoxRight)
        self.matchComboBoxRight.setFont(self.font(10, False, 50))
        self.matchComboBoxRight.addItem(_fromUtf8(""))
        self.matchComboBoxRight.setItemText(0, _fromUtf8(""))
        self.matchComboBoxRight.addItem(_fromUtf8(""))
        self.matchComboBoxRight.addItem(_fromUtf8(""))
        
        self.clearBtnRight = QtGui.QPushButton(self.DataSelectionGroupBoxRight)
        self.clearBtnRight.setFont(self.font(10, False, 50))
        
        self.findBtnRight = QtGui.QPushButton(self.DataSelectionGroupBoxRight)
        self.findBtnRight.setFont(self.font(10, False, 50))
        
        self.halfLabelRight = QtGui.QLabel(self.DataSelectionGroupBoxRight)
        self.halfLabelRight.setFont(self.font(10, False, 50))
        
        self.playerComboBoxRight = QtGui.QComboBox(self.DataSelectionGroupBoxRight)
        self.playerComboBoxRight.setFont(self.font(10, False, 50))
        self.playerComboBoxRight.addItem(_fromUtf8(""))
        self.playerComboBoxRight.setItemText(0, _fromUtf8(""))
        self.playerComboBoxRight.addItem(_fromUtf8(""))
        
        self.teamLabelRight = QtGui.QLabel(self.DataSelectionGroupBoxRight)
        self.teamLabelRight.setFont(self.font(10, False, 50))
        
        self.teamComboBoxRight = QtGui.QComboBox(self.DataSelectionGroupBoxRight)
        self.teamComboBoxRight.setFont(self.font(10, False, 50))
        self.teamComboBoxRight.addItem(_fromUtf8(""))
        self.teamComboBoxRight.setItemText(0, _fromUtf8(""))
        self.teamComboBoxRight.addItem(_fromUtf8(""))

        self.teamGroupBoxRight = QtGui.QGroupBox(self.teamTabRight)
        self.teamGroupBoxRight.setFont(self.font(12, True, 75))
        
        self.teamNameRight = QtGui.QLabel(self.teamGroupBoxRight)
        self.teamNameRight.setFont(self.font(14, False, 50))
        
        self.lineRight = QtGui.QFrame(self.teamGroupBoxRight)
        self.lineRight.setFrameShape(QtGui.QFrame.HLine)
        self.lineRight.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.winsRight = QtGui.QLabel(self.teamGroupBoxRight)
        self.winsRight.setFont(self.font(10, False, 50))
        
        self.lossesRight = QtGui.QLabel(self.teamGroupBoxRight)
        self.lossesRight.setFont(self.font(10, False, 50))
        
        self.wLRatioRight = QtGui.QLabel(self.teamGroupBoxRight)
        self.wLRatioRight.setFont(self.font(10, False, 50))
        
        self.otherRight = QtGui.QLabel(self.teamGroupBoxRight)
        self.otherRight.setFont(self.font(10, False, 50))
        
        self.dataVizTeamRight_1 = QtGui.QPushButton(self.teamGroupBoxRight)
        self.dataVizTeamRight_1.setFont(self.font(10, False, 50))
        
        self.dataVizTeamRight_2 = QtGui.QPushButton(self.teamGroupBoxRight)
        self.dataVizTeamRight_2.setFont(self.font(10, False, 50))
            
        self.dataVizTeamRight_3 = QtGui.QPushButton(self.teamGroupBoxRight)
        self.dataVizTeamRight_3.setFont(self.font(10, False, 50))
        
        self.dataVizTeamRight_4 = QtGui.QPushButton(self.teamGroupBoxRight)
        self.dataVizTeamRight_4.setFont(self.font(10, False, 50))

        self.PlayerGroupBoxRight = QtGui.QGroupBox(self.playerTabRight)
        self.PlayerGroupBoxRight.setFont(self.font(12, True, 75))
        
        self.playerNameLabelRight = QtGui.QLabel(self.PlayerGroupBoxRight)
        self.playerNameLabelRight.setFont(self.font(14, False, 50))

        self.lineRight_2 = QtGui.QFrame(self.PlayerGroupBoxRight)
        self.lineRight_2.setFrameShape(QtGui.QFrame.HLine)
        self.lineRight_2.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.killsRight = QtGui.QLabel(self.PlayerGroupBoxRight)
        self.killsRight.setFont(self.font(10, False, 50))
        
        self.deathsRight = QtGui.QLabel(self.PlayerGroupBoxRight)
        self.deathsRight.setFont(self.font(10, False, 50))
        
        self.assistsRight = QtGui.QLabel(self.PlayerGroupBoxRight)
        self.assistsRight.setFont(self.font(10, False, 50))
        
        self.kDRatioRight = QtGui.QLabel(self.PlayerGroupBoxRight)
        self.kDRatioRight.setFont(self.font(10, False, 50))
        
        self.isArcherRight = QtGui.QLabel(self.PlayerGroupBoxRight)
        self.isArcherRight.setFont(self.font(10, False, 50))
        
        self.dataVizPlayerRight_1 = QtGui.QPushButton(self.PlayerGroupBoxRight)
        self.dataVizPlayerRight_1.setFont(self.font(10, False, 50))
        
        self.dataVizPlayerRight_2 = QtGui.QPushButton(self.PlayerGroupBoxRight)
        self.dataVizPlayerRight_2.setFont(self.font(10, False, 50))
        
        self.dataVizPlayerRight_3 = QtGui.QPushButton(self.PlayerGroupBoxRight)
        self.dataVizPlayerRight_3.setFont(self.font(10, False, 50))
        
        self.dataVizPlayerRight_4 = QtGui.QPushButton(self.PlayerGroupBoxRight)
        self.dataVizPlayerRight_4.setFont(self.font(10, False, 50))
        #=======================================================================
        # 
        #=======================================================================
        self.horizontalLayout = QtGui.QHBoxLayout(self.DataVisualizationGroupBox)
        self.horizontalLayout.addWidget(self.graphicsViewLeft)
        self.horizontalLayout.addWidget(self.graphicsViewRight)
        
        self.horizontalLayoutTop = QtGui.QHBoxLayout(self.MatchInputsGroupBox)
        self.horizontalLayoutTop.addWidget(self.MatchNumberLabel)
        self.horizontalLayoutTop.addWidget(self.matchNumberSpinBox)
        self.horizontalLayoutTop.addWidget(self.CreateMatchPushBtn)
        self.horizontalLayoutTop.addWidget(self.ReloadDataPushBtn)
        self.horizontalLayoutTop.addWidget(self.progressBar)
        self.horizontalLayoutTop.addWidget(self.ErrorTextLine)
        
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.ContainerBottom)
        self.horizontalLayout_2.addWidget(self.tabsLeft)
        self.horizontalLayout_2.addWidget(self.tabsRight)
        
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)        
        self.gridLayout.addWidget(self.DataVisualizationGroupBox, 1, 0, 1, 1)        
        self.gridLayout.addWidget(self.ContainerBottom, 2, 0, 1, 1, QtCore.Qt.AlignBottom)        
        self.gridLayout.addWidget(self.MatchInputsGroupBox, 0, 0, 1, 1)
        
        self.gridLayout_3 = QtGui.QGridLayout(self.dataTabLeft)
        self.gridLayout_3.addWidget(self.DataSelectionGroupBoxLeft, 0, 0, 1, 1)
        
        self.gridLayout_4 = QtGui.QGridLayout(self.DataSelectionGroupBoxLeft)
        self.gridLayout_4.addWidget(self.playerComboBoxLeft, 7, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_4.addWidget(self.halfLabelLeft, 2, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_4.addWidget(self.teamComboBoxLeft, 5, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_4.addWidget(self.matchLabelLeft, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.matchComboBoxLeft, 1, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_4.addWidget(self.findBtnLeft, 8, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_4.addWidget(self.teamLabelLeft, 4, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_4.addWidget(self.playerLabelLeft, 6, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_4.addWidget(self.halfComboBoxLeft, 3, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_4.addWidget(self.clearBtnLeft, 9, 0, 1, 1, QtCore.Qt.AlignBottom)
        
        self.gridLayout_5 = QtGui.QGridLayout(self.teamGroupBoxLeft)
        self.gridLayout_5.addWidget(self.teamNameLeft, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.lineLeft, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.winsLeft, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.lossesLeft, 3, 0, 1, 1)
        self.gridLayout_5.addWidget(self.wLRatioLeft, 4, 0, 1, 1)
        self.gridLayout_5.addWidget(self.otherLeft, 5, 0, 1, 1)
        self.gridLayout_5.addWidget(self.dataVizTeamLeft_1, 6, 0, 1, 1)
        self.gridLayout_5.addWidget(self.dataVizTeamLeft_2, 7, 0, 1, 1)
        self.gridLayout_5.addWidget(self.dataVizTeamLeft_3, 8, 0, 1, 1)
        self.gridLayout_5.addWidget(self.dataVizTeamLeft_4, 9, 0, 1, 1)   
             
        self.gridLayout_6 = QtGui.QGridLayout(self.teamTabLeft)
        self.gridLayout_6.addWidget(self.teamGroupBoxLeft, 0, 0, 1, 1)
        
        self.gridLayout_7 = QtGui.QGridLayout(self.playerTabLeft)
        self.gridLayout_7.addWidget(self.PlayerGroupBoxLeft, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        
        self.gridLayout_8 = QtGui.QGridLayout(self.DataSelectionGroupBoxRight)
        self.gridLayout_8.addWidget(self.playerLabelRight, 7, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_8.addWidget(self.halfComboBoxRight, 3, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_8.addWidget(self.matchLabelRight, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.matchComboBoxRight, 1, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_8.addWidget(self.clearBtnRight, 10, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_8.addWidget(self.findBtnRight, 9, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_8.addWidget(self.halfLabelRight, 2, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_8.addWidget(self.playerComboBoxRight, 8, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_8.addWidget(self.teamLabelRight, 4, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_8.addWidget(self.teamComboBoxRight, 5, 0, 1, 1)
        
        self.gridLayout_9 = QtGui.QGridLayout(self.dataTabRight)
        self.gridLayout_9.addWidget(self.DataSelectionGroupBoxRight, 0, 0, 1, 1)
        
        self.gridLayout_10 = QtGui.QGridLayout(self.teamGroupBoxRight)
        self.gridLayout_10.addWidget(self.teamNameRight, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.lineRight, 1, 0, 1, 1)
        self.gridLayout_10.addWidget(self.winsRight, 2, 0, 1, 1)
        self.gridLayout_10.addWidget(self.lossesRight, 3, 0, 1, 1)
        self.gridLayout_10.addWidget(self.wLRatioRight, 4, 0, 1, 1)
        self.gridLayout_10.addWidget(self.otherRight, 5, 0, 1, 1)
        self.gridLayout_10.addWidget(self.dataVizTeamRight_1, 6, 0, 1, 1)
        self.gridLayout_10.addWidget(self.dataVizTeamRight_2, 7, 0, 1, 1)
        self.gridLayout_10.addWidget(self.dataVizTeamRight_3, 8, 0, 1, 1)
        self.gridLayout_10.addWidget(self.dataVizTeamRight_4, 9, 0, 1, 1)
        
        self.gridLayout_11 = QtGui.QGridLayout(self.teamTabRight)
        self.gridLayout_11.addWidget(self.teamGroupBoxRight, 0, 0, 1, 1)
        
        self.gridLayout_13 = QtGui.QGridLayout(self.playerTabRight)
        self.gridLayout_13.addWidget(self.PlayerGroupBoxRight, 0, 0, 1, 1)
                
        self.verticalLayout = QtGui.QVBoxLayout(self.PlayerGroupBoxLeft)
        self.verticalLayout.addWidget(self.playerNameLabelLeft)
        self.verticalLayout.addWidget(self.lineLeft_2)
        self.verticalLayout.addWidget(self.killsLeft, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.deathsLeft, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.assistsLeft, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.kDRatioLeft, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.isArcherLeft, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.dataVizPlayerLeft_1)
        self.verticalLayout.addWidget(self.dataVizPlayerLeft_2)
        self.verticalLayout.addWidget(self.dataVizPlayerLeft_3)
        self.verticalLayout.addWidget(self.dataVizPlayerLeft_4)
        
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.PlayerGroupBoxRight)
        self.verticalLayout_2.addWidget(self.playerNameLabelRight)
        self.verticalLayout_2.addWidget(self.lineRight_2)
        self.verticalLayout_2.addWidget(self.killsRight, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.deathsRight, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.assistsRight, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.kDRatioRight, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.isArcherRight, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.dataVizPlayerRight_1)
        self.verticalLayout_2.addWidget(self.dataVizPlayerRight_2)
        self.verticalLayout_2.addWidget(self.dataVizPlayerRight_3)
        self.verticalLayout_2.addWidget(self.dataVizPlayerRight_4)
        
        self.tabsLeft.setCurrentIndex(0)
        self.tabsRight.setCurrentIndex(0)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
                
        self.retranslateUi(MainWindow)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Harambe\'s Chivalry Data Cruncher", None))
        self.MatchInputsGroupBox.setTitle(_translate("MainWindow", "Match Inputs", None))
        self.MatchNumberLabel.setText(_translate("MainWindow", "Match Number", None))
        self.CreateMatchPushBtn.setText(_translate("MainWindow", "Create Match", None))
        self.ReloadDataPushBtn.setText(_translate("MainWindow", "Reload Data", None))
        self.DataVisualizationGroupBox.setTitle(_translate("MainWindow", "Data Visualization", None))
        self.DataSelectionGroupBoxLeft.setTitle(_translate("MainWindow", "Data Selection", None))
        self.playerComboBoxLeft.setItemText(1, _translate("MainWindow", "Crimson King", None))
        self.halfLabelLeft.setText(_translate("MainWindow", "Half", None))
        self.teamComboBoxLeft.setItemText(1, _translate("MainWindow", "Harambe", None))
        self.matchLabelLeft.setText(_translate("MainWindow", "Match", None))
        self.matchComboBoxLeft.setItemText(1, _translate("MainWindow", "Number One", None))
        self.matchComboBoxLeft.setItemText(2, _translate("MainWindow", "Number Two", None))
        self.findBtnLeft.setText(_translate("MainWindow", "Find", None))
        self.teamLabelLeft.setText(_translate("MainWindow", "Team", None))
        self.playerLabelLeft.setText(_translate("MainWindow", "Player", None))
        self.halfComboBoxLeft.setItemText(1, _translate("MainWindow", "Number One", None))
        self.halfComboBoxLeft.setItemText(2, _translate("MainWindow", "Number Two", None))
        self.clearBtnLeft.setText(_translate("MainWindow", "Clear", None))
        self.tabsLeft.setTabText(self.tabsLeft.indexOf(self.dataTabLeft), _translate("MainWindow", "Data Selection", None))
        self.teamGroupBoxLeft.setTitle(_translate("MainWindow", "Team", None))
        self.teamNameLeft.setText(_translate("MainWindow", "Accolade", None))
        self.winsLeft.setText(_translate("MainWindow", "Wins: ", None))
        self.lossesLeft.setText(_translate("MainWindow", "Losses:", None))
        self.wLRatioLeft.setText(_translate("MainWindow", "Win Loss Ratio :", None))
        self.otherLeft.setText(_translate("MainWindow", "Other :", None))
        self.dataVizTeamLeft_1.setText(_translate("MainWindow", "Data Viz ", None))
        self.dataVizTeamLeft_2.setText(_translate("MainWindow", "Data Viz ", None))
        self.dataVizTeamLeft_3.setText(_translate("MainWindow", "Data Viz ", None))
        self.dataVizTeamLeft_4.setText(_translate("MainWindow", "Data Viz ", None))
        self.tabsLeft.setTabText(self.tabsLeft.indexOf(self.teamTabLeft), _translate("MainWindow", "Team", None))
        self.PlayerGroupBoxLeft.setTitle(_translate("MainWindow", "Player", None))
        self.playerNameLabelLeft.setText(_translate("MainWindow", "Crimson King", None))
        self.killsLeft.setText(_translate("MainWindow", "Kills:", None))
        self.deathsLeft.setText(_translate("MainWindow", "Deaths:", None))
        self.assistsLeft.setText(_translate("MainWindow", "Assists:", None))
        self.kDRatioLeft.setText(_translate("MainWindow", "K/D Ratio:", None))
        self.isArcherLeft.setText(_translate("MainWindow", "Is Archer:", None))
        self.dataVizPlayerLeft_1.setText(_translate("MainWindow", "Data Viz ", None))
        self.dataVizPlayerLeft_2.setText(_translate("MainWindow", "Data Viz ", None))
        self.dataVizPlayerLeft_3.setText(_translate("MainWindow", "Data Viz ", None))
        self.dataVizPlayerLeft_4.setText(_translate("MainWindow", "Data Viz ", None))
        self.tabsLeft.setTabText(self.tabsLeft.indexOf(self.playerTabLeft), _translate("MainWindow", "Player", None))
        self.DataSelectionGroupBoxRight.setTitle(_translate("MainWindow", "Data Selection", None))
        self.playerLabelRight.setText(_translate("MainWindow", "Player", None))
        self.halfComboBoxRight.setItemText(1, _translate("MainWindow", "Number One", None))
        self.halfComboBoxRight.setItemText(2, _translate("MainWindow", "Number Two", None))
        self.matchLabelRight.setText(_translate("MainWindow", "Match", None))
        self.matchComboBoxRight.setItemText(1, _translate("MainWindow", "Number One", None))
        self.matchComboBoxRight.setItemText(2, _translate("MainWindow", "Number Two", None))
        self.clearBtnRight.setText(_translate("MainWindow", "Clear", None))
        self.findBtnRight.setText(_translate("MainWindow", "Find", None))
        self.halfLabelRight.setText(_translate("MainWindow", "Half", None))
        self.playerComboBoxRight.setItemText(1, _translate("MainWindow", "Crimson King", None))
        self.teamLabelRight.setText(_translate("MainWindow", "Team", None))
        self.teamComboBoxRight.setItemText(1, _translate("MainWindow", "Harambe", None))
        self.tabsRight.setTabText(self.tabsRight.indexOf(self.dataTabRight), _translate("MainWindow", "Data Selection", None))
        self.teamGroupBoxRight.setTitle(_translate("MainWindow", "Team", None))
        self.teamNameRight.setText(_translate("MainWindow", "Accolade", None))
        self.winsRight.setText(_translate("MainWindow", "Wins: ", None))
        self.lossesRight.setText(_translate("MainWindow", "Losses:", None))
        self.wLRatioRight.setText(_translate("MainWindow", "Win Loss Ratio :", None))
        self.otherRight.setText(_translate("MainWindow", "Other :", None))
        self.dataVizTeamRight_1.setText(_translate("MainWindow", "Data Viz ", None))
        self.dataVizTeamRight_2.setText(_translate("MainWindow", "Data Viz ", None))
        self.dataVizTeamRight_3.setText(_translate("MainWindow", "Data Viz ", None))
        self.dataVizTeamRight_4.setText(_translate("MainWindow", "Data Viz ", None))
        self.tabsRight.setTabText(self.tabsRight.indexOf(self.teamTabRight), _translate("MainWindow", "Team", None))
        self.PlayerGroupBoxRight.setTitle(_translate("MainWindow", "Player", None))
        self.playerNameLabelRight.setText(_translate("MainWindow", "Crimson King", None))
        self.killsRight.setText(_translate("MainWindow", "Kills:", None))
        self.deathsRight.setText(_translate("MainWindow", "Deaths:", None))
        self.assistsRight.setText(_translate("MainWindow", "Assists:", None))
        self.kDRatioRight.setText(_translate("MainWindow", "K/D Ratio:", None))
        self.isArcherRight.setText(_translate("MainWindow", "Is Archer:", None))
        self.dataVizPlayerRight_1.setText(_translate("MainWindow", "Data Viz ", None))
        self.dataVizPlayerRight_2.setText(_translate("MainWindow", "Data Viz ", None))
        self.dataVizPlayerRight_3.setText(_translate("MainWindow", "Data Viz ", None))
        self.dataVizPlayerRight_4.setText(_translate("MainWindow", "Data Viz ", None))
        self.tabsRight.setTabText(self.tabsRight.indexOf(self.playerTabRight), _translate("MainWindow", "Player", None))
    def font(self, fontSize, Bold, Weight):
        font = QtGui.QFont()
        font.setPointSize(fontSize)
        font.setBold(Bold)
        font.setWeight(Weight)
        return font
def run():
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

    