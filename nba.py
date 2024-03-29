# -*- coding: utf-8 -*-
"""NBA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18ledVXzXF8_uRdi52NnNJmpai2RN0_BT
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
# Imports from the scikit-learn package
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression # for linear regression
from sklearn import metrics #for accuracy of values
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pickle 

warnings.filterwarnings('ignore')
# %matplotlib inline

df = pd.read_excel('NBA.xlsx')
#df = df.iloc[:,:5].drop(columns=['Week'])

df['Day'] = df['Day'].astype(str)

# One-hot encode the data using pandas get_dummies
features = pd.get_dummies(df)

features

X = features.drop(columns=['W_L']).values
y = features['W_L'].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 50)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
result = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(result)
result1 = classification_report(y_test, y_pred)
print("Classification Report:",)
print (result1)
result2 = accuracy_score(y_test,y_pred)
print("Accuracy:",result2)

X_test

#                                           (Week, Value,   Player_E    Player_M    Player_N    Day_1   Day_2   Day_3   Day_4   Day_5   Day_6   Day_7)
 
#print('Player M = ' + str(classifier.predict([[     ,4000,    0,           1,        0,      0,     0,    0,   1,    0,   0,    0]])))
#print('Player N = ' + str(classifier.predict([[     ,2000,    0,           0,        1,      0,     0,    0,   1,    0,   0,    0]])))
#print('Player E = ' + str(classifier.predict([[     ,5000,    1,           0,        0,      0,     0,    0,   1,    0,   0,    0]])))

def bet_result(w,v,p,d):
  Day_1 = 0
  Day_2 = 0
  Day_3 = 0
  Day_4 = 0
  Day_5 = 0
  Day_6 = 0
  Day_7 = 0
  Player_M = 0
  Player_N = 0
  Player_E =0
  Value = v
  if d == 1:
    Day_1 = 1
  elif d == 2:
    Day_2 = 1
  elif d == 3:
    Day_3 = 1
  elif d == 4:
    Day_4 = 1
  elif d == 5:
    Day_5 = 1
  elif d == 6:
    Day_6 = 1
  elif d == 7:
    Day_7 = 1
  else:
    0
    
  
  if p == 'M':
    Player_M = 1
  elif p == 'N':
    Player_N = 1
  elif p == 'E':
    Player_E = 1
  else:
    0
  result = classifier.predict([[w, Value,   Player_E,   Player_M,   Player_N,   Day_1,  Day_2,  Day_3,  Day_4,  Day_5,  Day_6,  Day_7]])
  #print([[Value,   Player_E,   Player_M,   Player_N,   Day_1,  Day_2,  Day_3,  Day_4,  Day_5,  Day_6,  Day_7]])
  print('Player ' + p + ' : ' + str(result))

pickle.dump(classifier,open('model.pkl','wb'))

# bet_result(Week,Value,Player,Day)
#bet_result(28,3000,'M',1)
#bet_result(28,500,'N',1)
#bet_result(28,8000,'E',1)