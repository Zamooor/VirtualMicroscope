# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created: Sat Nov 23 16:30:54 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!
import sys, os
from PyQt4 import QtCore, QtGui
import algaeTable
from algaeLibrary import *
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
#if no value is specified each session will have this number of trials
defaultNumTrials=5

class Ui_Preferences(object):
    
    def setupUi(self, Preferences,startFlag):
        #a copy of the dialog window in onred to access function to close the window
        self.pref=Preferences
        
        self.startUpFlag=startFlag
        #will include all the elgae to be present in the session
        self.AlgaeIncludeSet=[]
        #list of all the checkboxes each selecting one type of algae
        self.CheckBoxList=[]
        
        Preferences.setObjectName(_fromUtf8("Preferences"))
        Preferences.setFixedSize(700, 500)
        
        
        self.Button_Ok = QtGui.QPushButton(Preferences)
        self.Button_Ok.setGeometry(QtCore.QRect(460, 460, 100, 28))
        self.Button_Ok.setObjectName(_fromUtf8("Button_Ok"))
        self.Button_Ok.clicked.connect(self.clickedOK)

        self.Button_Cancel=QtGui.QPushButton(Preferences)
        self.Button_Cancel.setGeometry(QtCore.QRect(570, 460, 100, 28))
        self.Button_Cancel.setObjectName(_fromUtf8("Button_Cancel"))
        self.Button_Cancel.clicked.connect(self.clickedCancel)
        
        self.tabWidget = QtGui.QTabWidget(Preferences)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 660, 440))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        
        self.Algae = QtGui.QWidget()
        self.Algae.setObjectName(_fromUtf8("Algae"))
        
        self.Group_Program_Options = QtGui.QGroupBox(self.Algae)
        self.Group_Program_Options.setGeometry(QtCore.QRect(20, 20, 610, 370))
        self.Group_Program_Options.setObjectName(_fromUtf8("Group_Program_Options"))
        
        self.List_Algae_Select = QtGui.QWidget()
        self.List_Algae_Select.setGeometry(QtCore.QRect(20, 30, 670, 230))
        self.List_Algae_Select.setObjectName(_fromUtf8("List_Algae_Select"))


        self.AlgaeLibrary = QtGui.QScrollArea(self.Group_Program_Options)
        self.AlgaeLibrary.setEnabled(True)
        self.AlgaeLibrary.setGeometry(QtCore.QRect(35, 60, 540, 300))
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
        
        self.formLayout = QtGui.QFormLayout(self.List_Algae_Select)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        
        self.Check_All = QtGui.QCheckBox( "Include All" ,self.Group_Program_Options)
        self.Check_All.setObjectName(_fromUtf8("Check_include"))
        self.Check_All.setGeometry(QtCore.QRect(35,15, 100, 50))
        #always add the "check al button"
        self.CheckBoxList.append(self.Check_All)
        
        Index=0
        #iterate through the whole algae dictionary and add a graphic/check box for each species
        for key in AlgaeLib:
            Index += 7 
            self.CurrentGroupBox = QtGui.QGroupBox(self.List_Algae_Select)
            self.CurrentGroupBox.setTitle(_fromUtf8(key))
            self.CurrentGroupBox.setObjectName(_fromUtf8("CurrentGroupBox"))

            self.CurrentLayoutWidget = QtGui.QWidget(self.CurrentGroupBox)
            self.CurrentLayoutWidget.setGeometry(QtCore.QRect(10, 20, 600, 47))
            self.CurrentLayoutWidget.setObjectName(_fromUtf8("CurrentLayoutWidget"))

            self.CurrentGridLayout = QtGui.QGridLayout(self.CurrentLayoutWidget)
            self.CurrentGridLayout.setMargin(0)
            self.CurrentGridLayout.setObjectName(_fromUtf8("CurrentGridLayout"))        

            
            self.Check_include = QtGui.QCheckBox("Include in Samples", self.CurrentLayoutWidget)
            self.Check_include.setObjectName(_fromUtf8("Check_include"))
            self.Check_include.setGeometry(QtCore.QRect(20, 0, 130, 47))
            #self.Check_include.stateChanged.connect(self.handleItemClicked)
            self.CheckBoxList.append(self.Check_include)
    
            self.formLayout.setWidget(Index, QtGui.QFormLayout.FieldRole, self.CurrentGroupBox)


            # Add graphic
            #CurrentGraphicsView = QtGui.QGraphicsView(self.scrollAreaWidgetContents)
            self.CurrentGraphicsView = QtGui.QLabel(self.List_Algae_Select)
            self.CurrentGraphicsView.setObjectName(_fromUtf8("CurrentGraphicsView"))
            self.formLayout.setWidget(Index, QtGui.QFormLayout.LabelRole, self.CurrentGraphicsView)
            self.CurrentGraphicsView.setPixmap(QtGui.QPixmap(os.getcwd() + "/Assets/20um/"+AlgaeLib[key]+".png"))
            self.CurrentGraphicsView.setFixedWidth(75)
            self.CurrentGraphicsView.setFixedHeight(75)
            #CurrentGraphicsView.setGeometry(0,0,90,90)
            self.CurrentGraphicsView.setScaledContents(True)
            self.backGroundColorString = "44,121,176,255"
            self.CurrentGraphicsView.setStyleSheet("background-color: rgba("+self.backGroundColorString+")" )
            
        self.AlgaeLibrary.setWidget(self.List_Algae_Select)
                
        self.tabWidget.addTab(self.Algae, _fromUtf8(""))
        self.Session = QtGui.QWidget()
        self.Session.setObjectName(_fromUtf8("Session"))
        self.Group_Algae_Species = QtGui.QGroupBox(self.Session)
        self.Group_Algae_Species.setGeometry(QtCore.QRect(20, 20, 261, 71))
        self.Group_Algae_Species.setObjectName(_fromUtf8("Group_Algae_Species"))
        self.Input_Num_Trials = QtGui.QLineEdit(self.Group_Algae_Species)
        self.Input_Num_Trials.setGeometry(QtCore.QRect(130, 30, 113, 22))
        self.Input_Num_Trials.setObjectName(_fromUtf8("Input_Num_Trials"))
        self.tabWidget.addTab(self.Session, _fromUtf8(""))

        self.retranslateUi(Preferences)
        
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Preferences)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(_translate("Preferences", "Preferences", None))
        self.Group_Program_Options.setTitle(_translate("Preferences", "Algae Species Selection", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Algae), _translate("Preferences", "Algae", None))
        self.Group_Algae_Species.setTitle(_translate("Preferences", "Number Of Trials", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Session), _translate("Preferences", "Session", None))
        self.Button_Ok.setText(_translate("Preferences", "OK", None))
        self.Button_Cancel.setText(_translate("Preferences", "Cancel", None))

    #when ok is clicked iterate through all check boxes and only add the checked
    #algae to the samples
    def clickedOK(self):
        x=1
        for key in AlgaeLib:
            if self.CheckBoxList[0].isChecked():
                self.AlgaeIncludeSet.append(key)
            elif self.CheckBoxList[x].isChecked():
                self.AlgaeIncludeSet.append(key)
            x+=1
            
        #if no boxes were checked add all species    
        if not self.AlgaeIncludeSet:
            for key in AlgaeLib:
                self.AlgaeIncludeSet.append(key)
                
        #append the number of trials requested by the user
        #if no value specified use default
        try:
           val = int(self.Input_Num_Trials.text())
           self.AlgaeIncludeSet.append(self.Input_Num_Trials.text())
        except ValueError:
           self.AlgaeIncludeSet.append(defaultNumTrials)
           
        self.pref.done(int(True))

    #when cancel is cliked dont change the session parameters
    #unles this is the first session then use all algae and default number of trials
    def clickedCancel(self):
        if self.startUpFlag==False:
            self.pref.done(int(False))
        else:
            for key in AlgaeLib:
                self.AlgaeIncludeSet.append(key)
                
            self.AlgaeIncludeSet.append(defaultNumTrials)
            self.pref.done(int(True))
    #when called returns the session parameters including algae
    #species and number of trials
    def retVal(self):
        return self.AlgaeIncludeSet


'''if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_Preferences()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())'''
