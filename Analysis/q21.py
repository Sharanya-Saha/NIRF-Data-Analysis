#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 19:25:54 2021

@author: kajal
"""
# =============================================================================
# 
# sponsorship:
# 2. Find the year in which every institute had the highest ratio for 
# projects/#agency among the above mentioned three years
# 
# =============================================================================

import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

df = pd.read_csv(r'Datasets/sponsorship.csv')

#df.columns

df = df.sort_values(['Institute','Financial Year'],ascending = True)
df.reset_index(inplace=True, drop=True)

qq  =list(df['Institute'].unique())
qq
#alpha = df.groupby('Institute')

result= pd.DataFrame(columns = ['Institute','year', 'ratio'])

lst = ['2019-20', '2018-19', '2017-18']

for i in qq:
    here = []
    home = df.copy()
    home = home.loc[home['Institute'] == i]
    home.reset_index(inplace=True, drop=True)
    
    mm = len(result.index)
    result.loc[mm,'Institute'] = i
    
    here.append(home.loc[2,'2019-20'] / home.loc[1,'2019-20'])
    here.append( home.loc[2,'2018-19'] / home.loc[1,'2018-19'])
    here.append(home.loc[2,'2017-18'] / home.loc[1,'2017-18'])
    ratio = max(here)
    ind = here.index(ratio)
    
    result.loc[mm,'year'] = lst[ind]
    result.loc[mm,'ratio'] = ratio


#========================================================
# result has the final answer
result.to_csv('Outputs/max_project_year.csv', index=False)
