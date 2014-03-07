# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'

#####################
## Things that could use improving!!!
##  1. Scaling the window/UI evenly is a tedious task, a centralized scale var would be nice
##  2. Some controls are still named things like label_2, consider adding descriptive names


import sys, os
import math
import algaeTable
from Globals import *

from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
import random
import resources_qrc 
from random import randint
from PyQt4 import QtCore, QtGui,QtOpenGL
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from results import Ui_results
from preferences import Ui_Preferences
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


#####################################################################################
#####################################################################################

#algaeTable = AlgaeTable()
algaeList = []
random.seed()
windowScale = 1.0
initWidth = 600
initHeight = 700

#This is the function that sets up the Main Window Widget
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Digital Microscope"))
        MainWindow.resize(initWidth * windowScale, 792 * windowScale)
        self.startUpFlag=False
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))

        
        self.scene = QtGui.QGraphicsScene(0, 0, initWidth * windowScale, 490 * windowScale)
        self.view = QtGui.QGraphicsView(self.scene, self.centralWidget)
        self.scene.setBackgroundBrush(QtGui.QColor("white"))
        self.centralWidget.centralWidget = self.view

        self.submit_button = QtGui.QPushButton(self.centralWidget)
        self.submit_button.setGeometry(QtCore.QRect(initWidth/2 * windowScale - 231/2, 690 * windowScale, 231, 41))
        self.submit_button.setObjectName(_fromUtf8("submit_button"))


        # button actions
        self.submit_button.clicked.connect(self.openResults)
        # self.findButton.clicked.connect(self.addToChart)

        
        #answer Table
        self.ans_table = QtGui.QTableWidget(self.centralWidget)
        self.ans_table.setGeometry(QtCore.QRect(50, 400 * windowScale, (initWidth  * windowScale - 100), 100))
        self.ans_table.setObjectName(_fromUtf8("ans_table"))
        self.ans_table.setColumnCount(2)
        self.ans_table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.ans_table.verticalHeader().setVisible(False)
        self.ans_table.setHorizontalHeaderLabels(['Name', 'Count'])
        self.ans_table.keyPressEvent = lambda event: event.ignore()
        
        
        
        MainWindow.setCentralWidget(self.centralWidget)
        
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 999, 26))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        
        self.menuTools = QtGui.QMenu(self.menuBar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        
        MainWindow.setMenuBar(self.menuBar)
        
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        
        MainWindow.setStatusBar(self.statusBar)
        
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout.triggered.connect(self.openAbout)

        
        self.actionControls = QtGui.QAction(MainWindow)
        self.actionControls.setObjectName(_fromUtf8("actionControls"))
        self.actionImport_Sample = QtGui.QAction(MainWindow)
        self.actionImport_Sample.setObjectName(_fromUtf8("actionImport_Sample"))
        
        self.actionCreate_New_Sample = QtGui.QAction(MainWindow)
        self.actionCreate_New_Sample.setObjectName(_fromUtf8("actionCreate_New_Sample"))
 
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionPreferences.triggered.connect(self.openPreferences)
        
        
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_Sample)
        self.menuFile.addAction(self.actionCreate_New_Sample)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences) # This is actually the execution of creating a new Session. 
        
        self.menuTools.addAction(self.actionAbout)
        self.menuTools.addAction(self.actionControls)
        
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def redrawUi(self):
        print windowScale
        self.scene.setSceneRect(0, 0, initWidth * windowScale, 400 * windowScale)
        self.submit_button.setGeometry(QtCore.QRect(initWidth/2 * windowScale - 231/2, 690 * windowScale, 231, 41))
        self.ans_table.setGeometry(QtCore.QRect(initWidth/2  * windowScale - 411/2, 500 * windowScale, 411, 181))
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.submit_button.setText(_translate("MainWindow", "Submit", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuTools.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionAbout.setText(_translate("MainWindow", "About...", None))
        self.actionPreferences.setText(_translate("MainWindow", "Create New Session", None))
        self.actionControls.setText(_translate("MainWindow", "Controls", None))
        self.actionImport_Sample.setText(_translate("MainWindow", "Import Existing Sample", None))
        self.actionCreate_New_Sample.setText(_translate("MainWindow", "Create New Sample", None))

    def setUpScene(self,scene,view ):
        pic = Pixmap(QtGui.QPixmap(":/Assets/Beaker_BG.png"), windowScale)
        pic.pos = QtCore.QPointF(0,0)
        pic.pos = QtCore.QPointF(random.randint(-100, 100)-initWidth/2, 0)
        self.scene.addItem(pic.pixmap_item) 
        #print "Printing Algae:"

        for key in algaeTable.AlgaeLib:
            if algaeTable.Is_Active(key):
                image = QtGui.QPixmap(":/Assets/20um/"+algaeTable.Get_File_Name(key))
                Trial = algaeTable.Get_Current_Round()
                #print key + ": " + str(algaeTable.Get_Actual_Count(key, Trial)) + " (" + str(algaeTable.Get_Min(key)) + " - " + str(algaeTable.Get_Max(key)) + ")"
                for y in xrange(algaeTable.Get_Actual_Count(key, Trial)):
                    #print "Drawing: " + algaeTable.Name_Array[x]
                    pic = Pixmap(image, .03)
                    # sets random positions with padding at the edge of the view
                    # following 3 lines should probably be part of the constructor
                    radius = 195.0
                    testPos = QtCore.QPointF(radius,radius)
                    while((testPos.x()**2 + testPos.y()**2)**(1.0/2.0) > radius):
                        testPos = QtCore.QPointF(random.randint(-195, 195), random.randint(-195, 195))
                    testPos = QtCore.QPointF((int)((testPos.x() + initWidth/2) * windowScale),(int)( (testPos.y() + 245) * windowScale))
                    pic.pos = testPos
                    pic.setRot(random.randint(0, 359))
                    pic.setScaleVariance(random.randint(-5, 10)/1000.0)
                    algaeList.append(pic)
                    self.scene.addItem(pic.pixmap_item)
        pic = Pixmap(QtGui.QPixmap(":/Assets/CircleView2.png"), windowScale)
        pic.pos = QtCore.QPointF(-initWidth/2+95,0)
        self.scene.addItem(pic.pixmap_item) 
        print "\n"
        print "Remaining Trials:" + str(algaeTable.Get_Num_Trials())
            
    ## Dialog for accurate guesses, appears when "<32" comboBoxItem is selected.
    ## Only accepts values >0 and <= 32, other values are truncated.
    ## Creating an event that sets the text and closes the dialog rather than using View.done
    ## and a trigger on the lineEdit would fix the trucation.
    class myCombo(QtGui.QComboBox):
        textAt4 = "32"
        skipOpen = True
        def __init__(self, parent = None):
            QtGui.QLineEdit.__init__(self, parent)
            self.currentIndexChanged['QString'].connect(self.handleIndexChanged)

        class Ui_View(object):
            def setupUi(self, View, combo):
                View.setFixedSize(300, 150)
                self.combo = combo
                self.promptLabel = QtGui.QLabel("Please enter number less than or equal to 32", View)
                self.promptLabel.setGeometry(35,0, 231, 41)
                self.promptLabel.setObjectName(_fromUtf8("<32 Label"))
                self.inputBox = QtGui.QLineEdit(View)
                self.inputBox.setGeometry(35,45, 231, 30)
                self.inputBox.setObjectName(_fromUtf8("<32 Label"))
                self.inputBox.textChanged['QString'].connect(self.handleTextChanged)
                self.okButton = QtGui.QPushButton(View)
                self.okButton.setGeometry(QtCore.QRect(35,80, 231, 41))
                self.okButton.setObjectName(_fromUtf8("submit_button"))
                self.okButton.setText("OK")
                self.okButton.clicked.connect(View.done)

            def handleTextChanged(self, value):
                if(str(value).isdigit()):
                    if(int(value) <= 32 and int(value) >= 0):
                        print value
                        self.combo.setItemText(4, value)
                        self.combo.textAt4 = value


        def handleIndexChanged(self, value):
            if(not self.skipOpen):
                if value == self.textAt4:
                    Open_View_Dialog=self.Ui_View()
                    View_Ui=QtGui.QDialog();
                    Open_View_Dialog.setupUi(View_Ui, self)
                    View_Ui.setModal(True) 
                    View_Ui.exec_()
                    
            self.skipOpen = False
    #keep track of how many boxes are checked         
    def CheckStateChanged(self,state):
        if state== QtCore.Qt.Checked:
            self.Count_Check+=1
        else:
            self.Count_Check-=1
            self.Check_All.setCheckState(QtCore.Qt.Unchecked)
     #list of all the groupboxes each contains a checkbox and 2 text lines
    
    def setNames(self):
        self.List_Algae_Select = QtGui.QWidget()
        self.List_Algae_Select.setGeometry(QtCore.QRect(20, 30, 670, 230))
        self.List_Algae_Select.setObjectName(_fromUtf8("List_Algae_Select"))

        self.formLayout = QtGui.QFormLayout(self.List_Algae_Select)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        
        self.GroupBoxList=[]
        self.List_Algae_Select = QtGui.QWidget()
        Index =0
        for key in algaeTable.AlgaeLib:
            if algaeTable.Is_Active(key):
                Index += 7
                self.CurrentGroupBox = QtGui.QGroupBox(self.List_Algae_Select)
                self.CurrentGroupBox.setTitle(_fromUtf8(key))
                self.CurrentGroupBox.setObjectName(_fromUtf8("CurrentGroupBox"))
                
                self.CurrentLayoutWidget = QtGui.QWidget(self.CurrentGroupBox)
                self.CurrentLayoutWidget.setGeometry(QtCore.QRect(10,20,600,47))
                self.CurrentLayoutWidget.setObjectName(_fromUtf8("CurrentLayoutWidget"))

                self.Range_High = QtGui.QLineEdit(self.CurrentLayoutWidget)
                self.Range_High.setGeometry(QtCore.QRect(20 , 30 , 500, 50))
                self.Range_High.setObjectName("High")
                self.Range_High.setText("23 - 64")
                
                self.GroupBoxList.append(self.CurrentLayoutWidget)#self.Check_include)
                self.ans_table.insertRow(0)
                self.ans_table.setItem(0,0,QtGui.QTableWidgetItem(key))
                self.Text_Range_Low = QtGui.QLineEdit(self.CurrentLayoutWidget)
                self.ans_table.setCellWidget(0,1, self.Range_High)
                self.ans_table.item(0,0).setFlags(Qt.NoItemFlags)
                self.ans_table.sortItems(0,Qt.AscendingOrder)
                print ' Print label : ' , self.Range_High.text()
        
            
    def resetForms(self):
        self.scene.clear()
        self.ans_table.setRowCount(0)
        self.ans_table.clearContents()
        self.setNames()

    def openResults(self):
        def getGuess(qTableWidget, row):
            candidate = qTableWidget.cellWidget(row, 1)
            if(str(candidate).isdigit()):
                return int(candidate)
            else:
                return int((int(candidate.text().split("-")[0]) * int(candidate.text().split("-")[1])) ** (1.0/2.0))
        def getName(qTableWidget, row):
            return str(qTableWidget.item(row, 0).text())
        
        print "Attempting to open results"
        # Save Algae View as image for review later
        outImage = QPixmap(999, 400)
        painter = QPainter(outImage)        
        self.scene.render(painter)
        
        mypath = os.getcwd()+"/TempSampleRenders"
        if not os.path.isdir(mypath):
           os.makedirs(mypath)
        if(not outImage.save(os.getcwd()+"/TempSampleRenders/Trial" + str(algaeTable.Get_Current_Round()+1) + ".png")):
            print "failed to save render"
        painter.end()

        ## Record user answers
        for z in xrange(self.ans_table.rowCount()):
            key = getName(self.ans_table, z)
            count = getGuess(self.ans_table, z)
            algaeTable.Set_User_Count(key,algaeTable.Get_Current_Round(),count)
            
        ## Only show results page after all trials are finished
        if (algaeTable.Get_Num_Trials() <= 1):
            print "All trials finished"
            resultsDialog=Ui_results()
            ui=QtGui.QDialog();
            resultsDialog.setupUi(ui, algaeTable,self.ans_table)
            ui.setModal(True) 
            ui.exec_()
            ## Start new session
            ##algaeTable.Set_Num_Trials(algaeTable.Total_Trials)
            self.openPreferences()
        else:
            print "More trials to go"
            algaeTable.Decrement_Trials()
            #after Results page closes generate new sample and reset forms
            self.resetForms()
            algaeTable.Generate_Sample()
            self.setUpScene(self.scene, self.view)
        print "Finished trying to open results."
        
    def openPreferences(self):
        preferencesDialog=Ui_Preferences()
        gui=QtGui.QDialog();
        preferencesDialog.setupUi(gui,self.startUpFlag)
        gui.setModal(True) 
        reset=gui.exec_()
        #reset the session when the parameters have been changed
        if reset==int(True):
            self.setSession()#preferencesDialog.retVal())
            
    def openAbout(self) :
        print "About has been reached"
        class DefAbout():
            skipOpen = True
            def __init__(self, parent = None):
                QtGui.QComboBox.__init__(self, parent)
            class Ui_View(object):
                def setupUi(self,View,combo) :
                    View.setFixedSize(300,150)
                    self.combo=combo
                    self.okButton = QtGui.QPushButton(View)
                    self.okButton.setGeomentry(QtCore.QRect(35,80,231,41))
                    self.okButton.setText("OK")
                    self.okButton.clicked.connect(View.done)

    #reset all relevant variables and restart the session    
    def setSession(self): #session):
        print " New Set Session "
        self.resetForms()
        algaeTable.Generate_Sample()
        self.setUpScene(self.scene, self.view) 
           
    
            
class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)

    # Cleans up Temporary Sample Renders on close
    def closeEvent(self, event):
        folder = os.getcwd() + "/TempSampleRenders"
        for aFile in os.listdir(folder):
            filePath = os.path.join(folder, aFile)
            if(aFile != ".gitignore"):
                os.unlink(filePath)

        event.accept()
		
if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    mwindow = Window()
    mwindow.ui.startUpFlag=True
    mwindow.ui.openPreferences()
    mwindow.ui.startUpFlag=False
    mwindow.show()
    sys.exit(app.exec_())
    

		
