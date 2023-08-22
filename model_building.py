# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:05:12 2023

@author: Gideon Markus
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
df_model = df[['avg_salary','Rating', 'Size', 'Type of ownership', 'Industry','Sector',         'Revenue','num_competitor','hourly','employer_provided', 'job_state', 'same_state','age','python_yn','spark','aws','excel','job_simp','seniority','desc_length']]

