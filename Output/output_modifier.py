#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 02:37:42 2020

@author: dibya
"""

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
result=pd.read_csv('output.csv')

lat=dataset.iloc[:,1]
long=dataset.iloc[:,2]
result['Long']=long
result['Lat']=lat
result=result.drop(['Unnamed: 0'],axis=1)
result=result.drop(['Location'],axis=1)
result['confirmed cases']=result['confirmed cases'].round()
result['recoved cases']=result['recoved cases'].round()
result['death cases']=result['death cases'].round()

result.to_csv('output_modified.csv')