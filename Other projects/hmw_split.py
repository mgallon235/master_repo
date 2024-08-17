import random
import pandas as pd
import numpy as np
import pygsheets

#  Connecting to Google Sheets
gc = pygsheets.authorize(service_file='/Users/mikelgallo/repos/master_repo/account_credentials.json')
sh = gc.open_by_key('1VicApobFt2rStzzJU_y2wUBAHVvQEeFUs-qW0UKac-E')


dir = {'chores':['a','b','c','d','e','f','g','i'],
       'weight':[6,6,6,4,6,4,3,8]}

df = pd.DataFrame.from_dict(dir)

df

'''  ------------------------------- Who is doing 7 points this week'''

participants = ['Rui','Mikel','Miguel']

'''  ------------------------------- Shuffle Dataset '''

dataset = df.sample(frac = 1).copy()

'''  ------------------------------- rolling sum'''
##participant_1   
diction = {}

dataset['r_sum'] = dataset['weight'].expanding().sum()

participant_1 = random.sample(participants,1)
p1 = dataset[dataset['r_sum']<=21]

diction[participant_1[0]] = p1['chores'].tolist()

diction
participant_1[0]
##participant_2
participant_2 = random.sample(['Mikel','Miguel'],1)
participant_2
dataset_2 = dataset[~ dataset['chores'].isin(p1['chores'])]
dataset_2
dataset_2['r_sum_2'] = dataset_2['weight'].expanding().sum()

diction[participant_2[0]] = dataset_2['chores'].tolist()

diction['Mikel'] = ['h']

diction


'''  ------------------------------- spliting chores'''

participant1_chores = dataset[dataset['r_sum']<=7]
participant2_chores = dataset[~ dataset['chores'].isin(participant1_chores['chores'])]

## Assign owner to each chore list
participant1_chores['owner'] = participant_7_owner
participant2_chores['owner'] = participant_6_owner


'''  ------------------------------- exporting to gsheets'''
# Check gsheet title
sh.title

# Check existing worksheets
sh.worksheets()

#Clean rows
sh[0].clear('A2')
sh[1].clear('A2')

#export participant_1
sh[0].set_dataframe(participant1_chores, 'A1')

#export participant_1
sh[1].set_dataframe(participant2_chores, 'A1')