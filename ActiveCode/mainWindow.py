# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Oct 19 18:39:35 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!
import sys, os
import math
from random import randint
from PyQt4 import QtCore, QtGui,QtOpenGL
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from results import Ui_results
from PIL import Image
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

try:
    from OpenGL import GL
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "OpenGL")
    sys.exit(1)
#####################################################################################
#####################################################################################


# Please keep the values in the following two variables the same
# This is terrible, please find a way to convert QColor to the csv in backGroundColorString
# Or find a way to set the pic (a QLabel) background color without a style sheet
backGroundColor = QColor(44,121,176,255)
backGroundColorString = "44,121,176,255"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(999, 792)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.glWidget = GLWidget(self.centralWidget)

        # Puts images in the glWidget!!!!!
        pic = QtGui.QLabel(self.glWidget)
        pic.setGeometry(10,10,79.5,62.75)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/Assets/attempt001.png"))
        pic.setScaledContents(True)
        pic.setStyleSheet("background-color: rgba("+backGroundColorString+")" )

        pic = QtGui.QLabel(self.glWidget)
        pic.setGeometry(350,277,79.5,62.75)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/Assets/attempt001.png"))
        pic.setScaledContents(True)
        pic.setStyleSheet("background-color: rgba("+backGroundColorString+")" )

        pic = QtGui.QLabel(self.glWidget)
        pic.setGeometry(115,347,79.5,62.75)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/Assets/attempt001.png"))
        pic.setScaledContents(True)
        pic.setStyleSheet("background-color: rgba("+backGroundColorString+")" )

        pic = QtGui.QLabel(self.glWidget)
        pic.setGeometry(377,100,79.5,62.75)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/Assets/attempt001.png"))
        pic.setScaledContents(True)
        pic.setStyleSheet("background-color: rgba("+backGroundColorString+")" )

        # Controls
        self.findButton = QtGui.QPushButton(self.centralWidget)
        self.findButton.setGeometry(QtCore.QRect(870, 430, 91, 31))
        self.findButton.setObjectName(_fromUtf8("findButton"))
        
		
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
        
        self.input_species = QtGui.QLineEdit(self.centralWidget)
        self.input_species.setGeometry(QtCore.QRect(550, 430, 181, 31))
        self.input_species.setText(_fromUtf8(""))
        self.input_species.setObjectName(_fromUtf8("input_species"))
               
        self.submit_button = QtGui.QPushButton(self.centralWidget)
        self.submit_button.setGeometry(QtCore.QRect(640, 660, 231, 41))
        self.submit_button.setObjectName(_fromUtf8("submit_button"))
		
        self.groupBox_move = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_move.setGeometry(QtCore.QRect(30, 430, 291, 271))
        self.groupBox_move.setTitle(_fromUtf8(""))
        self.groupBox_move.setObjectName(_fromUtf8("groupBox_move"))
        self.groupBox_move.keyPressEvent = lambda event: event.ignore()
        
        self.up_button = QtGui.QPushButton(self.groupBox_move)
        self.up_button.setGeometry(QtCore.QRect(100, 40, 71, 28))
        self.up_button.setObjectName(_fromUtf8("up_button"))
        
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_move)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 100, 61, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        
        self.right_button = QtGui.QPushButton(self.groupBox_move)
        self.right_button.setGeometry(QtCore.QRect(192, 100, 71, 28))
        self.right_button.setObjectName(_fromUtf8("right_button"))
        
        self.down_button = QtGui.QPushButton(self.groupBox_move)
        self.down_button.setGeometry(QtCore.QRect(100, 160, 71, 28))
        self.down_button.setObjectName(_fromUtf8("down_button"))
        
        self.label_2 = QtGui.QLabel(self.groupBox_move)
        self.label_2.setGeometry(QtCore.QRect(120, 240, 71, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        self.input_count = QtGui.QLineEdit(self.centralWidget)
        self.input_count.setGeometry(QtCore.QRect(750, 430, 111, 31))
        self.input_count.setText(_fromUtf8(""))
        self.input_count.setObjectName(_fromUtf8("input_count"))
        
        self.ans_table = QtGui.QTableView(self.centralWidget)
        self.ans_table.setGeometry(QtCore.QRect(550, 470, 411, 181))
        self.ans_table.setObjectName(_fromUtf8("ans_table"))
        
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
        
        self.actionControls = QtGui.QAction(MainWindow)
        self.actionControls.setObjectName(_fromUtf8("actionControls"))
        .5
        self.actionImport_Sample = QtGui.QAction(MainWindow)
        self.actionImport_Sample.setObjectName(_fromUtf8("actionImport_Sample"))
        
        self.actionCreate_New_Sample = QtGui.QAction(MainWindow)
        self.actionCreate_New_Sample.setObjectName(_fromUtf8("actionCreate_New_Sample"))
        
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_Sample)
        self.menuFile.addAction(self.actionCreate_New_Sample)
        
        self.menuTools.addAction(self.actionAbout)
        self.menuTools.addAction(self.actionControls)
        
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.resultsDialog=Ui_results()
        
        self.submit_button.clicked.connect(self.openResults)
        
        self.right_button.clicked.connect(self.RTrans)
        self.pushButton_2.clicked.connect(self.LTrans)
        self.up_button.clicked.connect(self.UTrans)
        self.down_button.clicked.connect(self.DTrans)
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
        self.pushButton_2.setText(_translate("MainWindow", "Left", None))
        self.right_button.setText(_translate("MainWindow", "Right", None))
        self.down_button.setText(_translate("MainWindow", "Down", None))
        self.label_2.setText(_translate("MainWindow", "Movement", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuTools.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionAbout.setText(_translate("MainWindow", "About...", None))
        self.actionControls.setText(_translate("MainWindow", "Controls", None))
        self.actionImport_Sample.setText(_translate("MainWindow", "Import Existing Sample", None))
        self.actionCreate_New_Sample.setText(_translate("MainWindow", "Create New Sample", None))

    def openResults(self,val):
        ui=QtGui.QDialog();
        self.resultsDialog.setupUi(ui)
        ui.show()
        ui.exec_()

    def RTrans(self):
        self.glWidget.setXTrans(.5)

    def LTrans(self):
        self.glWidget.setXTrans(-.5)

    def DTrans(self):
        self.glWidget.setYTrans(.5)

    def UTrans(self):
        self.glWidget.setYTrans(-.5)    
    
#####################################################################################
#####################################################################################         
            
class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
       
        self.ui.setupUi(self)
    #detect arrow keys and translates the sample accordingly
    def keyPressEvent(self, ev):
         if ev.key() == QtCore.Qt.Key_Right:
            self.ui.glWidget.setXTrans(0.5)
         elif ev.key() == QtCore.Qt.Key_Left:
            self.ui.glWidget.setXTrans(-0.5)
         elif ev.key() == QtCore.Qt.Key_Down:
            self.ui.glWidget.setYTrans(0.5)
         elif ev.key() == QtCore.Qt.Key_Up:
            self.ui.glWidget.setYTrans(-0.5)
    
#####################################################################################
#####################################################################################
   
class algaes:
    #texture:pass name of image to be uses as texture?
    def __init__(self, x,y):
        #will contain the name of the list
        self.object = 0
        self.d =((randint(0,10) / 10.00) - 0.5)
        self.x1 = x + self.d
        self.y1 = y + self.d
        self.x2 = -y + self.d
        self.y2 = -x + self.d
        self.posX=((randint(0,10) / 10.00) - 0.5);
        self.posY=((randint(0,10) / 10.00) - 0.5);
        #self.texture=texture

    def Textureize(self):
        self.y = 0
        
#####################################################################################
#####################################################################################
 #This is a class that Sound. is creating for inserting an image and seeing if
#we can add transparency and code used from (second link provided)
    #Still need to figure out things like incorporating vertices for the picture
    #on the the screen and stuff.
class ImageCh(QtGui.QWidget) :
    def _init_(self,image, parent=None) :
        super(ImageCh, self)._init_(parent)

        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.addItems(images)

        self.layout = QtGui.QVBoxLayout(self)
        self.layout.addWidget(self.comboBox)

class MyWindow(QtGui.QWidget):
    def _init_(self,images, parent=None):
        super(MyWindow, self)._init_(parent)
        self.label = QTGui.QLabel(self)

        self.imageChanger = ImageCh(images)
        self.imageChanger = move(self.imageChanger.pos().y(), self.imageChanger.pos().x() + 100)
        self.imageChanger.show()
        self.ImageChanger.comboBox.currentIndexChanger[str].connect(self.ChangeImage)

        self.layout = QtGui.QVBoxLayout(self)
        self.layout.addWidget(self.label)
    @QtCore.pyqtSlot(str)
    def changeImage(self, pathToImage):
        pixmap = QtGui.QPixmap(pathToImage)
        self.label.setPixmap(pixmap)
        
#####################################################################################
#####################################################################################
class GLWidget(QtOpenGL.QGLWidget):
    xRotationChanged = QtCore.pyqtSignal(int)
    yRotationChanged = QtCore.pyqtSignal(int)
    zRotationChanged = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)

        self.object = 0
        self.xTrans = 0
        self.yTrans = 0

        self.algaeList = []

        self.lastPos = QtCore.QPoint()

        self.trolltechGreen = QtGui.QColor.fromCmykF(0.450, 0.0, 1.0, 0.0)
        self.trolltechPurple = QtGui.QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)
        

    def minimumSizeHint(self):
        return QtCore.QSize(50, 50)

    def sizeHint(self):
        return QtCore.QSize(1000, 400)

    def setXTrans(self, trans):
        for algae in self.algaeList:
            algae.posX = trans+algae.posX
            #self.yRotationChanged.emit(angle)
            self.updateGL()#calls glDraw() which calls paintGl()

    def setYTrans(self, trans):
        for algae in self.algaeList:
            algae.posY = trans+algae.posY;
            #self.yRotationChanged.emit(angle)
            self.updateGL()#calls glDraw() which calls paintGl()         

    def initializeGL(self):
        self.qglClearColor(backGroundColor)
        self.makeObject()
        GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_CULL_FACE)

    def paintGL(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        #replace current matrix with identity matrix
        GL.glLoadIdentity()

        for algae in self.algaeList:
            GL.glTranslated(algae.posX, algae.posY, -10.0)
            #calls the list saved in object variable
            GL.glCallList(algae.object)

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0:
            return
        
        GL.glViewport(0,0,width,height)

        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        #clipping? 
        GL.glOrtho(-1, +1, +0.5, -0.5, 4.0, 15.0)
        GL.glMatrixMode(GL.GL_MODELVIEW)

    def mousePressEvent(self, event):
        self.lastPos = event.pos()

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()
        
##        if event.buttons() & QtCore.Qt.LeftButton:
##            self.setXRotation(self.xRot + 8 * dy)
##            self.setYRotation(self.yRot + 8 * dx)
##        elif event.buttons() & QtCore.Qt.RightButton:
##            self.setXRotation(self.xRot + 8 * dy)
##            self.setZRotation(self.zRot + 8 * dx)
##
##        self.lastPos = event.pos()
        


    def makeObject(self):
        #reserves a name for the list
        genList = GL.glGenLists(1)
        #uses name created above to make a list?
        GL.glNewList(genList, GL.GL_COMPILE)

        GL.glBegin(GL.GL_QUADS)
        #everything between here and "end" is in list?
        x = 0.2
        y = -0.0
        #create a new algae object
        self.algaeList.append(algaes(x,y))
        self.Create_Square(self.algaeList[-1].x1, self.algaeList[-1].y1,
                            self.algaeList[-1].x2, self.algaeList[-1].y2,self.trolltechGreen)
        GL.glEnd()
        #GL.glEndList()
        self.algaeList[-1].object=genList
        self.algaeList[-1].posX= ((randint(0,10) / 10.00) - 0.5)
        print genList
        #enList = GL.glGenLists(1)
        #GL.glNewList(enList, GL.GL_COMPILE)

        GL.glBegin(GL.GL_QUADS)
        x = 0.5
        y = -0.12
        self.algaeList.append(algaes(x,y))
        self.quad(self.algaeList[-1].x1, self.algaeList[-1].y1,
                  self.algaeList[-1].x2, self.algaeList[-1].y2,
                  self.algaeList[-1].y2, self.algaeList[-1].x2,
                  self.algaeList[-1].y1, self.algaeList[-1].x1,self.trolltechPurple)
        GL.glEnd()
        self.algaeList[-1].posY= ((randint(0,10) / 10.00) - 0.5)
        self.algaeList[-1].posX= ((randint(0,10) / 10.00) - 0.5)
        self.algaeList[-1].object=genList
        self.algaeList[-1].posY= ((randint(0,10) / 10.00) - 0.5)
        self.algaeList[-1].posX= ((randint(0,10) / 10.00) - 0.5)
        print genList
        #enList = GL.glGenLists(1)
        #GL.glNewList(enList, GL.GL_COMPILE)

        GL.glBegin(GL.GL_QUADS)
        x = 0.5
        y = -0.12
        self.algaeList.append(algaes(x,y))
        self.quad(self.algaeList[-1].x1, self.algaeList[-1].y1,
                  self.algaeList[-1].x2, self.algaeList[-1].y2,
                  self.algaeList[-1].y2, self.algaeList[-1].x2,
                  self.algaeList[-1].y1, self.algaeList[-1].x1,self.trolltechPurple)
        GL.glEnd()
        self.algaeList[-1].posY= ((randint(0,10) / 10.00) - 0.5)

        
        GL.glEndList()
        self.algaeList[-1].object=genList
        self.algaeList[-1].posY= ((randint(0,10) / 10.00) - 0.5)
        #self.algaeList[-1].object=enList
        self.algaeList[-1].posX=-0.5
        print "two"
        #print enList


    
    
    #makes vertices
    def quad(self, x1, y1, x2, y2, x3, y3, x4, y4,color):
        self.qglColor(color)

        GL.glVertex2d(x1, y1)
        GL.glVertex2d(x2, y2)
        GL.glVertex2d(x3, y3)
        GL.glVertex2d(x4, y4)

    def Create_Square(self, x1, x2, y1, y2,color):
        self.qglColor(color)

        GL.glVertex2d(0.2, 0.2)
        GL.glVertex2d(0.2, -0.2)
        GL.glVertex2d(-0.2, -0.2)
        GL.glVertex2d(-0.2, 0.2)

#dont know what this does...........
##        GL.glVertex2d(x4, y4)
##        GL.glVertex2d(x3, y3)
##        GL.glVertex2d(x2, y2)
##        GL.glVertex2d(x1, y1)
#####################################################################################

		

		
if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    mwindow = Window()

    mwindow.show()
    sys.exit(app.exec_())

    images = [ "/testpic1",
               "/testpic2"
               ]
    app = QtGui.QApplication(sys.argv)
    app.setApplication('MyWindow')

    main = MyWindow(images)
    main.show()
		
