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
# 2. For all the insti find  the ratio of socially challenged (Sc/st, OBC etc) to 
#  total number of children as well as economically backward people ?
# 
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import warnings
import numpy as np
warnings.filterwarnings('ignore', category=FutureWarning)
import os

df = pd.read_csv(r"Datasets/total-actual-strength.csv")

df.columns
df = df.groupby('Institute').sum()
df['Institute'] = df.index
df.reset_index(inplace = True,drop = True)
df1 = df[['Institute', 'Total Students','SociallyChallenged (SC+ST+OBC Including male & female)']]
df = df[['Institute', 'Total Students','EconomicallyBackward(Including male & female)']]

df['ratio economic'] = df['EconomicallyBackward(Including male & female)'] / df['Total Students']
df1['ratio social'] = df1['SociallyChallenged (SC+ST+OBC Including male & female)'] / df1['Total Students']

# =============================================================================
# df and df1 has the answer
# havnt made any graph. vo dekh lena ek baar

df.sort_values("ratio economic", inplace=True, ascending=False)


df1.sort_values("ratio social", inplace=True, ascending=False)

df = df[["Institute", "ratio economic"]]
df1 = df1[["Institute", "ratio social"]]


df.to_csv('Outputs/Top institues with highest economically backward-total ratio.csv', index = False)
df1.to_csv('Outputs/Top institues with highest socaially backward-total ratio.csv', index = False)






#==============================================================================
# final has the answer