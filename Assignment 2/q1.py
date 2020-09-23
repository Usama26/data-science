# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:07:32 2020

@author: Usama
"""

import pandas as pd

first_health_att = pd.read_csv('./Data/First_Health_Camp_Attended.csv');
second_health_att = pd.read_csv('./Data/Second_Health_Camp_Attended.csv');
third_health_att = pd.read_csv('./Data/Third_Health_Camp_Attended.csv');



first_health_att.isnull().sum()
first_health_att.Health_Score

second_health_att['Health_Camp_ID'].describe()
quartiles = list(second_health_att['Health_Camp_ID'].quantile([0.25,0.5,0.75]))





len(second_health_att['Health_Camp_ID'])/2

print(3910/2)
second_health_att['Health_Camp_ID'][1955]
second_health_att['Health_Camp_ID'][1954]



q1 = quartiles[0]
q3 = quartiles[2]

iqr = q3 - q1

minRange = q1 - (1.5 * iqr)
maxRange = q3 + (1.5 * iqr)

for each in list(second_health_att.values):
    if(each[1] < minRange or each[1] > maxRange):
        print(each[1])