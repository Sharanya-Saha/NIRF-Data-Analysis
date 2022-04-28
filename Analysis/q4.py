#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 19:51:56 2021

@author: pranshu
"""
# =============================================================================
# 
# Total-actual-strength 
# 
# 4. Which institute has the percentage of people who do not belong to its state 
# (foreign as well as different states)?
# ie show the diversity present among the students of each course(ratio of instate to outside students)
#
#
# =============================================================================

import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

df = pd.read_csv(r"Datasets/total-actual-strength.csv")

#df.columns
df['total outside'] = df['Outside State(Including male& female)'] + df['Outside Country(Including male& female)']
df = df[['Institute', 'Programs','Total Students', 'Within State(Including male& female)','total outside']]

df = df.groupby('Institute').sum()
df['Institute'] = df.index
df.reset_index(inplace=True, drop=True)

df['belonging outside state'] = df['total outside']*100/df['Total Students']
df = df.sort_values('belonging outside state', ascending = False)
df.columns

df = df[['Institute', 'belonging outside state']]
df.columns = ['Institute', 'Percentage of students who\'re not from the same state']
#========================================================
# df has the final answer



df.to_csv('Outputs/Top institues with highest number of migrants.csv', index=False)

