# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Tue Oct 15 18:40:00 2013
#      by: PyQt5 UI code generator 5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtWidgets
from PyQt4.QtWidgets import QApplication, QDialog
from results import Ui_results

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(823, 665)
        
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        
        self.findButton = QtWidgets.QPushButton(self.centralWidget)
        self.findButton.setGeometry(QtCore.QRect(730, 60, 51, 23))
        self.findButton.setObjectName("findButton")
        
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 420, 211, 171))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(60, 130, 101, 20))
        self.label.setObjectName("label")
        
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 110, 160, 29))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        
        self.magnification = QtWidgets.QDial(self.groupBox_2)
        self.magnification.setGeometry(QtCore.QRect(70, 10, 71, 81))
        self.magnification.setMinimum(0)
        self.magnification.setMaximum(100)
        self.magnification.setInvertedAppearance(False)
        self.magnification.setInvertedControls(False)
        self.magnification.setWrapping(True)
        self.magnification.setNotchesVisible(False)
        self.magnification.setObjectName("magnification")
        
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(90, 0, 66, 17))
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 40, 41, 17))
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(150, 40, 71, 17))
        self.label_6.setObjectName("label_6")
        
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(90, 80, 41, 17))
        self.label_7.setObjectName("label_7")
        
        self.searchBox = QtWidgets.QLineEdit(self.centralWidget)
        self.searchBox.setGeometry(QtCore.QRect(510, 60, 201, 20))
        self.searchBox.setText("")
        self.searchBox.setObjectName("searchBox")
        
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(250, 420, 241, 171))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(150, 130, 81, 16))
        self.label_3.setObjectName("label_3")
        
        self.coarseFocus = QtWidgets.QDial(self.groupBox)
        self.coarseFocus.setGeometry(QtCore.QRect(20, 50, 81, 71))
        self.coarseFocus.setWrapping(True)
        self.coarseFocus.setObjectName("coarseFocus")
        
        self.fineFocus = QtWidgets.QDial(self.groupBox)
        self.fineFocus.setGeometry(QtCore.QRect(130, 30, 100, 100))
        self.fineFocus.setWrapping(True)
        self.fineFocus.setObjectName("fineFocus")
        
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 91, 16))
        self.label_2.setObjectName("label_2")
        
        self.lightSelect = QtWidgets.QComboBox(self.groupBox)
        self.lightSelect.setGeometry(QtCore.QRect(20, 10, 201, 22))
        self.lightSelect.setAutoFillBackground(False)
        self.lightSelect.setObjectName("lightSelect")
        self.lightSelect.addItem("")
        self.lightSelect.addItem("")
        
        self.microscope = QtWidgets.QGraphicsView(self.centralWidget)
        self.microscope.setGeometry(QtCore.QRect(20, 20, 471, 381))
        self.microscope.setObjectName("microscope")
        
        self.submitButton = QtWidgets.QPushButton(self.centralWidget)
        self.submitButton.setGeometry(QtCore.QRect(500, 530, 301, 41))
        self.submitButton.setObjectName("submitButton")
        self.submitButton.clicked[bool].connect(self.test)
       
        self.sampleTitle = QtWidgets.QTextBrowser(self.centralWidget)
        self.sampleTitle.setGeometry(QtCore.QRect(510, 20, 271, 31))
        self.sampleTitle.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.sampleTitle.setObjectName("sampleTitle")
        
        self.AlgaeLibrary = QtWidgets.QScrollArea(self.centralWidget)
        self.AlgaeLibrary.setEnabled(False)
        self.AlgaeLibrary.setGeometry(QtCore.QRect(500, 100, 301, 421))
        self.AlgaeLibrary.setMouseTracking(True)
        self.AlgaeLibrary.setFocusPolicy(QtCore.Qt.NoFocus)
        self.AlgaeLibrary.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.AlgaeLibrary.setAcceptDrops(False)
        self.AlgaeLibrary.setToolTip("")
        self.AlgaeLibrary.setAccessibleDescription("")
        self.AlgaeLibrary.setAutoFillBackground(False)
        self.AlgaeLibrary.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.AlgaeLibrary.setLineWidth(1)
        self.AlgaeLibrary.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.AlgaeLibrary.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AlgaeLibrary.setWidgetResizable(True)
        self.AlgaeLibrary.setObjectName("AlgaeLibrary")
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 282, 419))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        self.groupBox_7 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_7.setGeometry(QtCore.QRect(20, 10, 241, 91))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        
        self.label_11 = QtWidgets.QLabel(self.groupBox_7)
        self.label_11.setGeometry(QtCore.QRect(130, 10, 81, 16))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 50, 111, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        
        self.label_12 = QtWidgets.QLabel(self.groupBox_7)
        self.label_12.setGeometry(QtCore.QRect(120, 30, 81, 16))
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.groupBox_7)
        self.graphicsView_7.setGeometry(QtCore.QRect(10, 10, 101, 71))
        self.graphicsView_7.setObjectName("graphicsView_7")
        
        self.groupBox_9 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_9.setGeometry(QtCore.QRect(20, 120, 241, 91))
        self.groupBox_9.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.groupBox_9.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.groupBox_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        
        self.label_15 = QtWidgets.QLabel(self.groupBox_9)
        self.label_15.setGeometry(QtCore.QRect(130, 10, 81, 16))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_8.setGeometry(QtCore.QRect(120, 50, 111, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        
        self.label_16 = QtWidgets.QLabel(self.groupBox_9)
        self.label_16.setGeometry(QtCore.QRect(120, 30, 81, 16))
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.groupBox_9)
        self.graphicsView_9.setGeometry(QtCore.QRect(10, 10, 101, 71))
        self.graphicsView_9.setObjectName("graphicsView_9")
        
        self.groupBox_10 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 230, 241, 91))
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        
        self.label_17 = QtWidgets.QLabel(self.groupBox_10)
        self.label_17.setGeometry(QtCore.QRect(130, 10, 81, 16))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_9.setGeometry(QtCore.QRect(120, 50, 111, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        
        self.label_18 = QtWidgets.QLabel(self.groupBox_10)
        self.label_18.setGeometry(QtCore.QRect(120, 30, 81, 16))
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        
        self.graphicsView_10 = QtWidgets.QGraphicsView(self.groupBox_10)
        self.graphicsView_10.setGeometry(QtCore.QRect(10, 10, 101, 71))
        self.graphicsView_10.setObjectName("graphicsView_10")
        
        self.groupBox_11 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_11.setGeometry(QtCore.QRect(20, 340, 241, 91))
        self.groupBox_11.setTitle("")
        self.groupBox_11.setObjectName("groupBox_11")
        
        self.label_19 = QtWidgets.QLabel(self.groupBox_11)
        self.label_19.setGeometry(QtCore.QRect(130, 10, 81, 16))
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_10.setGeometry(QtCore.QRect(120, 50, 111, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        
        self.label_20 = QtWidgets.QLabel(self.groupBox_11)
        self.label_20.setGeometry(QtCore.QRect(120, 30, 81, 16))
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        
        self.graphicsView_11 = QtWidgets.QGraphicsView(self.groupBox_11)
        self.graphicsView_11.setGeometry(QtCore.QRect(10, 10, 101, 71))
        self.graphicsView_11.setObjectName("graphicsView_11")
        
        self.AlgaeLibrary.setWidget(self.scrollAreaWidgetContents)
       
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 823, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionControls = QtWidgets.QAction(MainWindow)
        self.actionControls.setObjectName("actionControls")
        self.actionImport_Sample = QtWidgets.QAction(MainWindow)
        self.actionImport_Sample.setObjectName("actionImport_Sample")
        self.actionCreate_New_Sample = QtWidgets.QAction(MainWindow)
        self.actionCreate_New_Sample.setObjectName("actionCreate_New_Sample")
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
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def test(self,val):
        ui=QDialog();
        self.resultsDialog.setupUi(ui)
        ui.show()
        self.resultsDialog.exec_();

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.findButton.setText(_translate("MainWindow", "Find"))
        self.label.setText(_translate("MainWindow", "Magnification"))
        self.label_4.setText(_translate("MainWindow", "200X"))
        self.label_5.setText(_translate("MainWindow", "100X"))
        self.label_6.setText(_translate("MainWindow", "400X"))
        self.label_7.setText(_translate("MainWindow", "600X"))
        self.label_3.setText(_translate("MainWindow", "Fine Focus"))
        self.label_2.setText(_translate("MainWindow", "Coarse Focus"))
        self.lightSelect.setItemText(0, _translate("MainWindow", "Natural  Light"))
        self.lightSelect.setItemText(1, _translate("MainWindow", "Solar"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.sampleTitle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Name"))
        self.label_12.setText(_translate("MainWindow", "Count:"))
        self.label_15.setText(_translate("MainWindow", "Name"))
        self.label_16.setText(_translate("MainWindow", "Count:"))
        self.label_17.setText(_translate("MainWindow", "Name"))
        self.label_18.setText(_translate("MainWindow", "Count:"))
        self.label_19.setText(_translate("MainWindow", "Name"))
        self.label_20.setText(_translate("MainWindow", "Count:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionAbout.setText(_translate("MainWindow", "About..."))
        self.actionControls.setText(_translate("MainWindow", "Controls"))
        self.actionImport_Sample.setText(_translate("MainWindow", "Import Existing Sample"))
        self.actionCreate_New_Sample.setText(_translate("MainWindow", "Create New Sample"))

