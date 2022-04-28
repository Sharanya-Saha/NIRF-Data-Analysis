#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 19:25:54 2021

@author: kajal
"""
# =============================================================================
# 
# sponsorship:
# Find the top 5 (in decreasing order) institute which received 
# the highest amount over the period across last three years, 2017-18 to 2019-20.
# 
# =============================================================================

import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

df = pd.read_csv(r'Datasets/sponsorship.csv')

#df.columns

df = df.sort_values(['Institute','Financial Year'],ascending = True)
df.reset_index(inplace=True, drop=True)

df = df.loc[df['Financial Year'] == 'Total Amount Received (Amount in Rupees)']

for i,row in df.iterrows():
    df.at[i,'Total'] = row[2] + row[3] + row[4]


df = df.sort_values('Total',ascending = False)
df.reset_index(inplace=True, drop=True)

df = df[:5]
df = df[['Institute','Total']]
#========================================================
# df has the final answer

df.to_csv('Outputs/highest_sponsorship.csv', index=False)


