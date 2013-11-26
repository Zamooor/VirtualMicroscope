"""==========================================================================
Name: algaeTable.py

    This file will act as the algae data generator and storage for the main
program. Each type of algae will have a unique ID (numerical), Name (string).
=========================================================================="""
# Includes
import sys
import math

from random import randint

def supToI(u):
    if u == u'\u2074':
        return 4
    elif u == u'\u2075':
        return 5
    elif u == u'\u2076':
        return 6
    elif u == u'\u2077':
        return 7
    elif u == u'\u2078':
        return 8

class AlgaeTable:
    
    def __init__(self):
        # Data
        #This is now a dictionary within a dictionary
        #this can be used as a 2d array run test.py for a sample :)
        
        self.AlgaeLib={
            "Lepo Ovalis":{"File":"Attempt001"},
            "Eucapsis":{"File":"eucapsis_jul6_11_400N_JUD"},
            "Aphaniz Akinetes":{"File":"aphaniz_akinetes_sep16_10_200N_TBIRD"}
            }
        self.Max_Trials = 30
        self.Max_Types = 30
        self.Default_Num_Trials=5
        self.Num_Trials=5
        self.Total_Trials=self.Num_Trials
        self.Name_Array = []

        self.Total_Algae_Types = 0
        self.Default_Min_Count = 20
        self.Default_Max_Count = 60

        self.Total_Count_Array = []
        self.Min_Count_Array = []
        self.Max_Count_Array = []
        self.Total_Mass_Array = []

        self.User_Guess_Record = [[0 for x in xrange(self.Max_Types)] for x in xrange(self.Max_Trials)]
        self.Algae_Count_Record = [[0 for x in xrange(self.Max_Types)] for x in xrange(self.Max_Trials)]

    # Exported Functions
    def Get_Name(self,ID):
        return self.Name_Array[ID]

    def Get_File_Name(self,ID):
        return self.AlgaeLib[self.Name_Array[ID]]["File"] + ".png"

    def Get_Count(self,ID):
        return self.Total_Count_Array[ID]

    def Get_Count_At_Trial(self,ID, Trial):
        return self.Algae_Count_Record[ID][Trial]

    def Get_Guess_At_Trial(self,ID, Trial):
        return self.User_Guess_Record[ID][self.Total_Trials - Trial]

    def Get_Difference_At_Trial(self,ID, Trial):
        return self.Get_Guess_At_Trial(ID,Trial) - self.Get_Count_At_Trial(ID,Trial)

    # Geometric mean
    def Get_G_Mean(self,ID):
        Product = 1.00
        for x in xrange(self.Total_Trials):
            Product *= abs(self.Get_Difference_At_Trial(ID, x))
        return Product**(1.00/self.Total_Trials)

    def Get_Biomass(self, ID):
        return self.Total_Mass_Array[ID]

    def Get_ID(self, Name):
        for x in xrange(self.Total_Algae_Types):
            if Name == self.Name_Array[x]: return x
            
    def Get_Num_Trials(self):
        return self.Num_Trials    

    def Set_Num_Trials(self, num):
        self.Num_Trials = int(num)
        self.Total_trials = int(num)


    def Set_Count_Range(self, ID, Min, Max):
        self.Min_Count_Array[ID] = Min
        self.Max_Count_Array[ID] = Max

    def Set_Min_Count(self, ID, Min):
        self.Min_Count_Array[ID] = Min

    def Set_Max_Count(self, ID, Max):
        self.Max_Count_Array[ID] = Max

    #def Set_Num_Trials(self, num):
    #    self.Total_trials = int(num)
    #    self.Num_Trials = int(num)\
                          
    def clearArrays(self):
        self.Name_Array[:]=[]
        self.Total_Count_Array[:]=[]
        self.Min_Count_Array[:]=[]
        self.Max_Count_Array[:]=[]
        self.Algae_Count_Record = [[0 for x in xrange(self.Max_Types)] for x in xrange(self.Max_Trials)] 
        self.User_Guess_Record = [[0 for x in xrange(self.Max_Types)] for x in xrange(self.Max_Trials)]
        
    def PrepareArrays(self):
        #clear all the arrays before every session
        self.Total_Algae_Types = len(self.Name_Array)
        self.Total_Count_Array = [0 for x in xrange(self.Total_Algae_Types)]
        self.Total_Mass_Array = [0.00 for x in xrange(self.Total_Algae_Types)]
        self.Algae_Count_Record = [[0 for x in xrange(self.Max_Types)] for x in xrange(self.Max_Trials)]
        self.User_Guess_Record = [[0 for x in xrange(self.Max_Types)] for x in xrange(self.Max_Trials)]

    def Generate_Sample(self):
        for x in xrange(self.Total_Algae_Types):
            self.Total_Count_Array[x] = randint(self.Min_Count_Array[x], self.Max_Count_Array[x])
            self.Algae_Count_Record[x][self.Total_Trials - self.Num_Trials] = self.Total_Count_Array[x]
        
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
