#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 19:25:57 2021

@author: kajal
"""
# =============================================================================
# 
# sanctioned intake:
# 2. Find the total intake of every insti. And the top 5 and bottom 5 institutes.
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

ab = df.groupby('Institute').sum()
ab['Institute'] = ab.index
ab.reset_index(inplace=True, drop=True)

# =============================================================================
# 
#     
#     
#     year wise
#     
#     
#     
# =============================================================================
    
df1 = ab.copy()
df1 = df1.drop(['2018-19', '2017-18','2016-17', '2015-16', '2014-15'], axis = 1)
df1 = df1.sort_values('2019-20', ascending = False)

df2 = ab.copy()
df2  = df2.drop(['2019-20', '2017-18','2016-17', '2015-16', '2014-15'], axis = 1)
df2 = df2.sort_values('2018-19', ascending = False)

df3 = ab.copy()
df3 = df3.drop(['2019-20', '2018-19', '2016-17', '2015-16', '2014-15'], axis = 1)
df3 = df3.sort_values('2017-18', ascending = False)

df4 = ab.copy()
df4 = df4.drop(['2019-20', '2018-19', '2017-18', '2015-16', '2014-15'], axis = 1)
df4 = df4.sort_values('2016-17', ascending = False)

df5 = ab.copy()
df5 = df5.drop(['2019-20', '2018-19', '2017-18','2016-17', '2014-15'], axis = 1)
df5 = df5.sort_values('2015-16', ascending = False)

df6 = ab.copy()
df6 = df6.drop(['2019-20', '2018-19', '2017-18','2016-17', '2015-16'], axis = 1)
df6 = df6.sort_values('2014-15', ascending = False)

df1.to_csv('Outputs/2019-20_intake.csv', index=False)
df2.to_csv('Outputs/2018-19_intake.csv', index=False)
df3.to_csv('Outputs/2017-18_intake.csv', index=False)
df4.to_csv('Outputs/2016-17_intake.csv', index=False)
df5.to_csv('Outputs/2015-16_intake.csv', index=False)
df6.to_csv('Outputs/2014-15_intake.csv', index=False)

# =============================================================================
# 
#     
#     
#      total
#     
#     
#     ,,,,and
# =============================================================================
    
aa = ab.copy()

for index, row in aa.iterrows():
    aa.at[index, 'Total'] = row[0]+row[1]+row[2]+row[3]+row[4]+row[5]
    
aa = aa[['Institute', 'Total']]
aa = aa.sort_values('Total', ascending = False)

#==============================================================================
# generate please
aa.to_csv('Outputs/overall_intake.csv', index=False)




aa = aa[:5]    
