#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 19:25:54 2021

@author: kajal
"""
# =============================================================================
# 
# sanctioned intake:
# 1. Which program per institute had the highest as well as the lowest intake for the last 2-3 years?
# 
# =============================================================================

import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

df = pd.read_csv(r'Datasets/sanctioned-intake.csv')

df = df.replace(['-'],[0]) 
#df.columns
    
df['2019-20'] = df['2019-20'].astype(int)
df['2018-19'] = df['2018-19'].astype(int)
df['2017-18'] = df['2017-18'].astype(int)
df['2016-17'] = df['2016-17'].astype(int)
df['2015-16'] = df['2015-16'].astype(int)
df['2014-15'] = df['2014-15'].astype(int)

for index, row in df.iterrows():
    df.at[index, 'Total'] = row[2]+row[3]+row[4]+row[5]+row[6]+row[7]
    
df = df[['Institute', 'Academic Year', 'Total']]
df = df.sort_values('Institute', ascending = False)
df.reset_index(inplace = True, drop = True)


final = pd.DataFrame(columns=['Institute','Maximum Course','Maximum Number', 'Minimum Course', 'Minimum Number'])
qq =  list(df['Institute'].unique())

for i in qq:
    now = df.copy()
    now = now.loc[now['Institute']==i]
    now['Total'] = now['Total'].astype(int)
    now = now.sort_values('Total', ascending=False)
    now.reset_index(inplace = True, drop = True)
    
    end = len(now.index)
    end-=1
    # select 1st and last row
    here = len(final.index)
    final.at[here,'Institute'] = now.loc[0,'Institute']
    final.at[here,'Maximum Course'] = now.loc[0,'Academic Year']
    final.at[here,'Maximum Number'] = now.loc[0,'Total']
    final.at[here,'Minimum Course'] = now.loc[end,'Academic Year']
    final.at[here,'Minimum Number'] = now.loc[end,'Total']


#========================================================
# final has the final answer
final.to_csv('Outputs/min_max_program.csv', index=False)


