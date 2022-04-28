#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 19:51:55 2021

@author: pranshu
"""
# =============================================================================
# 
# Total-actual-strength 
# 
# 3. Which institute offers the maximum people a full waiver in fee?-----------> only institute?
# 
# =============================================================================

import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

df = pd.read_csv(r"Datasets/total-actual-strength.csv")

#df.columns

df = df[['Institute', 'Programs', 'Total Students',
       'No. of studentsreceiving full tuition fee reimbursement from the State and Central Government',
       'No. of students receiving full tuition fee reimbursement from Institution Funds',
       'No. of students receiving full tuition fee reimbursement from the Private Bodies']] 

df['Total reimbursement'] = df['No. of studentsreceiving full tuition fee reimbursement from the State and Central Government'] + df['No. of students receiving full tuition fee reimbursement from Institution Funds'] + df['No. of students receiving full tuition fee reimbursement from the Private Bodies']


# =============================================================================
# 
# 
#       max reimbursement provided
# 
# 
# =============================================================================

home = df.copy()
home = home[['Institute', 'Programs', 'Total Students','Total reimbursement']]

home = home.groupby('Institute').sum()
home['Institute'] = home.index
home.reset_index(inplace=True, drop=True)
home['percent reimbursement'] = home['Total reimbursement']*100/home['Total Students']

#home.columns
home = home[['Institute', 'Total Students', 'Total reimbursement', 'percent reimbursement']]

home = home.sort_values('percent reimbursement', ascending = False)
home.columns
home = home[['Institute',\
       'percent reimbursement']]
# =============================================================================
# 
# 
#   for which course the college provide maximum reimbursement
# 
# 
# 
# =============================================================================

df = df[['Institute', 'Programs', 'Total Students','Total reimbursement']]
df['percent reimbursement'] = df['Total reimbursement']*100/df['Total Students']

qq = list(df['Institute'].unique())

final = pd.DataFrame(columns = df.columns)
for i in qq:
    new = df.copy()
    new = new.loc[new['Institute'] == i]
    new = new.sort_values('percent reimbursement', ascending = False)
    new.reset_index(inplace=True, drop=True)

    mm = len(final.index)
    final.loc[mm,'Institute' ] = new.loc[0,'Institute']
    final.loc[mm,'Programs' ] = new.loc[0,'Programs']
    final.loc[mm,'Total Students' ] = new.loc[0,'Total Students']
    final.loc[mm,'Total reimbursement' ] = new.loc[0,'Total reimbursement']
    final.loc[mm,'Percent Reimbursement' ] = new.loc[0,'percent reimbursement']

# =============================================================================
# answer is in final and home data frames

final.columns

final = final[['Institute', 'Programs', 
       'Percent Reimbursement']]


final.sort_values('Percent Reimbursement', ascending = False, inplace=True)

final.to_csv('Outputs/Top programs and colleges which provide reimbursement to maximum number of students.csv', index = False)
