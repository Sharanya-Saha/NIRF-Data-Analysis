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
# 5. (Total allowed - actually admitted) percentage?
# 
# =============================================================================

import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

df = pd.read_csv(r"Datasets/total-actual-strength.csv")
home = pd.read_csv(r"Datasets/sanctioned-intake.csv")

df = df[['Institute', 'Programs', 'Total Students']]
home = home[['Institute', 'Academic Year', '2019-20']]

#df.columns
#home.columns

for index, row in df.iterrows():
    st =  row[1].replace('\n',' ')
    st =  st.replace('Year ','Years ')
    df.at[index,'Programs'] = st
    
for index, row in home.iterrows():
    st =  row[1].replace('Year ','Years ')
    home.at[index,'Academic Year'] = st

home.columns = ['Institute', 'Programs', 'sanctioned-intake']
df.columns = ['Institute', 'Programs', 'Actual intake']

final = df.merge(home, how='inner', on=['Institute', 'Programs'])
final.columns

final['Actual/Sanctioned'] = ((final['Actual intake'] - final ['sanctioned-intake'])*100 )/final ['sanctioned-intake'] 

final.sort_values('Actual/Sanctioned', inplace=True, ascending=False)

# =============================================================================
# 
#       final contains overflow amt. + shows overflow and - shows underflow
# 
# =============================================================================


left = final[final['Actual/Sanctioned']<0]
left = left[['Institute', 'Programs', 'Actual/Sanctioned']]
left.columns = ['Institute', 'Programs', 'Vacancies-Percent']

excessive = final[final['Actual/Sanctioned']>=0]
excessive = excessive[['Institute', 'Programs', 'Actual/Sanctioned']]
excessive.columns = ['Institute', 'Programs', 'Overfill-percent']


left['Vacancies-Percent']=left['Vacancies-Percent'].apply(lambda x: x*-1)


left = left.sort_values('Vacancies-Percent', ascending = False)

excessive = excessive.sort_values('Overfill-percent', ascending = False)


left.to_csv('Outputs/Top institutes with highest number of vacancies.csv', index = False)
excessive.to_csv('Outputs/Top institutes with highest overfill percent.csv', index = False)

