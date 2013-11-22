# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results.ui'


import sys, os

from PyQt4 import QtCore, QtGui
from algaeTable import *

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
        results.resize(755, 569)

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



        for x in xrange(AlgaeSample.Total_Algae_Types):
            Index = 7 + x
            CurrentGroupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
            CurrentGroupBox.setTitle(_fromUtf8(AlgaeSample.Get_Name(x)))
            CurrentGroupBox.setObjectName(_fromUtf8("CurrentGroupBox"))

            CurrentLayoutWidget = QtGui.QWidget(CurrentGroupBox)
            CurrentLayoutWidget.setGeometry(QtCore.QRect(10, 20, 600, 47))
            CurrentLayoutWidget.setObjectName(_fromUtf8("CurrentLayoutWidget"))

            CurrentGridLayout = QtGui.QGridLayout(CurrentLayoutWidget)
            CurrentGridLayout.setMargin(0)
            CurrentGridLayout.setObjectName(_fromUtf8("CurrentGridLayout"))

            CurrentLabel_Your_Answer = QtGui.QLabel(CurrentLayoutWidget)
            CurrentLabel_Your_Answer.setAlignment(QtCore.Qt.AlignCenter)
            CurrentLabel_Your_Answer.setObjectName(_fromUtf8("CurrentLabel_Your_Answer"))
            CurrentGridLayout.addWidget(CurrentLabel_Your_Answer, 0, 0, 1, 1)

            CurrentLabel_Correct_Answer = QtGui.QLabel(CurrentLayoutWidget)
            CurrentLabel_Correct_Answer.setAlignment(QtCore.Qt.AlignCenter)
            CurrentLabel_Correct_Answer.setObjectName(_fromUtf8("CurrentLabel_Correct_Answer"))
            CurrentGridLayout.addWidget(CurrentLabel_Correct_Answer, 0, 1, 1, 1)

            CurrentLabel_Difference = QtGui.QLabel(CurrentLayoutWidget)
            CurrentLabel_Difference.setAlignment(QtCore.Qt.AlignCenter)
            CurrentLabel_Difference.setObjectName(_fromUtf8("label_36"))
            CurrentGridLayout.addWidget(CurrentLabel_Difference, 0, 2, 1, 1)
            
            Label_User_Answer = QtGui.QLabel(CurrentLayoutWidget)
            Label_User_Answer.setObjectName(_fromUtf8("Label_User_Answer"))
            Label_User_Answer.setAlignment(QtCore.Qt.AlignCenter)
            CurrentGridLayout.addWidget(Label_User_Answer, 1, 0, 1, 1)

            Label_Correct_Answer = QtGui.QLabel(CurrentLayoutWidget)
            Label_Correct_Answer.setObjectName(_fromUtf8("Label_Correct_Answer"))
            Label_Correct_Answer.setAlignment(QtCore.Qt.AlignCenter)
            CurrentGridLayout.addWidget(Label_Correct_Answer, 1, 1, 1, 1)

            Label_Num_Difference = QtGui.QLabel(CurrentLayoutWidget)
            Label_Num_Difference.setObjectName(_fromUtf8("Label_Num_Difference"))
            Label_Num_Difference.setAlignment(QtCore.Qt.AlignCenter)
            CurrentGridLayout.addWidget( Label_Num_Difference, 1, 2, 1, 1)
            self.formLayout.setWidget(Index, QtGui.QFormLayout.FieldRole, CurrentGroupBox)

            CurrentLabel_Your_Answer.setText(_translate("results", "Your Answer", None))
            CurrentLabel_Correct_Answer.setText(_translate("results", "Correct Answer", None))
            CurrentLabel_Difference.setText(_translate("results", "Difference", None))
            Label_Correct_Answer.setText(_translate("results",str(AlgaeSample.Get_Count(x)), None))
             
            Label_User_Answer.setText(_translate("results", self.getUserCount(x,AlgaeSample,ansTable), None))
            Label_Num_Difference.setText(_translate("results", str(int(Label_User_Answer.text()) - int(Label_Correct_Answer.text())), None))

            # Add graphic
            #CurrentGraphicsView = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
            CurrentGraphicsView = QtGui.QLabel(self.scrollAreaWidgetContents)
            CurrentGraphicsView.setObjectName(_fromUtf8("CurrentGraphicsView"))
            self.formLayout.setWidget(Index, QtGui.QFormLayout.LabelRole, CurrentGraphicsView)
            CurrentGraphicsView.setPixmap(QtGui.QPixmap(os.getcwd() + "/Assets/20um/"+AlgaeSample.Get_File_Name(x)))
            CurrentGraphicsView.setFixedWidth(75)
            CurrentGraphicsView.setFixedHeight(75)
            #CurrentGraphicsView.setGeometry(0,0,90,90)
            CurrentGraphicsView.setScaledContents(True)
            backGroundColorString = "44,121,176,255"
            CurrentGraphicsView.setStyleSheet("background-color: rgba("+backGroundColorString+")" )
            
            """#print "Drawing: " + algaeTable.Name_Array[x]
            pic = QtGui.QLabel(self.glWidget)
            pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/Assets/20um/"+algaeTable.Name_Array[x] + ".png"))
            pic.setGeometry(randint(-1000,1000),randint(-1000,1000),pic.pixmap().width()/8,pic.pixmap().height()/8)
            pic.setScaledContents(True)
            pic.setStyleSheet("background-color: rgba("+backGroundColorString+")" )
            algaeList.append(pic)"""


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
    
    ## Converts unicode superscript digits to regular integer digits
    
        
    #Access the table widget and extract the users answers    
    def getUserCount(self, algaeIndex,algaeSample,ansTable):
        ## A dynamic attempt to solve the superscript problem that ultimatly failed
        ## -Jeff 11/21/2013
##        def supToI(s):
##            sups={u'\u2070' : 0,
##                    u'\xb9' : 1,
##                    u'\xb2' : 2,
##                    u'\xb3' : 3,    
##                    u'\u2074' : 4,           
##                    u'\u2075' : 5,
##                    u'\u2076' : 6,
##                    u'\u2077' : 7,
##                    u'\u2078' : 8,
##                    u'\u2079' : 9}
##            return ''.join([sups[i] for i in s])
        tableItem= ansTable.findItems(algaeSample.Get_Name(algaeIndex),QtCore.Qt.MatchFixedString)
        
        if(len(tableItem) > 0):
            return supToI(ansTable.cellWidget(tableItem[0].row(),1).currentText()[1])
        else:
            return "0"
        
    def closeEvent(self):
        print("event")
        
    
    def retranslateUi(self, results, AlgaeSample):
        results.setWindowTitle(_translate("Counting Results", "Dialog", None))
        self.pushButton.setText(_translate("results", "Continue", None))
        self.label.setText(_translate("results", "Overall Score", None))
        self.label_41.setText(_translate("results", "Results", None))
