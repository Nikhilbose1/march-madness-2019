# To run add the files you want to use to the current directory. Then change the files list to contain the names of the
# files you want to use

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nikhil Bose & Joel Joseprabu
"""

import pandas as pd
from bracketeer import build_bracket

# Submission file
file = 'SubmissionStage2.csv'
seeds = 'data/NCAATourneySeeds.csv'

# load in the sample submissions spreadsheet
template = pd.read_csv('SampleSubmissionStage2.csv')
spreadsheet = template.iloc[:, :].values

# load data from submission
data = pd.read_csv(file)
data_values = data.iloc[:, :].values

# load seed file
seeds = pd.read_csv(seeds)

# fetch seet and recalculate probability
for i in range(0, len(spreadsheet)):
    id_field = data_values[i][0]
    pred_field = data_values[i][1]
    split_id = id_field.split('_')
    season = int(split_id[0])
    team_1 = int(split_id[1])
    team_2 = int(split_id[2])

    team_1_seed = int(seeds[(seeds['Season'] == season) & (seeds['TeamID'] == team_1)].iloc[0][1][1:3])
    team_2_seed = int(seeds[(seeds['Season'] == season) & (seeds['TeamID'] == team_2)].iloc[0][1][1:3])

    cutoff = 0.5
    if (team_1_seed < team_2_seed):
        cutoff -= ((team_1_seed - team_2_seed)**2 / 500)
    else:
        cutoff += ((team_1_seed - team_2_seed)**2 / 500)

    pred = 0.5
    if (pred_field > cutoff):
        pred = 0.5 + (((pred_field - cutoff) / (1 - cutoff)) * (0.5))
    else:
        pred = 0.5 - (((cutoff - pred_field) / (cutoff)) * (0.5))

    spreadsheet[i][1] = pred

# create dataframe to match sample submissions spreadsheet
results = pd.DataFrame(data = spreadsheet, columns=["ID", "Pred"])

# save new submissions spreadsheet as csv to disk
results.to_csv('SubmissionStage2Seeded.csv', sep = ',', encoding = 'utf-8', index = False)

m = build_bracket(outputPath = 'seededbracket.png',
	teamsPath = 'data/Teams.csv',
	seedsPath = 'data/NCAATourneySeeds.csv',
	submissionPath = 'SubmissionStage2Seeded.csv',
	slotsPath = 'data/NCAATourneySlots.csv',
	year = 2019)

# output feedback
print()
print()
print("Teams selected with seeding; new bracket created.")
print()
print()