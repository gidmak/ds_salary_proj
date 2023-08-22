# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:41:46 2023

@author: Gideon Markus
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#Read dataset into a dataframe
df = pd.read_csv('eda_data.csv')

# TODOs
# Choosing the right columns
# Get dummy data
# Train test split
# Multiple linear regression
# Lasso regression
# Random forest
# Tune models GridsearchCV
# Test ensembles 

# Choosing the right columns
df_model = df[['avg_salary','Rating', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue','num_competitor','hourly','employer_provided', 'job_state', 'same_state', 'age', 'python_yn', 'spark', 'aws', 'excel', 'job_simp', 'seniority', 'desc_length']]

# Get dummy data
df_dum = pd.get_dummies(df_model)

# Train test split
from sklearn.model_selection import train_test_split

X = df_dum.drop('avg_salary', axis = 1)
y = df_dum.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Multiple linear regression
import statsmodels.api as sm
X_sm = X = sm.add_constant(X)
model = sm.OLS(y, X_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score
lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm, X_train, y_train, scoring = 'neg_mean_absolute_error', cv=3))

# Lasso regression
lm_l = Lasso()
np.mean(cross_val_score(lm_l, X_train, y_train, scoring = 'neg_mean_absolute_error', cv=3))
