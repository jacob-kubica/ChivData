'''
Created on Aug 15, 2016

@author: Jacob
'''
from PyQt4 import QtCore, QtGui
from test.test_iterlen import NoneLengthHint
class Ui_MainWindow():
    def __init__(self, Directory):
        self.Directory = Directory
        #self.methods.printShit()
        self.matchRight = None
        self.halfRight = None
        self.teamRight =  None
        self.playerRight = None
        
        self.matchLeft = None
        self.halfLeft = None
        self.teamLeft =  None
        self.playerLeft = None
    def setupUi(self, MainWindow):
        '''
        Set up gui window
        '''
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Harambe\'s Chivalry Data Cruncher")
        MainWindow.resize(1084, 813)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #=======================================================================
        # Handles Creation of 3 sub sections and adds them to a grid layout
        #=======================================================================
        self.MatchInputs()
        self.DataVisualization()
        self.Tabs()
        self.teamComboBoxRightfill()
        self.teamComboBoxLeftfill()
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)        
        self.gridLayout.addWidget(self.DataVisualizationGroupBox, 1, 0, 1, 1)        
        self.gridLayout.addWidget(self.ContainerBottom, 2, 0, 1, 1, QtCore.Qt.AlignBottom)        
        self.gridLayout.addWidget(self.MatchInputsGroupBox, 0, 0, 1, 1)
    def MatchInputs(self):
        '''
        Fills Top Subsection with necessary objects
        '''
        #Match Inputs Group Box
        self.MatchInputsGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.MatchInputsGroupBox.setFont(self.font(12, True, 75))
        self.MatchInputsGroupBox.setTitle("Match Inputs")
        #Label 'Match Count'
        self.MatchNumberLabel = QtGui.QLabel(self.MatchInputsGroupBox)
        self.MatchNumberLabel.setFont(self.font(10, False, 50))
        self.MatchNumberLabel.setText("Match Count")
        #Match SpinBox
        self.matchNumberSpinBox = QtGui.QSpinBox(self.MatchInputsGroupBox)
        self.matchNumberSpinBox.setFont(self.font(10, False, 50))
        #Create Match Push Button
        self.CreateMatchPushBtn = QtGui.QPushButton(self.MatchInputsGroupBox)
        self.CreateMatchPushBtn.clicked.connect(self.matchCreate)
        self.CreateMatchPushBtn.setFont(self.font(10, False, 50))
        self.CreateMatchPushBtn.setText("Create Match")
        #Reload Push Button
        self.ReloadDataPushBtn = QtGui.QPushButton(self.MatchInputsGroupBox)
        self.ReloadDataPushBtn.clicked.connect(self.matchReload)
        self.ReloadDataPushBtn.setFont(self.font(10, False, 50))
        self.ReloadDataPushBtn.setText("Reload Data")
        #Progress Bar
        self.progressBar = QtGui.QProgressBar(self.MatchInputsGroupBox)
        self.progressBar.setFont(self.font(10, False, 50))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        #Error Line Text Line
        self.ErrorTextLine = QtGui.QLineEdit(self.MatchInputsGroupBox)
        self.ErrorTextLine.setFont(self.font(10, False, 50))
        self.ErrorTextLine.setText("")
        #Layout
        self.horizontalLayoutTop = QtGui.QHBoxLayout(self.MatchInputsGroupBox)
        self.horizontalLayoutTop.addWidget(self.MatchNumberLabel)
        self.horizontalLayoutTop.addWidget(self.matchNumberSpinBox)
        self.horizontalLayoutTop.addWidget(self.CreateMatchPushBtn)
        self.horizontalLayoutTop.addWidget(self.ReloadDataPushBtn)
        self.horizontalLayoutTop.addWidget(self.progressBar)
        self.horizontalLayoutTop.addWidget(self.ErrorTextLine)
    def DataVisualization(self):
        '''
        Fills middle section with necessary objects
        '''
        #Data Visualization Group Box
        self.DataVisualizationGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.DataVisualizationGroupBox.setFont(self.font(12, True, 75))
        self.DataVisualizationGroupBox.setTitle("Data Visualization")
        #Graphic View Left
        self.graphicsViewLeft = QtGui.QGraphicsView(self.DataVisualizationGroupBox)
        #Graphic View Right
        self.graphicsViewRight = QtGui.QGraphicsView(self.DataVisualizationGroupBox)
        #Layout
        self.horizontalLayout = QtGui.QHBoxLayout(self.DataVisualizationGroupBox)
        self.horizontalLayout.addWidget(self.graphicsViewLeft)
        self.horizontalLayout.addWidget(self.graphicsViewRight)
    def Tabs(self):
        '''
        Container for tab methods
        '''
        self.ContainerBottom = QtGui.QWidget(self.centralwidget)
        def TabsLeft():
            '''
            Contains Left Tabs
            '''
            def dataTabLeft():
                '''
                Contains objects in the data selection group box
                '''
                def DataSelectionGroupBoxLeft():
                    '''
                    Container Function
                    '''
                    #Data Selection Group Box
                    self.DataSelectionGroupBoxLeft = QtGui.QGroupBox(self.dataTabLeft)
                    self.DataSelectionGroupBoxLeft.setFont(self.font(12, True, 75))
                    self.DataSelectionGroupBoxLeft.setTitle("Data Selection")
                    #Label "Match"
                    self.matchLabelLeft = QtGui.QLabel(self.DataSelectionGroupBoxLeft)
                    self.matchLabelLeft.setFont(self.font(10, False, 50))
                    self.matchLabelLeft.setText("Match")
                    #Match Combo Box
                    self.matchComboBoxLeft = QtGui.QComboBox(self.DataSelectionGroupBoxLeft)
                    self.matchComboBoxLeft.setFont(self.font(10, False, 50))
                    self.matchComboBoxLeft.addItem("-")
                    self.matchComboBoxLeft.activated[str].connect(self.matchSelectLeft)               
                    #Label "Half"
                    self.halfLabelLeft = QtGui.QLabel(self.DataSelectionGroupBoxLeft)
                    self.halfLabelLeft.setFont(self.font(10, False, 50))
                    self.halfLabelLeft.setText("Half")
                    #Half Combo Box
                    self.halfComboBoxLeft = QtGui.QComboBox(self.DataSelectionGroupBoxLeft)
                    self.halfComboBoxLeft.setFont(self.font(10, False, 50))
                    self.halfComboBoxLeft.addItem("-")
                    self.halfComboBoxLeft.addItem("Number One")
                    self.halfComboBoxLeft.addItem("Number Two")
                    self.halfComboBoxLeft.activated[str].connect(self.halfSelectLeft)               
                    #Label "Team"
                    self.teamLabelLeft = QtGui.QLabel(self.DataSelectionGroupBoxLeft)
                    self.teamLabelLeft.setFont(self.font(10, False, 50))
                    self.teamLabelLeft.setText("Team")
                    #Team Combo Box
                    self.teamComboBoxLeft = QtGui.QComboBox(self.DataSelectionGroupBoxLeft)
                    self.teamComboBoxLeft.setFont(self.font(10, False, 50))
                    self.teamComboBoxLeft.addItem("-")
                    self.teamComboBoxLeft.activated[str].connect(self.teamSelectLeft)
                    #Label "Player"
                    self.playerLabelLeft = QtGui.QLabel(self.DataSelectionGroupBoxLeft)
                    self.playerLabelLeft.setFont(self.font(10, False, 50))
                    self.playerLabelLeft.setText("Player")
                    #Player Combo Box
                    self.playerComboBoxLeft = QtGui.QComboBox(self.DataSelectionGroupBoxLeft)
                    self.playerComboBoxLeft.setFont(self.font(10, False, 50))
                    self.playerComboBoxLeft.addItem("-")
                    self.playerComboBoxLeft.activated[str].connect(self.playerSelectLeft)
                    #Find Button
                    self.findBtnLeft = QtGui.QPushButton(self.DataSelectionGroupBoxLeft)
                    self.findBtnLeft.setFont(self.font(10, False, 50))
                    self.findBtnLeft.setText("Find")
                    self.findBtnLeft.clicked.connect(self.findLeft)
                    #Clear Button
                    self.clearBtnLeft = QtGui.QPushButton(self.DataSelectionGroupBoxLeft)
                    self.clearBtnLeft.setFont(self.font(10, False, 50))
                    self.clearBtnLeft.setText("Clear")    
                    self.clearBtnLeft.clicked.connect(self.clearValueLeft)                
                    #Layout
                    self.DataSelectionGroupBoxLeftGrid = QtGui.QGridLayout(self.DataSelectionGroupBoxLeft)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.matchLabelLeft, 0, 0, 1, 1)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.matchComboBoxLeft, 1, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.halfLabelLeft, 2, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.halfComboBoxLeft, 3, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.teamLabelLeft, 4, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.teamComboBoxLeft, 5, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.playerLabelLeft, 6, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.playerComboBoxLeft, 7, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.findBtnLeft, 8, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxLeftGrid.addWidget(self.clearBtnLeft, 9, 0, 1, 1, QtCore.Qt.AlignBottom)
                self.dataTabLeft = QtGui.QWidget()
                DataSelectionGroupBoxLeft()
                self.dataTabLeftGrid = QtGui.QGridLayout(self.dataTabLeft)            
                self.dataTabLeftGrid.addWidget(self.DataSelectionGroupBoxLeft, 0, 0, 1, 1)
                self.tabsLeft.addTab(self.dataTabLeft, "Data Selection")
            def teamTabLeft():
                def teamGroupBoxLeft():
                    #Team Group Box
                    self.teamGroupBoxLeft = QtGui.QGroupBox(self.teamTabLeft)
                    self.teamGroupBoxLeft.setFont(self.font(12, True, 75))
                    self.teamGroupBoxLeft.setTitle("Team")
                    #Team Label
                    self.teamNameLeft = QtGui.QLabel(self.teamGroupBoxLeft)
                    self.teamNameLeft.setFont(self.font(14, False, 50))
                    self.teamNameLeft.setText("")
                    #Line
                    self.lineLeft = QtGui.QFrame(self.teamGroupBoxLeft)
                    self.lineLeft.setFrameShape(QtGui.QFrame.HLine)
                    self.lineLeft.setFrameShadow(QtGui.QFrame.Sunken)
                    #Wins Label
                    self.winsLeft = QtGui.QLabel(self.teamGroupBoxLeft)
                    self.winsLeft.setFont(self.font(10, False, 50))
                    self.winsLeft.setText("Wins:")
                    #Losses Label
                    self.lossesLeft = QtGui.QLabel(self.teamGroupBoxLeft)
                    self.lossesLeft.setFont(self.font(10, False, 50))
                    self.lossesLeft.setText("Losses:")
                    #Win Loss Ration Label
                    self.wLRatioLeft = QtGui.QLabel(self.teamGroupBoxLeft)
                    self.wLRatioLeft.setFont(self.font(10, False, 50))
                    self.wLRatioLeft.setText("Win/Loss Ratio:")
                    #Other Label
                    self.tKDRatioLeft = QtGui.QLabel(self.teamGroupBoxLeft)
                    self.tKDRatioLeft.setFont(self.font(10, False, 50))
                    self.tKDRatioLeft.setText("Total Kill/Death Ratio:")
                    #Data Visualization Button
                    self.dataVizTeamLeft_1 = QtGui.QPushButton(self.teamGroupBoxLeft)
                    self.dataVizTeamLeft_1.setFont(self.font(10, False, 50))
                    self.dataVizTeamLeft_1.setText("Team Kill/Death Ratio Match by Match")
                    #Data Visualization Button
                    self.dataVizTeamLeft_2 = QtGui.QPushButton(self.teamGroupBoxLeft)
                    self.dataVizTeamLeft_2.setFont(self.font(10, False, 50))
                    self.dataVizTeamLeft_2.setText("Player Combat Score Ratios")
                    #Data Visualization Button
                    '''
                    self.dataVizTeamLeft_3 = QtGui.QPushButton(self.teamGroupBoxLeft)
                    self.dataVizTeamLeft_3.setFont(self.font(10, False, 50))
                    self.dataVizTeamLeft_3.setText("Data Viz ")
                    '''
                    #Data Visualization Button
                    '''
                    self.dataVizTeamLeft_4 = QtGui.QPushButton(self.teamGroupBoxLeft)
                    self.dataVizTeamLeft_4.setFont(self.font(10, False, 50))
                    self.dataVizTeamLeft_4.setText("Data Viz ")
                    '''
                    #Layout
                    self.teamGroupBoxLeftGrid = QtGui.QGridLayout(self.teamGroupBoxLeft)
                    self.teamGroupBoxLeftGrid.addWidget(self.teamNameLeft, 0, 0, 1, 1)
                    self.teamGroupBoxLeftGrid.addWidget(self.lineLeft, 1, 0, 1, 1)
                    self.teamGroupBoxLeftGrid.addWidget(self.winsLeft, 2, 0, 1, 1)
                    self.teamGroupBoxLeftGrid.addWidget(self.lossesLeft, 3, 0, 1, 1)
                    self.teamGroupBoxLeftGrid.addWidget(self.wLRatioLeft, 4, 0, 1, 1)
                    self.teamGroupBoxLeftGrid.addWidget(self.tKDRatioLeft, 5, 0, 1, 1)
                    self.teamGroupBoxLeftGrid.addWidget(self.dataVizTeamLeft_1, 6, 0, 1, 1)
                    self.teamGroupBoxLeftGrid.addWidget(self.dataVizTeamLeft_2, 7, 0, 1, 1)
                    #self.teamGroupBoxLeftGrid.addWidget(self.dataVizTeamLeft_3, 8, 0, 1, 1)
                    #self.teamGroupBoxLeftGrid.addWidget(self.dataVizTeamLeft_4, 9, 0, 1, 1)
                self.teamTabLeft = QtGui.QWidget()
                teamGroupBoxLeft()
                self.teamTabLeftGrid = QtGui.QGridLayout(self.teamTabLeft)
                self.teamTabLeftGrid.addWidget(self.teamGroupBoxLeft, 0, 0, 1, 1)
                self.tabsLeft.addTab(self.teamTabLeft, "Team")
            def playerTabLeft():
                def PlayerGroupBoxLeft():
                    #Player Group Box
                    self.PlayerGroupBoxLeft = QtGui.QGroupBox(self.playerTabLeft)
                    self.PlayerGroupBoxLeft.setFont(self.font(12, True, 75))
                    self.PlayerGroupBoxLeft.setTitle("Player")
                    #Player Label
                    self.playerNameLabelLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
                    self.playerNameLabelLeft.setFont(self.font(14, False, 50))
                    self.playerNameLabelLeft.setText("")
                    #Line
                    self.lineLeft_2 = QtGui.QFrame(self.PlayerGroupBoxLeft)
                    self.lineLeft_2.setFrameShape(QtGui.QFrame.HLine)
                    self.lineLeft_2.setFrameShadow(QtGui.QFrame.Sunken)
                    #Kills Label
                    self.killsLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
                    self.killsLeft.setFont(self.font(10, False, 50))
                    self.killsLeft.setText("Kills:")
                    #Deaths Label
                    self.deathsLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
                    self.deathsLeft.setFont(self.font(10, False, 50))
                    self.deathsLeft.setText("Deaths:")
                    #Assists Label
                    self.assistsLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
                    self.assistsLeft.setFont(self.font(10, False, 50))
                    self.assistsLeft.setText("Assists:")
                    #Kill Death Ratio Label
                    self.kDRatioLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
                    self.kDRatioLeft.setFont(self.font(10, False, 50))
                    self.kDRatioLeft.setText("Kill/Death Ratio:")
                    #Combat Score/Death ratio
                    self.cSDRatioLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
                    self.cSDRatioLeft.setFont(self.font(10, False, 50))
                    self.cSDRatioLeft.setText("Combat Score/Death Ratio:")
                    #Combat Score/Death ratio relative
                    self.cSDRatioRealtiveLeft = QtGui.QLabel(self.PlayerGroupBoxLeft)
                    self.cSDRatioRealtiveLeft.setFont(self.font(10, False, 50))
                    self.cSDRatioRealtiveLeft.setText("Combat Score/Death Ratio Relative:")
                    #Data Visualization Button
                    self.dataVizPlayerLeft_1 = QtGui.QPushButton(self.PlayerGroupBoxLeft)
                    self.dataVizPlayerLeft_1.setFont(self.font(10, False, 50))
                    self.dataVizPlayerLeft_1.setText("Combat Score/Death Ratio Match by Match")
                    #Data Visualization Button
                    self.dataVizPlayerLeft_2 = QtGui.QPushButton(self.PlayerGroupBoxLeft)
                    self.dataVizPlayerLeft_2.setFont(self.font(10, False, 50))
                    self.dataVizPlayerLeft_2.setText("Combat Score/Death Ratio Relative Match by Match")
                    #Data Visualization Button
                    '''
                    self.dataVizPlayerLeft_3 = QtGui.QPushButton(self.PlayerGroupBoxLeft)
                    self.dataVizPlayerLeft_3.setFont(self.font(10, False, 50))
                    self.dataVizPlayerLeft_3.setText("Combat Score/Death Ratio Relative Match by Match")
                    '''
                    #Data Visualization Button
                    '''
                    self.dataVizPlayerLeft_4 = QtGui.QPushButton(self.PlayerGroupBoxLeft)
                    self.dataVizPlayerLeft_4.setFont(self.font(10, False, 50))
                    self.dataVizPlayerLeft_4.setText("Data Viz ")
                    '''
                    #Layouts
                    self.PlayerGroupBoxLeftGrid = QtGui.QVBoxLayout(self.PlayerGroupBoxLeft)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.playerNameLabelLeft)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.lineLeft_2)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.killsLeft)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.deathsLeft)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.assistsLeft)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.kDRatioLeft)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.cSDRatioLeft)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.cSDRatioRealtiveLeft)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.dataVizPlayerLeft_1)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.dataVizPlayerLeft_2)
                    '''
                    self.PlayerGroupBoxLeftGrid.addWidget(self.dataVizPlayerLeft_3)
                    self.PlayerGroupBoxLeftGrid.addWidget(self.dataVizPlayerLeft_4)
                    '''
                self.playerTabLeft = QtGui.QWidget()
                PlayerGroupBoxLeft()
                self.playerTabLeftGrid = QtGui.QGridLayout(self.playerTabLeft)
                self.playerTabLeftGrid.addWidget(self.PlayerGroupBoxLeft, 0, 0, 1, 1)
                self.tabsLeft.addTab(self.playerTabLeft, "")
                self.tabsLeft.setTabText(self.tabsLeft.indexOf(self.playerTabLeft), "Player")
            def tournamentLeft():
                def TournamentGroupBoxLeft():
                    #Tournament Group Box
                    self.TournamentGroupBoxLeft = QtGui.QGroupBox(self.tournamentLeft)
                    self.TournamentGroupBoxLeft.setFont(self.font(12, True, 75)) 
                    self.TournamentGroupBoxLeft.setTitle("Tournament")
                    #Tournament Button
                    self.tournamentBtnLeft_1 = QtGui.QPushButton(self.TournamentGroupBoxLeft)
                    self.tournamentBtnLeft_1.setFont(self.font(10, False, 50)) 
                    self.tournamentBtnLeft_1.setText("Top Teams Kills/Death Ratio")      
                    #Tournament Button 
                    self.tournamentBtnLeft_2 = QtGui.QPushButton(self.TournamentGroupBoxLeft)
                    self.tournamentBtnLeft_2.setFont(self.font(10, False, 50)) 
                    self.tournamentBtnLeft_2.setText("Top Archers Combat Score/Death Ratio")  
                    #Tournament Button   
                    self.tournamentBtnLeft_3 = QtGui.QPushButton(self.TournamentGroupBoxLeft)
                    self.tournamentBtnLeft_3.setFont(self.font(10, False, 50))   
                    self.tournamentBtnLeft_3.setText("Top Players Combat Score/Death Ratio") 
                    #Tournament Button
                    self.tournamentBtnLeft_4 = QtGui.QPushButton(self.TournamentGroupBoxLeft)
                    self.tournamentBtnLeft_4.setFont(self.font(10, False, 50)) 
                    self.tournamentBtnLeft_4.setText("Top Players Combat Score/Death Ratio Relative")   
                    #Tournament Button   
                    self.tournamentBtnLeft_5 = QtGui.QPushButton(self.TournamentGroupBoxLeft)
                    self.tournamentBtnLeft_5.setFont(self.font(10, False, 50))
                    self.tournamentBtnLeft_5.setText("Bottom Players Combat Score/Death Ratio")  
                    #Tournament Button 
                    self.tournamentBtnLeft_6 = QtGui.QPushButton(self.TournamentGroupBoxLeft)
                    self.tournamentBtnLeft_6.setFont(self.font(10, False, 50))
                    self.tournamentBtnLeft_6.setText("Bottom Players Combat Score/Death Ratio Relative")  
                    #Tournament Button
                    self.tournamentBtnLeft_7 = QtGui.QPushButton(self.TournamentGroupBoxLeft)
                    self.tournamentBtnLeft_7.setFont(self.font(10, False, 50))
                    self.tournamentBtnLeft_7.setText("Top Teams Win/Loss Ratio")  
                    #Layout
                    self.TournamentGroupBoxLeftGrid = QtGui.QGridLayout(self.TournamentGroupBoxLeft)
                    self.TournamentGroupBoxLeftGrid.addWidget(self.tournamentBtnLeft_1, 0, 0, 1, 1)
                    self.TournamentGroupBoxLeftGrid.addWidget(self.tournamentBtnLeft_2, 1, 0, 1, 1)
                    self.TournamentGroupBoxLeftGrid.addWidget(self.tournamentBtnLeft_3, 2, 0, 1, 1)
                    self.TournamentGroupBoxLeftGrid.addWidget(self.tournamentBtnLeft_4, 3, 0, 1, 1)
                    self.TournamentGroupBoxLeftGrid.addWidget(self.tournamentBtnLeft_5, 4, 0, 1, 1)
                    self.TournamentGroupBoxLeftGrid.addWidget(self.tournamentBtnLeft_6, 5, 0, 1, 1)
                    self.TournamentGroupBoxLeftGrid.addWidget(self.tournamentBtnLeft_7, 6, 0, 1, 1)
                self.tournamentLeft = QtGui.QWidget()
                TournamentGroupBoxLeft()
                self.tournamentLeftGrid = QtGui.QGridLayout(self.tournamentLeft)
                self.tournamentLeftGrid.addWidget(self.TournamentGroupBoxLeft, 0, 0, 1, 1)
                self.tabsLeft.addTab(self.tournamentLeft, "")
                self.tabsLeft.setTabText(self.tabsLeft.indexOf(self.tournamentLeft), "Tournament")
            self.tabsLeft = QtGui.QTabWidget(self.ContainerBottom)
            dataTabLeft()
            teamTabLeft()
            playerTabLeft()
            tournamentLeft()
            self.tabsLeft.setCurrentIndex(0)
        def TabsRight():
            self.tabsRight = QtGui.QTabWidget(self.ContainerBottom) 
            def dataTabRight():
                def DataSelectionGroupBoxRight():
                    #Data Selection Group Box
                    self.DataSelectionGroupBoxRight = QtGui.QGroupBox(self.dataTabRight)
                    self.DataSelectionGroupBoxRight.setFont(self.font(12, True, 75))
                    self.DataSelectionGroupBoxRight.setTitle("Data Selection")
                    #Match Label
                    self.matchLabelRight = QtGui.QLabel(self.DataSelectionGroupBoxRight)
                    self.matchLabelRight.setFont(self.font(10, False, 50))
                    self.matchLabelRight.setText("Match")
                    #Match Combo Box
                    self.matchComboBoxRight = QtGui.QComboBox(self.DataSelectionGroupBoxRight)
                    self.matchComboBoxRight.setFont(self.font(10, False, 50))
                    self.matchComboBoxRight.addItem("-")
                    self.matchComboBoxRight.activated[str].connect(self.matchSelectRight)
                    #Half Label
                    self.halfLabelRight = QtGui.QLabel(self.DataSelectionGroupBoxRight)
                    self.halfLabelRight.setFont(self.font(10, False, 50))
                    self.halfLabelRight.setText("Half")
                    #Half Combo Box
                    self.halfComboBoxRight = QtGui.QComboBox(self.DataSelectionGroupBoxRight)
                    self.halfComboBoxRight.setFont(self.font(10, False, 50))
                    self.halfComboBoxRight.addItem("-")
                    self.halfComboBoxRight.addItem("Number One")
                    self.halfComboBoxRight.addItem("Number Two")
                    self.halfComboBoxRight.activated[str].connect(self.halfSelectRight)
                    #Team Label
                    self.teamLabelRight = QtGui.QLabel(self.DataSelectionGroupBoxRight)
                    self.teamLabelRight.setFont(self.font(10, False, 50))
                    self.teamLabelRight.setText("Team")
                    #Team Combo Box
                    self.teamComboBoxRight = QtGui.QComboBox(self.DataSelectionGroupBoxRight)
                    self.teamComboBoxRight.setFont(self.font(10, False, 50))
                    self.teamComboBoxRight.addItem("-")
                    self.teamComboBoxRight.activated[str].connect(self.teamSelectRight)
                    #Player Label
                    self.playerLabelRight = QtGui.QLabel(self.DataSelectionGroupBoxRight)
                    self.playerLabelRight.setFont(self.font(10, False, 50))
                    self.playerLabelRight.setText("Player")
                    #Player Combo Box
                    self.playerComboBoxRight = QtGui.QComboBox(self.DataSelectionGroupBoxRight)
                    self.playerComboBoxRight.setFont(self.font(10, False, 50))
                    self.playerComboBoxRight.addItem("-")
                    self.playerComboBoxRight.activated[str].connect(self.playerSelectRight)
                    #Find Button
                    self.findBtnRight = QtGui.QPushButton(self.DataSelectionGroupBoxRight)
                    self.findBtnRight.setFont(self.font(10, False, 50))
                    self.findBtnRight.setText("Find")
                    self.findBtnRight.clicked.connect(self.findRight)
                    #Clear Button
                    self.clearBtnRight = QtGui.QPushButton(self.DataSelectionGroupBoxRight)
                    self.clearBtnRight.setFont(self.font(10, False, 50))
                    self.clearBtnRight.setText("Clear")
                    self.clearBtnRight.clicked.connect(self.clearValueRight)                    
                    #Layout
                    self.DataSelectionGroupBoxRightGrid = QtGui.QGridLayout(self.DataSelectionGroupBoxRight)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.matchLabelRight, 0, 0, 1, 1)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.matchComboBoxRight, 1, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.halfLabelRight, 2, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.halfComboBoxRight, 3, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.teamLabelRight, 4, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.teamComboBoxRight, 5, 0, 1, 1)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.playerLabelRight, 7, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.playerComboBoxRight, 8, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.findBtnRight, 9, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.DataSelectionGroupBoxRightGrid.addWidget(self.clearBtnRight, 10, 0, 1, 1, QtCore.Qt.AlignBottom)
                self.dataTabRight = QtGui.QWidget()
                self.dataTabRightGrid = QtGui.QGridLayout(self.dataTabRight)
                DataSelectionGroupBoxRight()
                self.dataTabRightGrid.addWidget(self.DataSelectionGroupBoxRight, 0, 0, 1, 1) 
                self.tabsRight.addTab(self.dataTabRight, "Data Selection")
            def teamTabRight():
                def teamGroupBoxRight():
                    #Team Group Box
                    self.teamGroupBoxRight = QtGui.QGroupBox(self.teamTabRight)
                    self.teamGroupBoxRight.setFont(self.font(12, True, 75))
                    self.teamGroupBoxRight.setTitle("Team")
                    #Team Label
                    self.teamNameRight = QtGui.QLabel(self.teamGroupBoxRight)
                    self.teamNameRight.setFont(self.font(14, False, 50))
                    self.teamNameRight.setText("")
                    #Line
                    self.lineRight = QtGui.QFrame(self.teamGroupBoxRight)
                    self.lineRight.setFrameShape(QtGui.QFrame.HLine)
                    self.lineRight.setFrameShadow(QtGui.QFrame.Sunken)
                    #Win Label
                    self.winsRight = QtGui.QLabel(self.teamGroupBoxRight)
                    self.winsRight.setFont(self.font(10, False, 50))
                    self.winsRight.setText("Wins:")
                    #Losses Label
                    self.lossesRight = QtGui.QLabel(self.teamGroupBoxRight)
                    self.lossesRight.setFont(self.font(10, False, 50))
                    self.lossesRight.setText("Losses:")
                    #Win Loss Ratio Label
                    self.wLRatioRight = QtGui.QLabel(self.teamGroupBoxRight)
                    self.wLRatioRight.setFont(self.font(10, False, 50))
                    self.wLRatioRight.setText("Win/Loss Ratio:")
                    #Other Label
                    self.tKDRatioRight = QtGui.QLabel(self.teamGroupBoxRight)
                    self.tKDRatioRight.setFont(self.font(10, False, 50))
                    self.tKDRatioRight.setText("Total Kill/Death Ratio:")
                    #Data Visualization Button
                    self.dataVizTeamRight_1 = QtGui.QPushButton(self.teamGroupBoxRight)
                    self.dataVizTeamRight_1.setFont(self.font(10, False, 50))
                    self.dataVizTeamRight_1.setText("Team Kill/Death Ratio Match by Match")    
                    #Data Visualization Button
                    self.dataVizTeamRight_2 = QtGui.QPushButton(self.teamGroupBoxRight)
                    self.dataVizTeamRight_2.setFont(self.font(10, False, 50))
                    self.dataVizTeamRight_2.setText("Player Combat Score Ratios")  
                    """
                    #Data Visualization Button
                    self.dataVizTeamRight_3 = QtGui.QPushButton(self.teamGroupBoxRight)
                    self.dataVizTeamRight_3.setFont(self.font(10, False, 50))
                    self.dataVizTeamRight_3.setText("Data Viz ")
                    """
                    #Data Visualization Button
                    '''
                    self.dataVizTeamRight_4 = QtGui.QPushButton(self.teamGroupBoxRight)
                    self.dataVizTeamRight_4.setFont(self.font(10, False, 50))
                    self.dataVizTeamRight_4.setText("Data Viz ")
                    '''
                    #Layout
                    self.gridLayout_10 = QtGui.QGridLayout(self.teamGroupBoxRight)
                    self.gridLayout_10.addWidget(self.teamNameRight, 0, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.lineRight, 1, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.winsRight, 2, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.lossesRight, 3, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.wLRatioRight, 4, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.tKDRatioRight, 5, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.dataVizTeamRight_1, 6, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.dataVizTeamRight_2, 7, 0, 1, 1)
                    '''
                    self.gridLayout_10.addWidget(self.dataVizTeamRight_3, 8, 0, 1, 1)
                    self.gridLayout_10.addWidget(self.dataVizTeamRight_4, 9, 0, 1, 1)
                    '''
                self.teamTabRight = QtGui.QWidget()
                self.teamTabRightGrid = QtGui.QGridLayout(self.teamTabRight)
                teamGroupBoxRight()
                self.teamTabRightGrid.addWidget(self.teamGroupBoxRight, 0, 0, 1, 1)
                self.tabsRight.addTab(self.teamTabRight, "")
                self.tabsRight.setTabText(self.tabsRight.indexOf(self.teamTabRight), "Team")
            def playerTabRight():
                def PlayerGroupBoxRight():
                    #Player Group Box
                    self.PlayerGroupBoxRight = QtGui.QGroupBox(self.playerTabRight)
                    self.PlayerGroupBoxRight.setFont(self.font(12, True, 75))
                    self.PlayerGroupBoxRight.setTitle("Player")
                    #Player Label
                    self.playerNameLabelRight = QtGui.QLabel(self.PlayerGroupBoxRight)
                    self.playerNameLabelRight.setFont(self.font(14, False, 50))
                    self.playerNameLabelRight.setText("")
                    #Line 
                    self.lineRight_2 = QtGui.QFrame(self.PlayerGroupBoxRight)
                    self.lineRight_2.setFrameShape(QtGui.QFrame.HLine)
                    self.lineRight_2.setFrameShadow(QtGui.QFrame.Sunken)
                    #Kills label
                    self.killsRight = QtGui.QLabel(self.PlayerGroupBoxRight)
                    self.killsRight.setFont(self.font(10, False, 50))
                    self.killsRight.setText("Kills:")
                    #Deaths Label
                    self.deathsRight = QtGui.QLabel(self.PlayerGroupBoxRight)
                    self.deathsRight.setFont(self.font(10, False, 50))
                    self.deathsRight.setText("Deaths:")
                    #Assists Label
                    self.assistsRight = QtGui.QLabel(self.PlayerGroupBoxRight)
                    self.assistsRight.setFont(self.font(10, False, 50))
                    self.assistsRight.setText("Assists:")
                    #Kill Death Ratio Label
                    self.kDRatioRight = QtGui.QLabel(self.PlayerGroupBoxRight)
                    self.kDRatioRight.setFont(self.font(10, False, 50))
                    self.kDRatioRight.setText("Kill/Death Ratio:")
                    #Combat Score/Death Ratio
                    self.cSDRatioRight = QtGui.QLabel(self.PlayerGroupBoxRight)
                    self.cSDRatioRight.setFont(self.font(10, False, 50))
                    self.cSDRatioRight.setText("Combat Score/Death Ratio:")
                    #Combat Score/Death Ratio
                    self.cSDRatioRelativeRatioRight = QtGui.QLabel(self.PlayerGroupBoxRight)
                    self.cSDRatioRelativeRatioRight.setFont(self.font(10, False, 50))
                    self.cSDRatioRelativeRatioRight.setText("Combat Score/Death Ratio Relative:")
                    #Data Visualization Button
                    self.dataVizPlayerRight_1 = QtGui.QPushButton(self.PlayerGroupBoxRight)
                    self.dataVizPlayerRight_1.setFont(self.font(10, False, 50))
                    self.dataVizPlayerRight_1.setText("Combat Score/Death Ratio Match by Match")
                    #Data Visualization Button
                    self.dataVizPlayerRight_2 = QtGui.QPushButton(self.PlayerGroupBoxRight)
                    self.dataVizPlayerRight_2.setFont(self.font(10, False, 50))
                    self.dataVizPlayerRight_2.setText("Combat Score/Death Ratio Relative Match by Match")
                    '''
                    #Data Visualization Button
                    self.dataVizPlayerRight_3 = QtGui.QPushButton(self.PlayerGroupBoxRight)
                    self.dataVizPlayerRight_3.setFont(self.font(10, False, 50))
                    self.dataVizPlayerRight_3.setText("Data Viz ")
                    #Data Visualization Button
                    self.dataVizPlayerRight_4 = QtGui.QPushButton(self.PlayerGroupBoxRight)
                    self.dataVizPlayerRight_4.setFont(self.font(10, False, 50))
                    self.dataVizPlayerRight_4.setText("Data Viz ")
                    '''
                    #Layout
                    self.PlayerGroupBoxRightGrid = QtGui.QVBoxLayout(self.PlayerGroupBoxRight)
                    self.PlayerGroupBoxRightGrid.addWidget(self.playerNameLabelRight)
                    self.PlayerGroupBoxRightGrid.addWidget(self.lineRight_2)
                    self.PlayerGroupBoxRightGrid.addWidget(self.killsRight)
                    self.PlayerGroupBoxRightGrid.addWidget(self.deathsRight)
                    self.PlayerGroupBoxRightGrid.addWidget(self.assistsRight)
                    self.PlayerGroupBoxRightGrid.addWidget(self.kDRatioRight)
                    self.PlayerGroupBoxRightGrid.addWidget(self.cSDRatioRight)
                    self.PlayerGroupBoxRightGrid.addWidget(self.cSDRatioRelativeRatioRight)
                    self.PlayerGroupBoxRightGrid.addWidget(self.dataVizPlayerRight_1)
                    self.PlayerGroupBoxRightGrid.addWidget(self.dataVizPlayerRight_2)
                    '''
                    self.PlayerGroupBoxRightGrid.addWidget(self.dataVizPlayerRight_3)
                    self.PlayerGroupBoxRightGrid.addWidget(self.dataVizPlayerRight_4)
                    '''
                self.playerTabRight = QtGui.QWidget()
                self.playerTabRightGrid = QtGui.QGridLayout(self.playerTabRight)
                PlayerGroupBoxRight()
                self.playerTabRightGrid.addWidget(self.PlayerGroupBoxRight, 0, 0, 1, 1)                   
                self.tabsRight.addTab(self.playerTabRight, "Player")
            def tournamentRight():
                def TournamentGroupBoxRight():
                    #Tournament Group Box
                    self.TournamentGroupBoxRight = QtGui.QGroupBox(self.tournamentRight)
                    self.TournamentGroupBoxRight.setFont(self.font(12, True, 75))   
                    self.TournamentGroupBoxRight.setTitle("Tournament") 
                    #Tournament Button            
                    self.tournamentBtnRight_1 = QtGui.QPushButton(self.TournamentGroupBoxRight)
                    self.tournamentBtnRight_1.setFont(self.font(10, False, 50))
                    self.tournamentBtnRight_1.setText("Top Teams Kills/Death Ratio")
                    #Tournament Button        
                    self.tournamentBtnRight_2 = QtGui.QPushButton(self.TournamentGroupBoxRight)
                    self.tournamentBtnRight_2.setFont(self.font(10, False, 50))
                    self.tournamentBtnRight_2.setText("Top Archers Combat Score/Death Ratio")                 
                    #Tournament Button 
                    self.tournamentBtnRight_3 = QtGui.QPushButton(self.TournamentGroupBoxRight)
                    self.tournamentBtnRight_3.setFont(self.font(10, False, 50))
                    self.tournamentBtnRight_3.setText("Top Players Combat Score/Death Ratio")   
                    #Tournament Button 
                    self.tournamentBtnRight_4 = QtGui.QPushButton(self.TournamentGroupBoxRight)
                    self.tournamentBtnRight_4.setFont(self.font(10, False, 50))  
                    self.tournamentBtnRight_4.setText("Top Players Combat Score/Death Ratio Relative")  
                    #Tournament Button 
                    self.tournamentBtnRight_5 = QtGui.QPushButton(self.TournamentGroupBoxRight)
                    self.tournamentBtnRight_5.setFont(self.font(10, False, 50))   
                    self.tournamentBtnRight_5.setText("Bottom Players Combat Score/Death Ratio") 
                    #Tournament Button 
                    self.tournamentBtnRight_6 = QtGui.QPushButton(self.TournamentGroupBoxRight)
                    self.tournamentBtnRight_6.setFont(self.font(10, False, 50))   
                    self.tournamentBtnRight_6.setText("Bottom Players Combat Score/Death Ratio Relative") 
                    #Tournament Button 
                    self.tournamentBtnRight_7 = QtGui.QPushButton(self.TournamentGroupBoxRight)
                    self.tournamentBtnRight_7.setFont(self.font(10, False, 50))   
                    self.tournamentBtnRight_7.setText("Top Teams Win/Loss Ratio") 
                    #Layout   
                    self.TournamentGroupBoxRightGrid = QtGui.QGridLayout(self.TournamentGroupBoxRight)
                    self.TournamentGroupBoxRightGrid.addWidget(self.tournamentBtnRight_1, 0, 0, 1, 1)
                    self.TournamentGroupBoxRightGrid.addWidget(self.tournamentBtnRight_2, 1, 0, 1, 1)
                    self.TournamentGroupBoxRightGrid.addWidget(self.tournamentBtnRight_3, 2, 0, 1, 1)
                    self.TournamentGroupBoxRightGrid.addWidget(self.tournamentBtnRight_4, 3, 0, 1, 1)        
                    self.TournamentGroupBoxRightGrid.addWidget(self.tournamentBtnRight_5, 4, 0, 1, 1) 
                    self.TournamentGroupBoxRightGrid.addWidget(self.tournamentBtnRight_6, 5, 0, 1, 1)        
                    self.TournamentGroupBoxRightGrid.addWidget(self.tournamentBtnRight_7, 6, 0, 1, 1)    
                self.tournamentRight = QtGui.QWidget()
                self.tournamentRightGrid = QtGui.QGridLayout(self.tournamentRight)
                TournamentGroupBoxRight()
                self.tournamentRightGrid.addWidget(self.TournamentGroupBoxRight, 0, 0, 1, 1)                       
                self.tabsRight.addTab(self.tournamentRight, "Tournament") 
            dataTabRight()
            teamTabRight()
            playerTabRight()
            tournamentRight()
            self.tabsRight.setCurrentIndex(0)
        TabsLeft()
        TabsRight()
        self.ContainerBottomGrid = QtGui.QHBoxLayout(self.ContainerBottom)
        self.ContainerBottomGrid.addWidget(self.tabsLeft)
        self.ContainerBottomGrid.addWidget(self.tabsRight)
    def font(self, fontSize, Bold, Weight):
        font = QtGui.QFont()
        font.setPointSize(fontSize)
        font.setBold(Bold)
        font.setWeight(Weight)
        return font
    def matchCreate(self):
        matchCount = self.matchNumberSpinBox.value()
        if int(matchCount) not in self.Directory.matchDir:
            if int(matchCount) - 1 in self.Directory.matchDir or int(matchCount) == 1:
                self.Directory.loadSpreadSheet()
                self.Directory.matchCreate(matchCount)
            else:
                self.ErrorTextLine.setText("Missing match #{}: last known match is match #{}".format(str(matchCount - 1), len(self.Directory.matchDir)))
        else:
            self.ErrorTextLine.setText("This match already exists use reload data to change it")
        self.matchComboBoxFill(self.matchComboBoxLeft)
        self.matchComboBoxFill(self.matchComboBoxRight)
    def matchReload(self):
        self.Directory.matchNumber = self.matchNumberSpinBox.value()
        self.Directory.loadSpreadSheet()
        self.Directory.reloadMatches(self.Directory.matchNumber)
        self.matchComboBoxFill(self.matchComboBoxLeft)
        self.matchComboBoxFill(self.matchComboBoxRight)
    def matchComboBoxFill(self, comboBox):
        self.comboEmpty(comboBox)
        for x in range (0, self.Directory.matchNumber):
            comboBox.addItem(str(x + 1))
    def comboEmpty(self, comboBox):
        for x in range(1, comboBox.count()):
            comboBox.removeItem(1)
    def matchSelectRight(self, text):
        if text == "-":
            self.matchRight = None
        else:
            self.matchRight = text
        self.teamComboBoxRightfill()
    def teamComboBoxRightfill(self):
        self.comboEmpty(self.teamComboBoxRight)
        if self.matchRight == None:
            teamList = sorted(self.Directory.teamList, key=str.lower)
            for team in teamList:
                self.teamComboBoxRight.addItem(team)
        else:
            teamList = sorted(self.Directory.matchDir[int(self.matchRight)].teamList, key=str.lower)
            for team in teamList:
                self.teamComboBoxRight.addItem(team)
        self.playerComboBoxRightFill()
    def playerComboBoxRightFill(self):
        self.comboEmpty(self.playerComboBoxRight)
        if self.matchRight == None:
            if self.teamRight == None:
                playerList = sorted(self.Directory.playerList, key=str.lower)
                for player in playerList:
                    self.playerComboBoxRight.addItem(player)        
            else:
                playerList = sorted(self.Directory.teamDir[self.teamRight].playerList, key=str.lower)
                for player in playerList:
                    self.playerComboBoxRight.addItem(player)    
        else:
            if self.teamRight == None:
                playerList = sorted(self.Directory.matchDir[int(self.matchRight)].playerList, key=str.lower)    
                for player in playerList:
                    self.playerComboBoxRight.addItem(player)       
            else:
                playerList = sorted(self.Directory.matchDir[int(self.matchRight)].teamDir[self.teamRight].playerList, key=str.lower)
                for player in playerList:
                    self.playerComboBoxRight.addItem(player)
    def halfSelectRight(self, text):
        if text == "-":
            self.halfRight = None
        elif text == "Number One":
            self.halfRight = 1
        else:
            self.halfRight = 2
    def teamSelectRight(self, text):
        if text == "-":
            self.teamRight = None
        else:
            self.teamRight = text
        self.playerComboBoxRightFill()
    def playerSelectRight(self, text):
        if text == "-":
            self.playerRight = None
        else:
            self.playerRight = text
    def matchSelectLeft(self, text):
        if text == "-":
            self.matchLeft = None
        else:
            self.matchLeft = text
        self.teamComboBoxLeftfill()
    def teamComboBoxLeftfill(self):
        self.comboEmpty(self.teamComboBoxLeft)
        if self.matchLeft == None:
            teamList = sorted(self.Directory.teamList, key=str.lower)
            for team in teamList:
                self.teamComboBoxLeft.addItem(team)
        else:
            teamList = sorted(self.Directory.matchDir[int(self.matchLeft)].teamList, key=str.lower)
            for team in teamList:
                self.teamComboBoxLeft.addItem(team)
        self.playerComboBoxLeftFill()
    def playerComboBoxLeftFill(self):
        self.comboEmpty(self.playerComboBoxLeft)
        if self.matchLeft == None:
            if self.teamLeft == None:
                playerList = sorted(self.Directory.playerList, key=str.lower)
                for player in playerList:
                    self.playerComboBoxLeft.addItem(player)        
            else:
                playerList = sorted(self.Directory.teamDir[self.teamLeft].playerList, key=str.lower)
                for player in playerList:
                    self.playerComboBoxLeft.addItem(player)    
        else:
            if self.teamLeft == None:    
                playerList = sorted(self.Directory.matchDir[int(self.matchLeft)].playerList, key=str.lower)
                for player in playerList:
                    self.playerComboBoxLeft.addItem(player)       
            else:
                playerList = sorted(self.Directory.matchDir[int(self.matchLeft)].teamDir[self.teamLeft].playerList, key=str.lower)
                for player in playerList:
                    self.playerComboBoxLeft.addItem(player)
    def halfSelectLeft(self, text):
        if text == "-":
            self.halfLeft = None
        elif text == "Number One":
            self.halfLeft = 1
        else:
            self.halfLeft = 2
    def teamSelectLeft(self, text):
        if text == "-":
            self.teamLeft = None
        else:
            self.teamLeft = text
        self.playerComboBoxLeftFill()
    def playerSelectLeft(self, text):
        if text == "-":
            self.playerLeft = None
        else:
            self.playerLeft = text
    def matchComboBoxFill(self, comboBox):
        self.comboEmpty(comboBox)
        for x in range (0, self.Directory.matchNumber):
            comboBox.addItem(str(x + 1))
    def findRight(self):
        self.playerobjectRight = None
        self.teamObjectRight = None
        if self.matchRight != None:
            if self.halfRight != None:
                if self.teamRight != None:
                    if self.playerRight != None:
                        self.playerobjectRight = self.Directory.matchDir[int(self.matchRight)].halfDir[int(self.halfRight)].teamDir[self.teamRight].playerDir[self.playerRight]
                        self.teamObjectRight = self.Directory.matchDir[int(self.matchRight)].halfDir[int(self.halfRight)].teamDir[self.teamRight]
                    else:
                        self.teamObjectRight = self.Directory.matchDir[int(self.matchRight)].halfDir[int(self.halfRight)].teamDir[self.teamRight]
                else:
                    if self.playerRight != None:
                        self.playerobjectRight = self.Directory.matchDir[int(self.matchRight)].halfDir[int(self.halfRight)].playerDir[self.playerRight]
                    else:
                        pass
            else:
                if self.teamRight != None:
                    if self.playerRight != None:
                        self.playerobjectRight = self.Directory.matchDir[int(self.matchRight)].teamDir[self.teamRight].playerDir[self.playerRight]
                        self.teamObjectRight = self.Directory.matchDir[int(self.matchRight)].teamDir[self.teamRight]
                    else:
                        self.teamObjectRight = self.Directory.matchDir[int(self.matchRight)].teamDir[self.teamRight]
                else:
                    if self.playerRight != None:
                        self.playerobjectRight = self.Directory.matchDir[int(self.matchRight)].playerDir[self.playerRight]
                    else:
                        pass
        else:
            if self.halfRight != None:
                if self.teamRight != None:
                    if self.playerRight != None:
                        self.playerobjectRight = self.Directory.teamDir[self.teamRight].playerDir[self.playerRight]
                        self.teamObjectRight = self.Directory.teamDir[self.teamRight]
                    else:
                        self.teamObjectRight = self.Directory.teamDir[self.teamRight]
                else:
                    if self.playerRight != None:
                        self.playerobjectRight = self.Directory.playerDir[self.playerRight]
                    else:
                        pass
            else:
                if self.teamRight != None:
                    if self.playerRight != None:
                        self.playerobjectRight = self.Directory.teamDir[self.teamRight].playerDir[self.playerRight]
                        self.teamObjectRight = self.Directory.teamDir[self.teamRight]
                    else:
                        self.teamObjectRight = self.Directory.teamDir[self.teamRight]
                else:
                    if self.playerRight != None:
                        self.playerobjectRight = self.Directory.playerDir[self.playerRight]
                    else:
                        pass
        if self.teamObjectRight != None:
            self.teamNameRight.setText("{}".format(self.teamObjectRight.teamName))
            self.winsRight.setText("Wins: {}".format(self.teamObjectRight.teamWins))
            self.lossesRight.setText("Losses: {}".format(self.teamObjectRight.teamLoss))
            self.wLRatioRight.setText("Win Loss Ratio: {}".format(self.teamObjectRight.wLRatio))
            #self.tKDRatioRight.setText("Total Kill/Death Ratio: {}".format())
        if self.playerobjectRight != None:
            self.playerNameLabelRight.setText("{}".format(self.playerobjectRight.playerName))
            self.killsRight.setText("Kills: {}".format(self.playerobjectRight.kills))
            self.deathsRight.setText("Deaths: {}".format(self.playerobjectRight.deaths))
            self.assistsRight.setText("Assists: {}".format(self.playerobjectRight.assists))
            self.kDRatioRight.setText("Kill/Death Ratio: {}".format(self.playerobjectRight.kDRatio))
            #self.cSDRatioRight.setText("Combat Score/Death Ratio: {}".format())
            #self.cSDRatioRelativeRight.setText("Combat Score/Death Ratio Relative: {}".format())
        self.matchRight = None
        self.halfRight = None
        self.teamRight =  None
        self.playerRight = None
    def findLeft(self):
        self.playerobjectLeft = None
        self.teamObjectLeft = None
        if self.matchLeft != None:
            if self.halfLeft != None:
                if self.teamLeft != None:
                    if self.playerLeft != None:
                        self.playerobjectLeft = self.Directory.matchDir[int(self.matchLeft)].halfDir[int(self.halfLeft)].teamDir[self.teamLeft].playerDir[self.playerLeft]
                        self.teamObjectLeft = self.Directory.matchDir[int(self.matchLeft)].halfDir[int(self.halfLeft)].teamDir[self.teamLeft]
                    else:
                        self.teamObjectLeft = self.Directory.matchDir[int(self.matchLeft)].halfDir[int(self.halfLeft)].teamDir[self.teamLeft]
                else:
                    if self.playerLeft != None:
                        self.playerobjectLeft = self.Directory.matchDir[int(self.matchLeft)].halfDir[int(self.halfLeft)].playerDir[self.playerLeft]
                    else:
                        pass
            else:
                if self.teamLeft != None:
                    if self.playerLeft != None:
                        self.playerobjectLeft = self.Directory.matchDir[int(self.matchLeft)].teamDir[self.teamLeft].playerDir[self.playerLeft]
                        self.teamObjectLeft = self.Directory.matchDir[int(self.matchLeft)].teamDir[self.teamLeft]
                    else:
                        self.teamObjectLeft = self.Directory.matchDir[int(self.matchLeft)].teamDir[self.teamLeft]
                else:
                    if self.playerLeft != None:
                        self.playerobjectLeft = self.Directory.matchDir[int(self.matchLeft)].playerDir[self.playerLeft]
                    else:
                        pass
        else:
            if self.halfLeft != None:
                if self.teamLeft != None:
                    if self.playerLeft != None:
                        self.playerobjectLeft = self.Directory.teamDir[self.teamLeft].playerDir[self.playerLeft]
                        self.teamObjectLeft = self.Directory.teamDir[self.teamLeft]
                    else:
                        self.teamObjectLeft = self.Directory.teamDir[self.teamLeft]
                else:
                    if self.playerLeft != None:
                        self.playerobjectLeft = self.Directory.playerDir[self.playerLeft]
                    else:
                        pass
            else:
                if self.teamLeft != None:
                    if self.playerLeft != None:
                        self.playerobjectLeft = self.Directory.teamDir[self.teamLeft].playerDir[self.playerLeft]
                        self.teamObjectLeft = self.Directory.teamDir[self.teamLeft]
                    else:
                        self.teamObjectLeft = self.Directory.teamDir[self.teamLeft]
                else:
                    if self.playerLeft != None:
                        self.playerobjectLeft = self.Directory.playerDir[self.playerLeft]
                    else:
                        pass
        if self.teamObjectLeft != None:
            self.teamNameLeft.setText("{}".format(self.teamObjectLeft.teamName))
            self.winsLeft.setText("Wins: {}".format(self.teamObjectLeft.teamWins))
            self.lossesLeft.setText("Losses: {}".format(self.teamObjectLeft.teamLoss))
            self.wLRatioLeft.setText("Win Loss Ratio: {}".format(self.teamObjectLeft.wLRatio))
            #self.tKDRatioLeft.setText("Total Kill/Death Ratio: {}".format())
        if self.playerobjectLeft != None:
            self.playerNameLabelLeft.setText("{}".format(self.playerobjectLeft.playerName))
            self.killsLeft.setText("Kills: {}".format(self.playerobjectLeft.kills))
            self.deathsLeft.setText("Deaths: {}".format(self.playerobjectLeft.deaths))
            self.assistsLeft.setText("Assists: {}".format(self.playerobjectLeft.assists))
            self.kDRatioLeft.setText("K/D Ratio: {}".format(self.playerobjectLeft.kDRatio))
            #self.cSDRatioLeft.setText("Is Archer: {}".format(self.playerobjectLeft.isArcher))
            #self.cSDRatioRelativeLeft.setText("Is Archer: {}".format(self.playerobjectLeft.isArcher))
        self.matchLeft = None
        self.halfLeft = None
        self.teamLeft =  None
        self.playerLeft = None
    def clearValueLeft(self):
        self.matchLeft = None
        self.halfLeft = None
        self.teamLeft =  None
        self.playerLeft = None
        self.teamObjectLeft = None
        self.playerobjectLeft = None
        self.comboEmpty(self.playerComboBoxLeft)
        self.comboEmpty(self.teamComboBoxLeft)
        self.halfComboBoxLeft.setCurrentIndex(0)
        self.matchComboBoxLeft.setCurrentIndex(0)
    def clearValueRight(self):
        self.matchRight = None
        self.halfRight = None
        self.teamRight =  None
        self.playerRight = None
        self.teamObjectRight = None
        self.playerobjectRight = None
        self.comboEmpty(self.playerComboBoxRight)
        self.comboEmpty(self.teamComboBoxRight)
        self.halfComboBoxRight.setCurrentIndex(0)
        self.matchComboBoxRight.setCurrentIndex(0)  
def run(Directory):
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow(Directory)
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

    