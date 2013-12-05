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

        self.Default_Min_Count = 20
        self.Default_Max_Count = 60
            
    def Get_Num_Trials(self):
        return self.Num_Trials    

    def Set_Num_Trials(self, num):
        self.Num_Trials = int(num)
        self.Total_trials = int(num)

    def Generate_Sample(self):
        for key in self.AlgaeLib:
            if (self.Is_Active(key)):
                self.Set_Actual_Count(key, self.Get_Current_Round(), randint(self.Get_Min(key), self.Get_Max(key)))

    def Decrement_Trials(self):
        self.Num_Trials-=1

    # Dictionary / record functions
    def Set_Actual_Count(self, Algae_Name, Trial, Count):
        self.AlgaeLib[Algae_Name]["Actual"+str(Trial)] = Count

    def Get_Actual_Count(self, Algae_Name, Trial):
        return self.AlgaeLib[Algae_Name]["Actual"+str(Trial)]

    def Set_User_Count(self, Algae_Name, Trial, Count):
        self.AlgaeLib[Algae_Name]["User"+str(Trial)] = Count

    def Get_User_Count(self, Algae_Name, Trial):
        return self.AlgaeLib[Algae_Name]["User"+str(Trial)]

    def Set_Active(self, Algae_Name, Active):
        self.AlgaeLib[Algae_Name]["Active"] = Active

    def Is_Active(self, Algae_Name):
        return self.AlgaeLib[Algae_Name]["Active"]

    def Get_Current_Round(self):
        return self.Total_Trials - self.Num_Trials

    def Set_Range(self, Algae_Name, Min, Max):
        self.AlgaeLib[Algae_Name]["Min"] = Min
        self.AlgaeLib[Algae_Name]["Max"] = Max

    def Get_Min(self, Algae_Name):
        return self.AlgaeLib[Algae_Name]["Min"]

    def Get_Max(self, Algae_Name):
        return self.AlgaeLib[Algae_Name]["Max"]

    def Get_Difference(self, Algae_Name, Trial):
        return self.Get_User_Count(Algae_Name, Trial) - self.Get_Actual_Count(Algae_Name, Trial)

    def Get_Geometric_Mean(self,Algae_Name):
        Product = 1.00
        for x in xrange(self.Total_Trials):
            Product *= abs(self.Get_Difference(Algae_Name, x))
        return Product**(1.00/self.Total_Trials)

    def Get_File_Name(self,Algae_Name):
        return self.AlgaeLib[Algae_Name]["File"] + ".png"
    
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
