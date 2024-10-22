# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Oct 19 18:39:35 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!
import sys
import math
from PyQt4 import QtCore, QtGui,QtOpenGL
from results import Ui_results
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
    QtGui.QMessageBox.critical(None, "OpenGL hellogl",
            "PyOpenGL must be installed to run this example.")
    sys.exit(1)

	
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(999, 792)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.glWidget = GLWidget(self.centralWidget)

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
    
            
            
            
class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
       
        self.ui.setupUi(self)

    
    
   
       
  
            		
class GLWidget(QtOpenGL.QGLWidget):
    xRotationChanged = QtCore.pyqtSignal(int)
    yRotationChanged = QtCore.pyqtSignal(int)
    zRotationChanged = QtCore.pyqtSignal(int)
    x = 0
    y = 0
    z = -10

    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)

        self.object = 0
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0

        self.lastPos = QtCore.QPoint()

        self.trolltechGreen = QtGui.QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QtGui.QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)

    def minimumSizeHint(self):
        return QtCore.QSize(50, 50)

    def sizeHint(self):
        return QtCore.QSize(1000, 400)

    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = angle
            self.xRotationChanged.emit(angle)
            self.updateGL()

    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
            self.yRotationChanged.emit(angle)
            self.updateGL()

    def setZRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.zRot:
            self.zRot = angle
            self.zRotationChanged.emit(angle)
            self.updateGL()

    def initializeGL(self):
        self.qglClearColor(self.trolltechPurple.dark())
        self.object = self.makeObject()
        GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_CULL_FACE)

    def paintGL(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glLoadIdentity()
        GL.glTranslated(self.x,self.y,self.z)
        GL.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        GL.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        GL.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)
        GL.glCallList(self.object)

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0:
            return

        GL.glViewport((width - side) / 2, (height - side) / 2, side, side)

        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        GL.glMatrixMode(GL.GL_MODELVIEW)

    def mousePressEvent(self, event):
        self.lastPos = event.pos()

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & QtCore.Qt.LeftButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setYRotation(self.yRot + 8 * dx)
        elif event.buttons() & QtCore.Qt.RightButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setZRotation(self.zRot + 8 * dx)

        self.lastPos = event.pos()
        
    

    def makeObject(self):
        genList = GL.glGenLists(1)
        GL.glNewList(genList, GL.GL_COMPILE)

        GL.glBegin(GL.GL_QUADS)

        x1 = +0.06
        y1 = -0.14
        x2 = +0.14
        y2 = -0.06
        x3 = +0.08
        y3 = +0.00
        x4 = +0.30
        y4 = +0.22

        self.quad(x1, y1, x2, y2, y2, x2, y1, x1)
        self.quad(x3, y3, x4, y4, y4, x4, y3, x3)

        self.extrude(x1, y1, x2, y2)
        self.extrude(x2, y2, y2, x2)
        self.extrude(y2, x2, y1, x1)
        self.extrude(y1, x1, x1, y1)
        self.extrude(x3, y3, x4, y4)
        self.extrude(x4, y4, y4, x4)
        self.extrude(y4, x4, y3, x3)

        NumSectors = 200

        for i in range(NumSectors):
            angle1 = (i * 2 * math.pi) / NumSectors
            x5 = 0.30 * math.sin(angle1)
            y5 = 0.30 * math.cos(angle1)
            x6 = 0.20 * math.sin(angle1)
            y6 = 0.20 * math.cos(angle1)

            angle2 = ((i + 1) * 2 * math.pi) / NumSectors
            x7 = 0.20 * math.sin(angle2)
            y7 = 0.20 * math.cos(angle2)
            x8 = 0.30 * math.sin(angle2)
            y8 = 0.30 * math.cos(angle2)

            self.quad(x5, y5, x6, y6, x7, y7, x8, y8)

            self.extrude(x6, y6, x7, y7)
            self.extrude(x8, y8, x5, y5)

        GL.glEnd()
        GL.glEndList()

        return genList

    def quad(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.qglColor(self.trolltechGreen)

        GL.glVertex3d(x1, y1, -0.05)
        GL.glVertex3d(x2, y2, -0.05)
        GL.glVertex3d(x3, y3, -0.05)
        GL.glVertex3d(x4, y4, -0.05)

        GL.glVertex3d(x4, y4, +0.05)
        GL.glVertex3d(x3, y3, +0.05)
        GL.glVertex3d(x2, y2, +0.05)
        GL.glVertex3d(x1, y1, +0.05)

    def extrude(self, x1, y1, x2, y2):
        self.qglColor(self.trolltechGreen.dark(250 + int(100 * x1)))

        GL.glVertex3d(x1, y1, +0.05)
        GL.glVertex3d(x2, y2, +0.05)
        GL.glVertex3d(x2, y2, -0.05)
        GL.glVertex3d(x1, y1, -0.05)

    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle

    def moveRight(self):
        self.x = self.x + 4
        self.updateGL()

    def keyPressEvent(self, event):
        print "asdf"
        if(QtCore.Qt.Right):
            self.moveRight()
		

		
if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    mwindow = Window()

    mwindow.show()
    sys.exit(app.exec_())
		
