#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:21:58 2020

@author: dibya
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.metrics

import keras
from keras.models import Sequential
from keras.layers import Dense



from sklearn.base import TransformerMixin

class DataFrameImputer(TransformerMixin):

    def __init__(self):
        """Impute missing values.

        Columns of dtype object are imputed with the most frequent value 
        in column.

        Columns of other types are imputed with mean of column.

        """
    def fit(self, X, y=None):

        self.fill = pd.Series([X[c].value_counts().index[0]
            if X[c].dtype == np.dtype('O') else X[c].mean() for c in X],
            index=X.columns)

        return self

    def transform(self, X, y=None):
        return X.fillna(self.fill)

#dataset = pd.read_csv('covid_combined.csv', parse_dates=['Date'], dayfirst=True)    
#dataset = pd.read_csv('output.csv')
dataset = pd.read_csv('covid_combined.csv') #Here we take the dataset


#dataset=dataset.iloc[0:58,:]


#dataset=dataset.iloc[:,0:4]
X = dataset.iloc[:,0:4]#Here we take the input variables
X['DateP']=X['DateP']-43852
X['Long']=X['Long'].astype(str)
X['Lat']=X['Lat'].astype(str)
X = X.drop(['Date'], axis=1)#Here drop the Date variable as they have already converted the Date into a numerical value
X['Location'] = X['Lat'].str.cat(X['Long'], sep =" ") 


X=X.drop(['Lat'],axis=1)
X=X.drop(['Long'],axis=1)




#X.iloc[:,2]=X.iloc[:,2].dt.strftime('%m/%d/%Y')

#Here we define the output variables
y_confirmed = dataset.iloc[:, 4]
y_recovered = dataset.iloc[:,5]
y_deaths = dataset.iloc[:,6]


from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X=LabelEncoder()
X.iloc[:,1]=labelencoder_X.fit_transform(X.iloc[:,1])


from sklearn.compose import ColumnTransformer

ct = ColumnTransformer([("Country", OneHotEncoder(), [1])], remainder = 'passthrough')
X = ct.fit_transform(X).toarray()





#X=X.reshape(-1,1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y_confirmed, test_size = 0.2, random_state = 0)

'''
from sklearn.ensemble import RandomForestRegressor
regressor_confirmed=RandomForestRegressor(n_estimators=100,random_state=0)
regressor_confirmed.fit(X,y_confirmed)
y_pred_confirmed=regressor_confirmed.predict(X)

regressor_recovered=RandomForestRegressor(n_estimators=100,random_state=0)
regressor_recovered.fit(X,y_recovered)
y_pred_recovered=regressor_recovered.predict(X)

regressor_deaths=RandomForestRegressor(n_estimators=100,random_state=0)
regressor_deaths.fit(X,y_deaths)
y_pred_deaths=regressor_deaths.predict(X)

result=pd.DataFrame()
result['confirmed cases']=y_confirmed
result['predicted C ']=y_pred_confirmed
result['recoved cases']=y_recovered
result['predicted R ']=y_pred_recovered
result['death cases']=y_deaths
result['predicted D']=y_pred_deaths

result.to_csv('results.csv')
'''
'''
from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=200,random_state=0)
regressor.fit(X_train,y_train)
'''

'''
from sklearn.linear_model import LinearRegression



from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=2)
X_poly=poly_reg.fit_transform(X_train)
poly_reg.fit(X_poly,y_train)

lin_reg=LinearRegression()
lin_reg.fit(X_poly,y_train)
'''

'''
from sklearn.svm import SVR
regressor=SVR(kernel='rbf')
regressor.fit(X_train,y_train)
'''

'''
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)
'''


  # Initialising the ANN acc-73.5%
classifier = Sequential()

# Adding the input layer and the first hidden layer

classifier.add(Dense(32, kernel_initializer='normal',input_dim = 465, activation='relu'))

# Adding the second hidden layer
classifier.add(Dense(output_dim =512 , init = 'uniform', activation = 'relu'))


# Adding the third hidden layer
classifier.add(Dense(output_dim = 512, init = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'linear'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'mean_absolute_error', metrics = ['mean_absolute_error'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 5, nb_epoch = 170)
#classifier.fit(X_train, y_train)


classifier.save("Confirmed values.h5")















test_data=pd.read_csv('test_cases.csv')
test_data=test_data.drop(['Date'],axis=1)
test_data=test_data.drop(['Confirmed'],axis=1)
#test_data=test_data.iloc[0:3,:]
test_data['DateP']=test_data['DateP']-43852

#y_pred=lin_reg.predict(poly_reg.fit_transform(test_data))


#y_pred=regressor.predict(X_test)


y_pred=classifier.predict(X_test)
