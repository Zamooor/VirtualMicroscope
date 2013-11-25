"""==========================================================================
Name: algaeTable.py

    This file will act as the algae data generator and storage for the main
program. Each type of algae will have a unique ID (numerical), Name (string).
=========================================================================="""
# Includes
import sys
import math
import numpy as np
from random import randint

class AlgaeTable:

    def __init__(self):
        # Trials Data
        self.Max_Trials = 30 # Total trials cannot surpass this number
        self.Total_Trials = 15 # How many trials the program will perform
        self.Current_Trial = 0; # What trial the program is currently on
        
        # Data
        self.Name_Array = [
            "Lepo Ovalis",
            "Eucapsis",
            "Aphaniz Akinetes"]
        self.File_Name_Array = [
            "Attempt001",
            "eucapsis_jul6_11_400N_JUD",
            "aphaniz_akinetes_sep16_10_200N_TBIRD"]
        self.Total_Algae_Types = len(self.Name_Array)
        self.Default_Min_Count = 20
        self.Default_Max_Count = 60

        self.Total_Count_Array = np.zeros((self.Total_Algae_Types, self.Max_Trials), dtype='int')
        self.Min_Count_Array = [self.Default_Min_Count for x in xrange(self.Total_Algae_Types)]
        self.Max_Count_Array = [self.Default_Max_Count for x in xrange(self.Total_Algae_Types)]

    # Exported Functions
    def Get_Name(self,ID):
        return self.Name_Array[ID]

    def Get_File_Name(self,ID):
        return self.File_Name_Array[ID] + ".png"

    def Get_Count(self,ID, Trial):
        return self.Total_Count_Array.item(ID, Trial)

    def Get_Current_Count(self,ID):
        return self.Total_Count_Array.item(ID, self.Current_Trial)

    def Get_ID(self, Name):
        for x in xrange(self.Total_Algae_Types):
            if Name == self.Name_Array[x]: return x

    def Set_Count_Range(self, ID, Min, Max):
        self.Min_Count_Array[ID] = Min
        self.Max_Count_Array[ID] = Max

    def Set_Min_Count(self, ID, Min):
        self.Min_Count_Array[ID] = Min

    def Set_Max_Count(self, ID, Max):
        self.Max_Count_Array[ID] = Max

    def Generate_Sample(self):
        self.Current_Trial = self.Current_Trial + 1
        for x in xrange(self.Total_Algae_Types):
            self.Total_Count_Array[x] = randint(self.Min_Count_Array[x], self.Max_Count_Array[x])
