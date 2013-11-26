# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results.ui'
#
# Created: Sat Oct 19 18:44:45 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!


import sys, os
from PyQt4 import QtCore, QtGui,QtOpenGL
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from algaeTable import *
from Globals import *

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

class Ui_results(object):

    

    
    
    def setupUi(self, results, AlgaeSample,ansTable):
        results.setObjectName(_fromUtf8("results"))
        results.setFixedSize(755, 569)

        self.pushButton = QtGui.QPushButton(results)
        self.pushButton.setGeometry(QtCore.QRect(558, 520, 181, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(results.done)

        self.label = QtGui.QLabel(results)
        self.label.setGeometry(QtCore.QRect(248, 523, 91, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        
        self.AlgaeLibrary = QtGui.QScrollArea(results)
        self.AlgaeLibrary.setEnabled(True)
        self.AlgaeLibrary.setGeometry(QtCore.QRect(8, 80, 731, 411))
        self.AlgaeLibrary.setMouseTracking(True)
        self.AlgaeLibrary.setFocusPolicy(QtCore.Qt.NoFocus)
        self.AlgaeLibrary.setAcceptDrops(True)
        self.AlgaeLibrary.setToolTip(_fromUtf8(""))
        self.AlgaeLibrary.setAutoFillBackground(True)
        self.AlgaeLibrary.setFrameShape(QtGui.QFrame.StyledPanel)
        self.AlgaeLibrary.setFrameShadow(QtGui.QFrame.Sunken)
        self.AlgaeLibrary.setLineWidth(1)
        self.AlgaeLibrary.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.AlgaeLibrary.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AlgaeLibrary.setWidgetResizable(True)
        self.AlgaeLibrary.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AlgaeLibrary.setObjectName(_fromUtf8("AlgaeLibrary"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -170, 708, 579))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.formLayout = QtGui.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))

        ## New Layout
        for x in xrange(AlgaeSample.Total_Algae_Types):
            ## Header
            CurrentGridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
            CurrentGridLayout.setMargin(0)
            # Name
            CurrentLabel_Your_Answer = QtGui.QLabel(self.scrollAreaWidgetContents)
            CurrentLabel_Your_Answer.setAlignment(QtCore.Qt.AlignCenter)
            CurrentLabel_Your_Answer.setText(_fromUtf8(AlgaeSample.Get_Name(x)))
            CurrentGridLayout.addWidget(CurrentLabel_Your_Answer, 0, 0, 1, 1)
            # Standard Deviation
            L_Std_Dv = QtGui.QLabel(self.scrollAreaWidgetContents)
            L_Std_Dv.setAlignment(QtCore.Qt.AlignCenter)
            L_Std_Dv.setText("Standard deviation: 0")
            CurrentGridLayout.addWidget(L_Std_Dv, 0, 1, 1, 1)
            # Geometric Mean
            L_G_Mean = QtGui.QLabel(self.scrollAreaWidgetContents)
            L_G_Mean.setAlignment(QtCore.Qt.AlignCenter)
            L_G_Mean.setText("Geometric Mean: " + str(AlgaeSample.Get_G_Mean(x)))
            CurrentGridLayout.addWidget(L_G_Mean, 0, 2, 1, 1)
            # Add Header
            self.formLayout.addRow(CurrentGridLayout)


            ## Table
            Current_Grid = QtGui.QTableWidget(self.scrollAreaWidgetContents)
            Current_Grid.setGeometry(QtCore.QRect(550, 470, 411, 181))
            Current_Grid.setObjectName(_fromUtf8("AlgaeGrid"))
            Current_Grid.setColumnCount(5)
            Current_Grid.setRowCount(AlgaeSample.Total_Trials)
            Current_Grid.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
            Current_Grid.verticalHeader().setVisible(False)
            Current_Grid.setHorizontalHeaderLabels(['Trial', 'Guess', 'Actual', 'Difference', 'Image'])
            self.formLayout.addRow(Current_Grid)

            class QButton(QtGui.QWidget):
                def __init__(self, fileName, parent = None):
                    QtGui.QWidget.__init__(self, parent)
                    self.button = QtGui.QPushButton('View', self)
                    self.fileName = fileName
                    self.button.clicked.connect(self.Open_View)

                class Ui_View(object):
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
                    def setupUi(self, View, FileName):
                        
                        View.setObjectName(_fromUtf8(FileName))
                        View.setFixedSize(999, 400)
                        View.setWindowTitle(_translate(FileName, FileName, None))
                        self.scene = QtGui.QGraphicsScene(0, 0, 999, 400)
                        self.centralWidget = QtGui.QGraphicsView(self.scene, View)
                        self.pic = Pixmap(QtGui.QPixmap(os.getcwd() + "/TempSampleRenders/"+FileName), 1)
                        print os.getcwd() + "/TempSampleRenders/"+FileName
                        self.pic.pos = QtCore.QPointF(0,0)
                        self.scene.addItem(self.pic.pixmap_item)

                def Open_View(self):
                    Open_View_Dialog=self.Ui_View()
                    View_Ui=QtGui.QDialog();
                    Open_View_Dialog.setupUi(View_Ui, self.fileName)
                    View_Ui.setModal(True) 
                    View_Ui.exec_()

            
            
            # Fill table
            for t in xrange(AlgaeSample.Total_Trials):
                #Current_Grid.insertRow(0)
                Current_Grid.setItem(t,0,QtGui.QTableWidgetItem(str(t+1)))
                Current_Grid.setItem(t,1,QtGui.QTableWidgetItem(str(AlgaeSample.Get_Guess_At_Trial(x,t))))
                Current_Grid.setItem(t,2,QtGui.QTableWidgetItem(_translate("results",str(AlgaeSample.Get_Count_At_Trial(x,t)), None)))
                Current_Grid.setItem(t,3,QtGui.QTableWidgetItem(str(AlgaeSample.Get_Difference_At_Trial(x,t))))
                Current_Grid.setItem(t,4,QtGui.QTableWidgetItem("Coming soon"))
                View_Button = QButton("Trial" + str(t+1) + ".png")
                Current_Grid.setCellWidget(t,4, View_Button)


##        # Old Layout
##        for x in xrange(AlgaeSample.Total_Algae_Types):
##            Index = 7 + x
##            CurrentGroupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
##            CurrentGroupBox.setTitle(_fromUtf8(AlgaeSample.Get_Name(x)))
##            CurrentGroupBox.setObjectName(_fromUtf8("CurrentGroupBox"))
##
##            CurrentLayoutWidget = QtGui.QWidget(CurrentGroupBox)
##            CurrentLayoutWidget.setGeometry(QtCore.QRect(10, 20, 600, 47))
##            CurrentLayoutWidget.setObjectName(_fromUtf8("CurrentLayoutWidget"))
##
##            CurrentGridLayout = QtGui.QGridLayout(CurrentLayoutWidget)
##            CurrentGridLayout.setMargin(0)
##            CurrentGridLayout.setObjectName(_fromUtf8("CurrentGridLayout"))
##
##            CurrentLabel_Your_Answer = QtGui.QLabel(CurrentLayoutWidget)
##            CurrentLabel_Your_Answer.setAlignment(QtCore.Qt.AlignCenter)
##            CurrentLabel_Your_Answer.setObjectName(_fromUtf8("CurrentLabel_Your_Answer"))
##            CurrentGridLayout.addWidget(CurrentLabel_Your_Answer, 0, 0, 1, 1)
##
##            CurrentLabel_Correct_Answer = QtGui.QLabel(CurrentLayoutWidget)
##            CurrentLabel_Correct_Answer.setAlignment(QtCore.Qt.AlignCenter)
##            CurrentLabel_Correct_Answer.setObjectName(_fromUtf8("CurrentLabel_Correct_Answer"))
##            CurrentGridLayout.addWidget(CurrentLabel_Correct_Answer, 0, 1, 1, 1)
##
##            CurrentLabel_Difference = QtGui.QLabel(CurrentLayoutWidget)
##            CurrentLabel_Difference.setAlignment(QtCore.Qt.AlignCenter)
##            CurrentLabel_Difference.setObjectName(_fromUtf8("label_36"))
##            CurrentGridLayout.addWidget(CurrentLabel_Difference, 0, 2, 1, 1)
##            
##            Label_User_Answer = QtGui.QLabel(CurrentLayoutWidget)
##            Label_User_Answer.setObjectName(_fromUtf8("Label_User_Answer"))
##            Label_User_Answer.setAlignment(QtCore.Qt.AlignCenter)
##            CurrentGridLayout.addWidget(Label_User_Answer, 1, 0, 1, 1)
##
##            Label_Correct_Answer = QtGui.QLabel(CurrentLayoutWidget)
##            Label_Correct_Answer.setObjectName(_fromUtf8("Label_Correct_Answer"))
##            Label_Correct_Answer.setAlignment(QtCore.Qt.AlignCenter)
##            CurrentGridLayout.addWidget(Label_Correct_Answer, 1, 1, 1, 1)
##
##            Label_Num_Difference = QtGui.QLabel(CurrentLayoutWidget)
##            Label_Num_Difference.setObjectName(_fromUtf8("Label_Num_Difference"))
##            Label_Num_Difference.setAlignment(QtCore.Qt.AlignCenter)
##            CurrentGridLayout.addWidget( Label_Num_Difference, 1, 2, 1, 1)
##            self.formLayout.setWidget(Index, QtGui.QFormLayout.FieldRole, CurrentGroupBox)
##
##            CurrentLabel_Your_Answer.setText(_translate("results", "Your Answer", None))
##            CurrentLabel_Correct_Answer.setText(_translate("results", "Correct Answer", None))
##            CurrentLabel_Difference.setText(_translate("results", "Difference", None))
##            Label_Correct_Answer.setText(_translate("results",str(AlgaeSample.Get_Count(x)), None))
##             
##            Label_User_Answer.setText(_translate("results", self.getUserCount(x,AlgaeSample,ansTable), None))
##            Label_Num_Difference.setText(_translate("results", str(int(Label_User_Answer.text()) - int(Label_Correct_Answer.text())), None))
##
##            # Add graphic
##            #CurrentGraphicsView = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
##            CurrentGraphicsView = QtGui.QLabel(self.scrollAreaWidgetContents)
##            CurrentGraphicsView.setObjectName(_fromUtf8("CurrentGraphicsView"))
##            self.formLayout.setWidget(Index, QtGui.QFormLayout.LabelRole, CurrentGraphicsView)
##            CurrentGraphicsView.setPixmap(QtGui.QPixmap(os.getcwd() + "/Assets/20um/"+AlgaeSample.Get_File_Name(x)))
##            CurrentGraphicsView.setFixedWidth(75)
##            CurrentGraphicsView.setFixedHeight(75)
##            #CurrentGraphicsView.setGeometry(0,0,90,90)
##            CurrentGraphicsView.setScaledContents(True)
##            backGroundColorString = "44,121,176,255"
##            CurrentGraphicsView.setStyleSheet("background-color: rgba("+backGroundColorString+")" )

        self.AlgaeLibrary.setWidget(self.scrollAreaWidgetContents)
        self.groupBox = QtGui.QGroupBox(results)
        self.groupBox.setGeometry(QtCore.QRect(8, 10, 731, 51))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_41 = QtGui.QLabel(self.groupBox)
        self.label_41.setGeometry(QtCore.QRect(170, 0, 381, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(24)
        self.label_41.setFont(font)
        self.label_41.setTextFormat(QtCore.Qt.RichText)
        self.label_41.setScaledContents(False)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.lineEdit = QtGui.QLineEdit(results)
        self.lineEdit.setGeometry(QtCore.QRect(350, 520, 181, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        

        self.retranslateUi(results, AlgaeSample)
        QtCore.QMetaObject.connectSlotsByName(results)

    #Access the table widget and extract the users answers    
    def getUserCount(self, algaeIndex,algaeSample,ansTable):
        tableItem= ansTable.findItems(algaeSample.Get_Name(algaeIndex),QtCore.Qt.MatchFixedString)
        
        if(len(tableItem) > 0):
            #return ansTable.item(tableItem[0].row(),1).text()
            #figure out how to get a value from a combobox?
            return "coming soon."
        else:
            return "0"
        
    def closeEvent(self):
        print("event")
        
    
    def retranslateUi(self, results, AlgaeSample):
        results.setWindowTitle(_translate("Counting Results", "Dialog", None))
        self.pushButton.setText(_translate("results", "Continue", None))
        self.label.setText(_translate("results", "Overall Score", None))
        self.label_41.setText(_translate("results", "Results", None))
