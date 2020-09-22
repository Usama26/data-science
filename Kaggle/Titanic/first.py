# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:44:27 2020

@author: Usama
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier

from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split


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
# list(data['Embarked'].values).index(np.nan,62)

data.drop([61,829],inplace=True)



f,ax = plt.subplots(figsize=(6,5))

sns.set_color_codes("pastel")

sns.barplot(x="Survived",y="Sex",data=data,label="Total",color="b")


SurvivedMale = len(data.query('Sex == "male" and Survived == 1'))
SurvivedFemale = len(data.query('Sex == "female" and Survived == 1'))
Total = len(data)

print((SurvivedMale/Total)*100)
print((SurvivedFemale/Total)*100)

finalData = data.drop(['PassengerId','Name','Ticket','Fare'],axis=1)

finalData.replace('male',1,inplace=True)
finalData.replace('female',2,inplace=True)


finalData.Embarked.unique()
finalData.Embarked.replace('S',1,inplace=True)
finalData.Embarked.replace('C',2,inplace=True)
finalData.Embarked.replace('Q',3,inplace=True)



X_train,X_test,Y_train,Y_test = train_test_split(finalData[finalData.columns[:-1]] ,finalData[finalData.columns[-1]],test_size=0.3)


sel = SelectFromModel(RandomForestClassifier(n_estimators = 100))
sel.fit(X_train, Y_train)

sel.get_support()


selected_feat= X_train.columns[(sel.get_support())]
len(selected_feat)
print(selected_feat)


X_train[selected_feat]

from sklearn.svm import SVC
svm = SVC(kernel="linear",C=0.025,random_state=101)
svm.fit(X_train[selected_feat],Y_train)
Y_pred = svm.predict(X_test[selected_feat])



# comp_pred = X_test
# comp_pred.insert(loc=6,column="PRED",value=Y_pred)

from sklearn.metrics import accuracy_score

accuracy_score(Y_test, Y_pred)
