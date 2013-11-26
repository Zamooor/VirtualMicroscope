#helpful site
#http://www.pythonforbeginners.com/dictionary/

import sys, os
from PyQt4 import QtCore, QtGui
import algaeTable
from Globals import *

if __name__ == "__main__":
    print "printing all keys algae in dictinary"
    for key in algaeTable.AlgaeLib:
        print key

    print"\n"

    
    print "adding 9 trials for Lepo Ovalis to the dictionary"
    for x in range(1,10):
        algaeTable.AlgaeLib["Lepo Ovalis"]["trial"+str(x)]=x+10

    print"\n"

    
    print"printing all the trial information for the algae Lepo Ovalis"
    for x in range(1,10):
        print "trial "+str(x)
        print algaeTable.AlgaeLib["Lepo Ovalis"]["trial"+str(x)]
    print"\n"
    

    print "adding 9 trials for every algae in the dictionary"
    for key in algaeTable.AlgaeLib:
        for x in range(1,10):
            algaeTable.AlgaeLib[key]["trial"+str(x)]=x+10
    print"\n"
            
    print "printing the p trial session info for all algae"
    for x in range(1,10):
        print "trial"+str(x)+":"
        for key in algaeTable.AlgaeLib:
            print key+": "+str(algaeTable.AlgaeLib[key]["trial"+str(x)])
        print ""
    print"\n"
