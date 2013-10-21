"""==========================================================================
Name: algaeTable.py

    This file will act as the algae data generator and storage for the main
program. Each type of algae will have a unique ID (numerical), Name (string).
=========================================================================="""
# Includes
import sys
import math

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

# Data
Total_Algae_Types = 2

Name_Array = ["" for x in xrange(Total_Algae_Types)]
Name_Array = [
    "Type 1",
    "Type 2"]

Total_Count_Array = [0 for x in xrange(Total_Algae_Types)]
Total_Mass_Array = [0.00 for x in xrange(Total_Algae_Types)]

# Default program
if __name__ == '__main__':
    print "Printing tables:"
    for x in xrange(Total_Algae_Types):
        print '\n[{}] {}'.format(x, Name_Array[x])
        print 'Count: {}'.format(Total_Count_Array[x])
        print 'Biomass: {}'.format(Total_Mass_Array[x])
