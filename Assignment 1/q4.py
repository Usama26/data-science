# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 00:58:09 2020

@author: Usama
"""

import pandas as pd 
  
def f(x):
    if x < 50000:
        return x
    
# Creating the dataframe  
df = pd.read_csv("nba.csv")

df.filter(["Name", "Team", "Salary"]) 

print(df['Salary'].apply(f))
