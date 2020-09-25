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
first_health_att.dropna("Health_Score",axis=1)

second_health_att['Health_Camp_ID'].describe()
quartiles = list(second_health_att['Health_Camp_ID'].quantile([0.25,0.5,0.75]))





len(second_health_att['Health_Camp_ID'])/2

print(3910/2)
second_health_att['Health_Camp_ID'][1955]
second_health_att['Health_Camp_ID'][1954]



q1 = quartiles[0]
q3 = quartiles[2]

iqr = q3 - q1

minRange = q1 - (3.0* iqr)
maxRange = q3 + (3.0* iqr)


#Converting Outliers as the question asked
for i in range(0,len(second_health_att)):
    if(second_health_att['Health_Camp_ID'][i] < minRange or second_health_att['Health_Camp_ID'][i] > maxRange):
        print(second_health_att['Health_Camp_ID'][i] , "X" ,i)
        if(second_health_att['Health_Camp_ID'][i+1] - second_health_att['Health_Camp_ID'][i-1] <= 2):
            second_health_att['Health_Camp_ID'][i] = second_health_att['Health_Camp_ID'][i+1]