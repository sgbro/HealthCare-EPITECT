#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:44:15 2020

@author: dibya
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.metrics

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model

dataset = pd.read_csv('test_nn (2).csv') 

dataset['dateP']=dataset['dateP']-43852
dataset['Long']=dataset['Long'].astype(str)
dataset['Lat']=dataset['Lat'].astype(str)

dataset['Location'] = dataset['Lat'].str.cat(dataset['Long'], sep =" ") 


dataset=dataset.drop(['Lat'],axis=1)
dataset=dataset.drop(['Long'],axis=1)
dataset=dataset.drop(['Unnamed: 0'],axis=1)


from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X=LabelEncoder()
dataset.iloc[:,1]=labelencoder_X.fit_transform(dataset.iloc[:,1])


from sklearn.compose import ColumnTransformer

ct = ColumnTransformer([("Country", OneHotEncoder(), [1])], remainder = 'passthrough')
dataset= ct.fit_transform(dataset).toarray()


model=load_model('Confirmed values.h5')
model.summary()

y_confirmed=model.predict(dataset)

model=load_model('Recovered values.h5')

y_recovered=model.predict(dataset)

model=load_model('Death values.h5')

y_death=model.predict(dataset)

dataset['confirmed cases']=y_confirmed
dataset['recoved cases']=y_recovered
dataset['death cases']=y_death

dataset.to_csv('output.csv')