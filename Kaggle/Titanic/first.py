# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:44:27 2020

@author: Usama
"""

import pandas as pd
import numpy as np

data = pd.read_csv('train.csv')

cols = list(data.columns)

newCols  = cols[:1]

newCols.extend(cols[2:])
newCols.extend(['Survived'])

data = data[newCols]

data.isnull().sum()

len(data)

print((891*20)/100)

data.replace('',np.nan,inplace=True)


from sklearn.impute import SimpleImputer

imp = SimpleImputer(missing_values=np.nan , strategy="mean")

temp = imp.fit_transform(pd.DataFrame(data['Age']))

data['NewAge'] = temp.apply(np.ceil)


data.insert(loc=4,column='RoundedAge',value=data['NewAge'])

data.drop('NewAge',axis=1,inplace=True)

data.drop('Age',axis=1,inplace=True)


np.floor(temp)
list(temp.columns.values)

# 829 , 61

list(data['Embarked'].values).index(np.nan,62)