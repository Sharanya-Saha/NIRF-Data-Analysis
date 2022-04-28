#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 19:53:51 2021

@author: pranshu
"""
# =============================================================================
# 
# Total-actual-strength 
# 
# 1. Which program in each of the top(5) institutes has the highest/lowest female
#    to male ratio? (perform a statistical test as well (check if it is meaningful))
# 
# =============================================================================

# Set the figure size - handy for larger output
import matplotlib.pyplot as plt# Set up with a higher resolution screen (useful on Mac)

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

df = pd.read_csv(r"Datasets/total-actual-strength.csv")



df['ratio'] = df['No. of Female Students'] / df['No. of Male Students']
df.columns

qq = list(df['Institute'].unique())

final = pd.DataFrame(columns = ['Institute', 'Maximum Programs', 'Maximum Ratio','Minimum Programs', 'Minimum Ratio'])

for i in qq:
    new = df.copy()
    this = pd.DataFrame(columns = new.columns)
    new = new.loc[new['Institute'] == i]
    new = new.sort_values('ratio', ascending = False)
    new.reset_index(inplace=True, drop=True)
    
    this.loc[0] = new.loc[0]
    this.loc[1] = new.loc[len(new.index)-1]
    
    
    mm = len(final.index)
    final.loc[mm,'Institute' ] = this.loc[0,'Institute']
    final.loc[mm,'Maximum Programs' ] = new.loc[0,'Programs']
    final.loc[mm,'Maximum Ratio' ] = new.loc[0,'ratio']
    final.loc[mm,'Minimum Programs' ] = new.loc[1,'Programs']
    final.loc[mm,'Minimum Ratio' ] = new.loc[1,'ratio']

#==============================================================================
# final has the answer

final.columns

final1 = final[['Institute', 'Minimum Programs','Minimum Ratio']]

final.drop(['Minimum Programs','Minimum Ratio'],axis=1, inplace=True)

final.sort_values('Maximum Ratio', ascending = False, inplace=True)
final1.sort_values('Minimum Ratio', inplace=True)

final.reset_index(inplace=True, drop=True)
final1.reset_index(inplace=True, drop=True)

final = final[1:]

final['Maximum Ratio']= final['Maximum Ratio'].astype(float)



final.to_csv('Outputs/Top institues with highest female-male ratio.csv', index = False)
final1.to_csv('Outputs/Top institues with lowest female-male ratio.csv', index = False)