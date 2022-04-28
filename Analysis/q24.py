#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 19:51:56 2021

@author: kajal
"""
# =============================================================================
# 
# Total-actual-strength 
# 6. Report colleges having rare courses (PG 1 year).
# 
# =============================================================================

import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

df = pd.read_csv(r"Datasets/total-actual-strength.csv")

#df.columns
#r"Datasets/total-actual-strength.csv")
qq = list(df['Programs'].unique()) 
aa = pd.DataFrame(columns = ['Programs', 'Count'])

aa['Programs'] = qq
aa['Count'] = 0

for i in range(len(df)):
    for xx in range(len(aa)):
        if df.loc[i,'Programs'] == aa.loc[xx,'Programs']:
            aa.loc[xx,'Count'] = aa.loc[xx,'Count']+1
            break

aa = aa.sort_values('Count',ascending=False)
aa.reset_index(inplace = True, drop=True)


# =============================================================================
#       plot a graph for the courses vs freuqency
# =============================================================================

aa.groupby(['Programs']).sum().plot(kind='pie', subplots=True, startangle=90,figsize=(15,10), autopct='%1.1f%%')
size = len(aa)

aa = aa[size-3:]
aa.reset_index(inplace = True, drop=True)

# =============================================================================
# aa has the count for every college

# we are cosidering the last three rows as rare

# =============================================================================

df = df[['Institute', 'Programs']]
final = pd.DataFrame(columns = ['Institute','Programs'])

for index, row in df.iterrows():
    if (row[1] == aa.loc[0,'Programs']) or (row[1] == aa.loc[1,'Programs']) or (row[1] == aa.loc[2,'Programs']): 
            final.loc[len(final.index)] = row

final = final.sort_values('Programs')

# =============================================================================
# final contains the answer for the question 
final.to_csv('Outputs/rare_program.csv', index=False)
