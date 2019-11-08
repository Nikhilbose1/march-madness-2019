# To run add the files you want to use to the current directory. Then change the files list to contain the names of the
# files you want to use

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nikhil Bose
"""
# -------------------------
# IMPORT NECESSARY MODULES
# -------------------------
import pandas as pd

# Files to consider
files = ['SubmissionStage2-Logistic Regression.csv', 'SubmissionStage2 - Neural Network.csv']
# list to store data from each file
files_data = []

# load in the sample submissions spreadsheet
template = pd.read_csv('SampleSubmissionStage2.csv')
spreadsheet = template.iloc[:, :].values

# load data from files
for file in files:
    data = pd.read_csv(file)
    data_values = data.iloc[:, :].values
    files_data.append(data_values)

# add the prediction to each prediction index
for i in range(0, len(spreadsheet)):
    diff = -1
    for file_data in files_data:
        if abs(.5 - file_data[i][1]) > diff:
            prediction = file_data[i][1]
            diff = abs(.5 - file_data[i][1])
    spreadsheet[i][1] = round(prediction, 5)

# create dataframe to match sample submissions spreadsheet
results = pd.DataFrame(data = spreadsheet, columns=["ID", "Pred"])

# save new submissions spreadsheet as csv to disk
results.to_csv('SubmissionStage2.csv', sep = ',', encoding = 'utf-8', index = False)

# output feedback
print()
print()
print("Most confident predictions selected.")
print()
print()