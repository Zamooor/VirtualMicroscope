"""==========================================================================
Name: algaeTable.py

    This file will act as the algae data generator and storage for the main
program. Each type of algae will have a unique ID (numerical), Name (string).
=========================================================================="""
# Includes
import sys
import math
from algaeLibrary import *
from random import randint

class AlgaeTable:

    def __init__(self):
        # Data
        self.Num_Trials=5
        self.Name_Array = []

        self.Total_Algae_Types = 0
        self.Default_Min_Count = 20
        self.Default_Max_Count = 60

        self.Total_Count_Array = []
        self.Min_Count_Array = []
        self.Max_Count_Array = []
        self.Total_Mass_Array = []

    # Exported Functions
    def Get_Name(self,ID):
        return self.Name_Array[ID]

    def Get_File_Name(self,ID):
        return AlgaeLib[self.Name_Array[ID]] + ".png"

    def Get_Count(self,ID):
        return self.Total_Count_Array[ID]

    def Get_Biomass(self, ID):
        return self.Total_Mass_Array[ID]

    def Get_ID(self, Name):
        for x in xrange(self.Total_Algae_Types):
            if Name == self.Name_Array[x]: return x
            
    def Get_Num_Trials(self):
        return self.Num_Trials    

    def Set_Count_Range(self, ID, Min, Max):
        self.Min_Count_Array[ID] = Min
        self.Max_Count_Array[ID] = Max

    def Set_Min_Count(self, ID, Min):
        self.Min_Count_Array[ID] = Min

    def Set_Max_Count(self, ID, Max):
        self.Max_Count_Array[ID] = Max

    def Set_Num_Trials(self, num):
        self.Num_Trials = int(num)

    def setNames(self,session):
        #clearr all the arrays before every session
        self.Name_Array[:]=[]
        self.Total_Count_Array[:]=[]
        self.Min_Count_Array[:]=[]
        self.Max_Count_Array[:]=[]
        
        self.Name_Array=list(session)
        self.Total_Algae_Types = len(self.Name_Array)
        self.Total_Count_Array = [0 for x in xrange(self.Total_Algae_Types)]
        self.Min_Count_Array = [self.Default_Min_Count for x in xrange(self.Total_Algae_Types)]
        self.Max_Count_Array = [self.Default_Max_Count for x in xrange(self.Total_Algae_Types)]
        self.Total_Mass_Array = [0.00 for x in xrange(self.Total_Algae_Types)]

    def Generate_Sample(self):
        for x in xrange(self.Total_Algae_Types):
            self.Total_Count_Array[x] = randint(self.Min_Count_Array[x], self.Max_Count_Array[x])
        
    def Decrement_Trials(self):
        self.Num_Trials-=1
          

# Default program
"""if __name__ == '__main__':
    print "Printing tables:"
    for x in xrange(Total_Algae_Types):
        print '\n[{}] {}'.format(x, self.Name_Array[x])
        print 'Count: {}'.format(self.Total_Count_Array[x])
        print 'Biomass: {}'.format(self.Total_Mass_Array[x])

    print "Generating sample data:"
    Generate_Sample()
    for x in xrange(Total_Algae_Types):
        print '\n[{}] {}'.format(x, self.Name_Array[x])
        print 'Count: {}'.format(self.Total_Count_Array[x])
        print 'Biomass: {}'.format(self.Total_Mass_Array[x])"""
