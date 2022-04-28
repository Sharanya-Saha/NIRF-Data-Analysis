#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 01:06:07 2021

@author: sharanya
"""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
pd.options.mode.chained_assignment = None
df=pd.read_csv('Datasets/cosultancy.csv')

    
    
cols=['2019-20','2018-19','2017-18']
for col in cols :
    df[col] = df[col].astype(int)

    
needed=pd.read_csv('Datasets/Consistent_Institutes.csv')
notneeded=list(set(list(df['Institute']))-set(list(needed['Institute'])))

for i in notneeded :
    df=df[df['Institute']!=i]




projects_df=df[df['Financial Year']=='Total no. of Consultancy Projects']
client_df=df[df['Financial Year']=='Total no. of Client Organizations']
projects_df.sort_values(by=['Institute'],inplace=True)
client_df.sort_values(by=['Institute'],inplace=True)
projects_df=projects_df.reset_index()
client_df=client_df.reset_index()

projects_df=projects_df[['Institute','2019-20','2018-19','2017-18']]
client_df=client_df[['Institute','2019-20','2018-19','2017-18']]


for col in cols :
    projects_df[f'ratio {col}']=projects_df[col]/client_df[col]
    
projects_df=projects_df[['Institute','ratio 2019-20','ratio 2018-19','ratio 2017-18']]
projects_df.columns=['Institute','2019-20','2018-19','2017-18']
projectstoclients19=projects_df[['Institute','2019-20']]
projectstoclients18=projects_df[['Institute','2018-19']]
projectstoclients17=projects_df[['Institute','2017-18']]
projectstoclients19.sort_values(by=['2019-20'],inplace=True)
projectstoclients18.sort_values(by=['2018-19'],inplace=True)
projectstoclients17.sort_values(by=['2017-18'],inplace=True)


projectstoclients17['More']=0
projectstoclients17.loc[projectstoclients17['2017-18']>=2,'More']=1
projectstoclients17.loc[projectstoclients17['2017-18']<1,'More']=2
t_2017=projectstoclients17['More'].value_counts()


projectstoclients18['More']=0
projectstoclients18.loc[projectstoclients18['2018-19']>=2,'More']=1
projectstoclients18.loc[projectstoclients18['2018-19']<1,'More']=2
t_2018=projectstoclients18['More'].value_counts()

projectstoclients19['More']=0
projectstoclients19.loc[projectstoclients19['2019-20']>=2,'More']=1
projectstoclients19.loc[projectstoclients19['2019-20']<1,'More']=2
t_2019=projectstoclients19['More'].value_counts()

barWidth = 0.1
fig = plt.subplots(figsize =(5, 5))
 
# set height of bar
less_than_1 =[t_2017[2],t_2018[2],t_2019[2]] 
greater_than_2 =[t_2017[1],t_2018[1],t_2019[1]] 
 
# Set position of bar on X axis
br1 = np.arange(len(less_than_1))
br2 = [x + barWidth for x in br1]

 
# Make the plot
plt.bar(br1, less_than_1, width = barWidth,
        edgecolor ='grey', label ='Ratio < 1')
plt.bar(br2, greater_than_2, width = barWidth,
        edgecolor ='grey', label ='Ratio >=2')

 
# Adding Xticks
plt.xlabel('Year', fontweight ='bold', fontsize = 8)
plt.ylabel('Number of Institutes', fontweight ='bold', fontsize = 8)
plt.xticks([r + barWidth for r in range(len(less_than_1))],
        ['2017-18', '2018-19','2019-20'])

plt.title('Comaparison of Ratios of number of projects to number of clients')
plt.legend()
#plt.savefig('Outputs/Comparison of Number of Sponsored Projects to Consultancy Projects.jpg',dpi=100)
# plt.show()


projects_df.to_csv('Outputs/consultancy-project-to-client-ratio.csv',index=False)



projects_df['Max'] = projects_df[cols].idxmax(axis=1)
projects_df=projects_df[['Institute','Max']]
projects_df.columns=['Institute','Year (Maximum)']
xp=projects_df['Year (Maximum)'].value_counts()
fig = plt.subplots(figsize =(5, 5))
xp.plot.bar()
plt.xlabel('Year')
plt.ylabel('Number of Institutes')
projects_df.to_csv('Outputs/Maximum-project-to-client-ratio-year.csv',index=False)

