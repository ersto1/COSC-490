# -*- coding: utf-8 -*-
"""buildings_dataset

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NC_iz811YoFvVhfZ1dzn4nKPl6qeg0lv
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib
data = ("Buildings_Footprint.csv")

df = pd.read_csv(data)
type(df)

to_drop = ['OBJECTID_1', 'SUBTYPE','SYMBOL','Override', 'RuleID_1', 'Override_1','URL']
df.drop(to_drop, inplace=True, axis=1)

df.head()

"""# New Section"""

median_column = df["BUILDING_I"]
type(median_column)
median_column.plot(kind="hist")
plt.show()

df.plot(x="OBJECTID", y="BUILDING_I")
plt.show()

df.plot(x="OBJECTID", y="AREA_")
plt.show()

median_column = df["BUILDING_I"]
type(median_column)
median_column.plot(kind="pie")
plt.show()

median_column = df["BUILDING_I"]
type(median_column)
median_column.plot(kind="line")
plt.show()

import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))

import numpy
import pandas
myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = ['a', 'b']
colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)

import pandas
url = "Buildings_Footprint.csv"
names = ['OBJECTID_1', 'OBJECTID', 'TAG', 'SUBTYPE', 'SRCDATE', 'SYMBOL', 'Shape_Leng', 'BUILDING_I', 'AREA_', 'PERIMETER', 'RuleID', 'GlobalID', 'URL', 'Shape__Area', 'Shape__Length']
data = pandas.read_csv(url, names=names)
print(data.shape)
description = data.describe()
print(description)

from sklearn.preprocessing import StandardScaler
import pandas
import numpy
url = "https://data.baltimorecity.gov/datasets/baltimore::buildings-footprint.csv"
names = ['OBJECTID_1', 'OBJECTID', 'TAG', 'SUBTYPE', 'SRCDATE', 'SYMBOL', 'Shape_Leng', 'BUILDING_I', 'AREA_', 'PERIMETER', 'RuleID', 'GlobalID', 'URL', 'Shape__Area', 'Shape__Length']
df = pandas.read_csv(url, names=names)
array = df.values
# separate array into input and output components
X = array[:,0:8]
Y = array[:,1]
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
# summarize transformed data
numpy.set_printoptions(precision=3)
print(rescaledX[0:5,:])
to_drop = ['OBJECTID_1','TAG', 'SUBTYPE', 'SRCDATE', 'SYMBOL', 'Shape_Leng', 'BUILDING_I', 'AREA_', 'PERIMETER', 'RuleID', 'GlobalID', 'URL', 'Shape__Area', 'Shape__Length']
df.drop(to_drop, inplace=True, axis=1)
df.head()

# Evaluate using Cross Validation
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
import pandas as pd
url = "https://data.baltimorecity.gov/datasets/baltimore::buildings-footprint.csv"
names = ['OBJECTID_1', 'OBJECTID', 'TAG','BUILDING_I', 'AREA_', 'PERIMETER', 'RuleID', 'GlobalID', 'URL', 'Shape__Area', 'Shape__Length']
df = read_csv(url, names=names)
array = df.values
X = array[:,0:8]
Y = array[:,8]
kfold = KFold(n_splits=10, random_state=7, shuffle=True)
model = LogisticRegression(solver='liblinear')
results = cross_val_score(model, X, Y, cv=kfold)
print("Accuracy: %.3f%% (%.3f%%)" % (results.mean()*100.0, results.std()*100.0))
to_drop = ['OBJECTID_1','TAG','SUBTYPE','SRCDATE','SYMBOL','Shape__Length','AREA_', 'PERIMETER', 'RuleID','Override','RuleID_1','Override_1','GlobalID', 'URL', 'Shape__Area','Shape__Length']
df.drop(to_drop, inplace=True, axis=1)
df.head()

# Cross Validation Classification LogLoss
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
import pandas as pd
url = "Buildings_Footprint.csv"
to_drop = ['OBJECTID_1', 'TAG','SUBTYPE','SRCDATE','SYMBOL','Shape__Length','Shape__Area','Override','RuleID_1','Override_1','GlobalID','URL','Shape_Leng']
df = pd.read_csv("Buildings_Footprint.csv")
df.drop(to_drop, inplace=True, axis=1)
df.head()
# dropna(). Look it up
# Now we have 5 features "OBJECTID, BUILDING_I, AREA, PERIMETER, RULEID"
# Next step, take that column and move it to the end - BUILDING_I" # This is our target we want to predict"
array = df.values
X = array[:,0:4]
Y = array[:,4]
kfold = KFold(n_splits=10, random_state=None)
model = LogisticRegression(solver='liblinear')
scoring = 'neg_log_loss'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print("Logloss: %.3f (%.3f)") % (results.mean(), results.std())

# KNN Regression
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsRegressor
url = "Buildings_Footprint.csv"
names = ['OBJECTID_1', 'OBJECTID', 'TAG', 'SUBTYPE', 'SRCDATE', 'SYMBOL', 'Shape_Leng', 'BUILDING_I', 'AREA_', 'PERIMETER', 'RuleID', 'GlobalID', 'URL', 'Shape__Area', 'Shape__Length']
dataframe = read_csv(url, delim_whitespace=True, names=names)
array = dataframe.values
X = array[:,0:13]
Y = array[:,13]
kfold = KFold(n_splits=10, random_state=7)
model = KNeighborsRegressor()
scoring = 'neg_mean_squared_error'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print(results.mean())

import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["BUILDING_I", "PERIMETER"]
df = pd.read_csv("https://data.baltimorecity.gov/datasets/baltimore::buildings-footprint.csv", usecols=columns)
print("Contents in csv file:", df)
plt.plot(df.BUILDING_I, df.PERIMETER)
plt.show()

import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["BUILDING_I", "AREA_"]
df = pd.read_csv("https://data.baltimorecity.gov/datasets/baltimore::buildings-footprint.csv", usecols=columns)
print("Contents in csv file:", df)
plt.plot(df.BUILDING_I, df.AREA_)
plt.show()

# Compare Algorithms
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# load dataset
url = "Buildings_Footprint.csv"
names = ['OBJECTID_1', 'OBJECTID', 'TAG', 'SUBTYPE', 'SRCDATE', 'SYMBOL', 'Shape_Leng', 'BUILDING_I', 'AREA_', 'PERIMETER', 'RuleID', 'GlobalID', 'URL', 'Shape__Area', 'Shape__Length']
dataframe = read_csv(url, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
# prepare models
models = []
models.append(('LR', LogisticRegression(solver='liblinear')))
models.append(('LDA', LinearDiscriminantAnalysis()))
# evaluate each model in turn
results = []
names = []
scoring = 'accuracy'
for name, model in models:
	kfold = KFold(n_splits=10, random_state=7)
	cv_results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)

# Grid Search for Algorithm Tuning
from pandas import read_csv
import numpy
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
url = "Buildings_Footprint.csv"
names = ['OBJECTID_1', 'OBJECTID']
dataframe = read_csv(url, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,1]
alphas = numpy.array([1,0.1,0.01,0.001,0.0001,0])
param_grid = dict(alpha=alphas)
model = Ridge()
grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=3)
grid.fit(X, Y)
print(grid.best_score_)
print(grid.best_estimator_.alpha)

# Random Forest Classification
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
url = "Buildings_Footprint.csv"
names = ['OBJECTID_1', 'OBJECTID', 'TAG', 'SUBTYPE', 'SRCDATE', 'SYMBOL', 'Shape_Leng', 'BUILDING_I', 'AREA_', 'PERIMETER', 'RuleID', 'GlobalID', 'URL', 'Shape__Area', 'Shape__Length']
dataframe = read_csv(url, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
num_trees = 100
max_features = 3
kfold = KFold(n_splits=10, random_state=7)
model = RandomForestClassifier(n_estimators=num_trees, max_features=max_features)
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())

# Save Model Using Pickle
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
url = "Buildings_Footprint.csv"
names = ['OBJECTID_1', 'OBJECTID', 'TAG', 'SUBTYPE', 'SRCDATE', 'SYMBOL', 'Shape_Leng', 'BUILDING_I', 'AREA_', 'PERIMETER', 'RuleID', 'GlobalID', 'URL', 'Shape__Area', 'Shape__Length']
dataframe = read_csv(url, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
# Fit the model on 67%
model = LogisticRegression(solver='liblinear')
model.fit(X_train, Y_train)
# save the model to disk
filename = 'finalized_building_model.sav'
pickle.dump(model, open(filename, 'wb'))

# some time later...

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)

import pandas as pd # data processing
import numpy as np # working with arrays
import matplotlib.pyplot as plt # visualization
import seaborn as sb # visualization
from termcolor import colored as cl # text customization

from sklearn.model_selection import train_test_split # data split

from sklearn.linear_model import LinearRegression # OLS algorithm
from sklearn.linear_model import Ridge # Ridge algorithm
from sklearn.linear_model import Lasso # Lasso algorithm
from sklearn.linear_model import BayesianRidge # Bayesian algorithm
from sklearn.linear_model import ElasticNet # ElasticNet algorithm

from sklearn.metrics import explained_variance_score as evs # evaluation metric
from sklearn.metrics import r2_score as r2 # evaluation metric

sb.set_style('whitegrid') # plot style
plt.rcParams['figure.figsize'] = (20, 10) # plot size



