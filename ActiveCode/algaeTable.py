"""==========================================================================
Name: algaeTable.py

    This file will act as the algae data generator and storage for the main
program. Each type of algae will have a unique ID (numerical), Name (string).
=========================================================================="""
# Includes
import sys
import math
from random import randint

# Data
Name_Array = [
    "Type 1",
    "Type 2",
    "type 3"]
Total_Algae_Types = len(Name_Array)
Default_Min_Count = 0
Default_Max_Count = 10

#Name_Array = ["NULL" for x in xrange(Total_Algae_Types)]
Total_Count_Array = [0 for x in xrange(Total_Algae_Types)]
Min_Count_Array = [Default_Min_Count for x in xrange(Total_Algae_Types)]
Max_Count_Array = [Default_Max_Count for x in xrange(Total_Algae_Types)]
Total_Mass_Array = [0.00 for x in xrange(Total_Algae_Types)]

# Exported Functions
def Get_Name(ID):
    return Name_Array[ID]

def Get_Count(ID):
    return Total_Count_Array[ID]

def Get_Biomass(ID):
    return Total_Mass_Array[ID]

def Get_ID(Name):
    for x in xrange(Total_Algae_Types):
        if Name == Name_Array[x]: return x

def Set_Count_Range(ID, Min, Max):
    Min_Count_Array[ID] = Min
    Max_Count_Array[ID] = Max

def Set_Min_Count(ID, Min):
    Min_Count_Array[ID] = Min

def Set_Max_Count(ID, Max):
    Max_Count_Array[ID] = Max

def Generate_Sample():
    for x in xrange(Total_Algae_Types):
        Total_Count_Array[x] = randint(Min_Count_Array[x], Max_Count_Array[x])

# Sample Data
Min_Count_Array[1] = 3
Max_Count_Array[0] = 20


# Default program
if __name__ == '__main__':
    print "Printing tables:"
    for x in xrange(Total_Algae_Types):
        print '\n[{}] {}'.format(x, Name_Array[x])
        print 'Count: {}'.format(Total_Count_Array[x])
        print 'Biomass: {}'.format(Total_Mass_Array[x])

    print "Generating sample data:"
    Generate_Sample()
    for x in xrange(Total_Algae_Types):
        print '\n[{}] {}'.format(x, Name_Array[x])
        print 'Count: {}'.format(Total_Count_Array[x])
        print 'Biomass: {}'.format(Total_Mass_Array[x])
