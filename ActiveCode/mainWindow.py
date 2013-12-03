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

import random
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
#algaeTable.Generate_Sample()


## 2um scale is 557/8px long
## so initialy a 75mm*25mm slide is 167343px wide and 11718px high
##====================================================
##  scaling and moving have been disabled ##
##=============================================
##offsetX = 0.0
##offsetY = 0.0
##offsetMaxX = 167343.75/2
##offsetMaxY = 11718.75/2
##offsetMinX = -offsetMaxX
##offsetMinY = -offsetMaxY
##magLevel = 400
##magLevelMin = 60



### Class borrowed from animatedtiles demo:
# PyQt doesn't support deriving from more than one wrapped class so we use
# composition and delegate the property.
'''class Pixmap(QtCore.QObject):
    def __init__(self, pix):
        super(Pixmap, self).__init__()

        self.pixmap_item = QtGui.QGraphicsPixmapItem(pix)
        self.pixmap_item.setCacheMode(QtGui.QGraphicsItem.DeviceCoordinateCache)
        self.pixmap_item.setScale(.03)
    def _set_pos(self, pos):
        self.pixmap_item.setPos(pos)

    def setRot(self, angle):
        self.pixmap_item.setRotation(angle)

    def setScaleVariance(self, var):
        self.pixmap_item.setScale(self.pixmap_item.scale() + var)

    pos = QtCore.pyqtProperty(QtCore.QPointF, fset=_set_pos)'''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Digital Microscope"))
        MainWindow.setFixedSize(999, 792)
        self.startUpFlag=False
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        
###################
##        DISABLED
########################
##        self.magLabel = QtGui.QLabel(self.centralWidget)
##        self.magLabel.setGeometry(900, 405, 90, 30)
##        global magLevel
##        self.magLabel.setText("%dX" % magLevel)
##        self.magLabel.setStyleSheet("font: 18pt;" )
        
        self.scene = QtGui.QGraphicsScene(0, 0, 999, 400)
        self.view = QtGui.QGraphicsView(self.scene, self.centralWidget)
        self.scene.setBackgroundBrush(QtGui.QColor("white"))
        self.centralWidget.centralWidget = self.view

        # Controls		
        self.groupBox_mag = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_mag.setGeometry(QtCore.QRect(340, 430, 201, 271))
        self.groupBox_mag.setTitle(_fromUtf8(""))
        self.groupBox_mag.setObjectName(_fromUtf8("groupBox_mag"))
        
        self.label = QtGui.QLabel(self.groupBox_mag)
        self.label.setGeometry(QtCore.QRect(60, 240, 101, 20))
        self.label.setObjectName(_fromUtf8("label"))        
        
        self.mag_dial = QtGui.QDial(self.groupBox_mag)
        self.mag_dial.setGeometry(QtCore.QRect(60, 70, 91, 101))
        self.mag_dial.setMinimum(0)
        self.mag_dial.setMaximum(100)
        self.mag_dial.setInvertedAppearance(False)
        self.mag_dial.setInvertedControls(False)
        self.mag_dial.setWrapping(True)
        self.mag_dial.setNotchesVisible(False)
        self.mag_dial.setObjectName(_fromUtf8("mag_dial"))
        self.mag_dial.keyPressEvent = lambda event: event.ignore()
        
        self.label_4 = QtGui.QLabel(self.groupBox_mag)
        self.label_4.setGeometry(QtCore.QRect(90, 50, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_mag)
        self.label_5.setGeometry(QtCore.QRect(30, 110, 41, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_mag)
        self.label_6.setGeometry(QtCore.QRect(150, 110, 71, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox_mag)
        self.label_7.setGeometry(QtCore.QRect(90, 170, 41, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))

###################
##        DISABLED : The input section for the algae Samples
########################
       # self.input_species = QtGui.QLineEdit(self.centralWidget)
       # self.input_species.setGeometry(QtCore.QRect(550, 430, 181, 31))
       # self.input_species.setText(_fromUtf8(""))
       # self.input_species.setPlaceholderText ("Enter Name of Algae")
       # self.input_species.setObjectName(_fromUtf8("input_species"))

		
        self.groupBox_move = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_move.setGeometry(QtCore.QRect(30, 430, 291, 271))
        self.groupBox_move.setTitle(_fromUtf8(""))
        self.groupBox_move.setObjectName(_fromUtf8("groupBox_move"))
        self.groupBox_move.keyPressEvent = lambda event: event.ignore()

        self.cameraLabel = QtGui.QLabel(self.groupBox_move)
        self.cameraLabel.setGeometry(QtCore.QRect(110, 95, 50, 50))
        self.cameraLabel.setPixmap(QtGui.QPixmap(os.getcwd() + "/Assets/camera.png"))
        self.cameraLabel.setScaledContents(True)

        #buttons
        
        self.findButton = QtGui.QPushButton(self.centralWidget)
        self.findButton.setGeometry(QtCore.QRect(870, 430, 91, 31))
        self.findButton.setObjectName(_fromUtf8("findButton"))
     
        self.submit_button = QtGui.QPushButton(self.centralWidget)
        self.submit_button.setGeometry(QtCore.QRect(640, 660, 231, 41))
        self.submit_button.setObjectName(_fromUtf8("submit_button"))
        
        self.up_button = QtGui.QPushButton(self.groupBox_move)
        self.up_button.setGeometry(QtCore.QRect(100, 40, 71, 28))
        self.up_button.setObjectName(_fromUtf8("up_button"))
        
        self.left_button = QtGui.QPushButton(self.groupBox_move)
        self.left_button.setGeometry(QtCore.QRect(20, 100, 61, 28))
        self.left_button.setObjectName(_fromUtf8("pushButton_2"))
        
        self.right_button = QtGui.QPushButton(self.groupBox_move)
        self.right_button.setGeometry(QtCore.QRect(192, 100, 71, 28))
        self.right_button.setObjectName(_fromUtf8("right_button"))
        
        self.down_button = QtGui.QPushButton(self.groupBox_move)
        self.down_button.setGeometry(QtCore.QRect(100, 160, 71, 28))
        self.down_button.setObjectName(_fromUtf8("down_button"))
        
        self.label_2 = QtGui.QLabel(self.groupBox_move)
        self.label_2.setGeometry(QtCore.QRect(120, 240, 71, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
###################
##        DISABLED
########################
        
        self.input_count = QtGui.QLineEdit(self.centralWidget)
        self.input_count.setGeometry(QtCore.QRect(750, 430, 111, 31))
        self.input_count.setText(_fromUtf8(""))
        self.input_count.setObjectName(_fromUtf8("input_count"))
        self.input_count.setPlaceholderText ("Enter Count")

        # button actions
        self.submit_button.clicked.connect(self.openResults)
      #  self.findButton.clicked.connect(self.addToChart)
#########################
##        DISABLED
#########################
##        self.right_button.pressed.connect(self.RTrans)
##        self.right_button.setAutoRepeat(True)
##        self.left_button.pressed.connect(self.LTrans)
##        self.left_button.setAutoRepeat(True)
##        self.up_button.pressed.connect(self.UTrans)
##        self.up_button.setAutoRepeat(True)
##        self.down_button.pressed.connect(self.DTrans)
##        self.down_button.setAutoRepeat(True)
        
        #answer Table
        self.ans_table = QtGui.QTableWidget(self.centralWidget)
        self.ans_table.setGeometry(QtCore.QRect(550, 470, 411, 181))
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
        #self.actionPreferences.triggered.connect(self.openPreferences)

        
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
        self.menuFile.addAction(self.actionPreferences)
        
        self.menuTools.addAction(self.actionAbout)
        self.menuTools.addAction(self.actionControls)
        
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.findButton.setText(_translate("MainWindow", "Add", None))
        self.label.setText(_translate("MainWindow", "Magnification", None))
        self.label_4.setText(_translate("MainWindow", "200X", None))
        self.label_5.setText(_translate("MainWindow", "100X", None))
        self.label_6.setText(_translate("MainWindow", "400X", None))
        self.label_7.setText(_translate("MainWindow", "600X", None))
        self.submit_button.setText(_translate("MainWindow", "Submit", None))
        self.up_button.setText(_translate("MainWindow", "UP", None)) 
        self.left_button.setText(_translate("MainWindow", "Left", None))
        self.right_button.setText(_translate("MainWindow", "Right", None))
        self.down_button.setText(_translate("MainWindow", "Down", None))
        self.label_2.setText(_translate("MainWindow", "Movement", None))
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
        print "Printing Algae:"
        # this algae gen algorithm's run time is terrible
        for x in xrange(algaeTable.Total_Algae_Types):
            image = QtGui.QPixmap(os.getcwd() + "/Assets/20um/"+algaeTable.Get_File_Name(x))
            print str(algaeTable.Get_Name(x)) + ": " + str(algaeTable.Get_Count(x)) + " (" + str(algaeTable.Min_Count_Array[x]) + " - " + str(algaeTable.Max_Count_Array[x]) + ")"
            for y in xrange(algaeTable.Total_Count_Array[x]):
                #print "Drawing: " + algaeTable.Name_Array[x]
                pic = Pixmap(image, .03)
                # sets random positions with padding at the edge of the view
                # following 3 lines should probably be part of the constructor
                radius = 200
                pic.pos = QtCore.QPointF(random.randint(20, 979), random.randint(20, 370))
                pic.setRot(random.randint(0, 359))
                pic.setScaleVariance(random.randint(-5, 10)/1000.0)
                algaeList.append(pic)
                self.scene.addItem(pic.pixmap_item)
        print "\n"
        print "Remaining Trials:" + str(algaeTable.Get_Num_Trials())
###################
##        DISABLED
########################              
#    def addToChart(self):
        #checks if "count" value is a number and if the "name" field is not empty 
        # adds them to the table. and sorts them alphabeticaly by name
 #       try:
 #           number=int(self.input_count.text())
 #           if not (self.input_species.text().isEmpty()):
 #               self.ans_table.insertRow(0)
 #               self.ans_table.setItem(0,1,QtGui.QTableWidgetItem("0"))
 #               self.ans_table.setItem(0,0,QtGui.QTableWidgetItem(self.input_species.text()))
               

 #               self.ans_table.sortItems(0,Qt.AscendingOrder)

                
  #      except Exception:
            #QtGui.QMessageBox.about(MainWindow,'Error','Input can only be a number')
  #          pass     
            
    def setNames(self):
        
        for x in xrange(algaeTable.Total_Algae_Types):
            #self.ans_table.insertRow(0)
            self.ans_table.setItem(x,0,QtGui.QTableWidgetItem(algaeTable.Get_Name(x)))
            #self.ans_table.setItem(x,1,QtGui.QTableWidgetItem("0"))

            #change second cell to a comboBox
            combo = QtGui.QComboBox()
            combo.addItem("0-32" )
            combo.addItem("32-64")
            combo.addItem("64-128")
            combo.addItem("128-256")
            combo.addItem("256-300")

            self.ans_table.setCellWidget(x,1, combo)
            self.ans_table.item(x,0).setFlags(Qt.NoItemFlags)
            self.ans_table.sortItems(0,Qt.AscendingOrder)
            
    def resetForms(self):
      #  self.input_species.clear()
      #  self.input_count.clear()
        self.scene.clear()
        self.ans_table.setRowCount(algaeTable.Total_Algae_Types)
        self.ans_table.clearContents()
        self.setNames()

    def openResults(self):
        print "Attempting to open results"
        # Save Algae View as image for review later
        outImage = QPixmap(999, 400)
        painter = QPainter(outImage)
        
        self.scene.render(painter)
        
        if(not outImage.save(os.getcwd() + "/TempSampleRenders/Trial" + str(algaeTable.Get_Num_Trials()) + ".png")):
            print "failed to save render"

        painter.end()

        ## Record user answers
        for z in xrange(algaeTable.Total_Algae_Types):
            algaeTable.User_Guess_Record[z][algaeTable.Get_Num_Trials()] = 2
            #Current_Grid.setItem(t,3,QtGui.QTableWidgetItem(str(AlgaeSample.Get_Count_At_Trial(x,t) - 2**supToI(AlgaeSample.Get_Guess_At_Trial(x,t)[1]))))

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

    #reset all relevant variables and restart the session    
    def setSession(self): #session):
        #algaeTable.Set_Num_Trials(session.pop())
        print " New Set Session "
        algaeList[:]=[]
        algaeTable.PrepareArrays()
        self.resetForms()
        algaeTable.Generate_Sample()
        self.setUpScene(self.scene, self.view) 
           
####################
##        DISABLED
########################
##    def RTrans(self):
##        self.glWidget.setXTrans(-10)
##
##    def LTrans(self):
##        self.glWidget.setXTrans(10)
##
##    def DTrans(self):
##        self.glWidget.setYTrans(-10)
##
##    def UTrans(self):
##        self.glWidget.setYTrans(10)
##
##    
##
##    def Bigger(self):
##        scale = 1.5
##        global magLevel
##        
##        magLevel = magLevel * scale
##        self.magLabel.setText("%.2fX" %magLevel)
##        global offsetMaxX
##        offsetMaxX = offsetMaxX * scale
##        global offsetMaxY
##        offsetMaxY = offsetMaxY * scale
##        for pic in algaeList:
##            pic.setGeometry(pic.x() * scale, pic.y() * scale,pic.width() * scale,pic.height() * scale)
##    def Smaller(self):
##        scale = 1.5
##        global magLevel
##        # an expiremental temp fix
##        if(magLevel/scale > magLevelMin):
##            magLevel = magLevel/scale
##            self.magLabel.setText("%.2fX" %magLevel)
##            global offsetMinX
##            offsetMinX = offsetMinX/scale
##            global offsetMinY
##            offsetMinY = offsetMinY/scale
##            for pic in algaeList:
##                pic.setGeometry(pic.x() / scale, pic.y() / scale, pic.width() / scale, pic.height() / scale)
#####################################################################################
#####################################################################################         
            
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
  
        

###########################
##  DISABLED
#########################
##    #detect arrow keys and translates the sample accordingly
##    def keyPressEvent(self, ev):
##        if ev.key() == QtCore.Qt.Key_D:
##            self.ui.RTrans()
##        elif ev.key() == QtCore.Qt.Key_A:
##            self.ui.LTrans()
##        elif ev.key() == QtCore.Qt.Key_S:
##            self.ui.DTrans()
##        elif ev.key() == QtCore.Qt.Key_W:
##            self.ui.UTrans()

##    # test for scaling!
##    def wheelEvent(self, ev):
##        if ev.delta() > 0:
##            self.ui.Bigger()
##        else:
##            self.ui.Smaller()

        



		

		
if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    mwindow = Window()
    mwindow.ui.startUpFlag=True
    mwindow.ui.openPreferences()
    mwindow.ui.startUpFlag=False
    mwindow.show()
    sys.exit(app.exec_())
    
#what is this for? when commented out it doesnt change anything.
    '''app = QtGui.QApplication(sys.argv)
    app.setApplication('MyWindow')

    main = MyWindow(images)
    main.show()'''
		
