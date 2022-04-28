#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 23:59:43 2021

@author: sharanya
"""

import pandas as pd
from matplotlib import pyplot as plt
pd.options.mode.chained_assignment = None
df=pd.read_csv('Datasets/cosultancy.csv')

cols=['2019-20','2018-19','2017-18']
for col in cols :
    df[col] = df[col].astype(int)

df=df[df['Financial Year']=='Total no. of Consultancy Projects']

def yearwise(df,year) :
    df.sort_values(by=[year],inplace=True)
    highest=df[-5:]
    highest.sort_values(by=[year],inplace=True,ascending=False)
    return list(highest['Institute'])

l2019=yearwise(df, '2019-20')
l2018=yearwise(df, '2018-19')
l2017=yearwise(df, '2017-18')

temp={'2019-20':l2019,'2018-19':l2018,'2017-18':l2017}
temp_pd=pd.DataFrame(temp)

temp_pd.to_csv('Outputs/consultancy_projects_top5.csv',index=False)

df['total']=df['2019-20']+df['2018-19']+df['2017-18']
df.sort_values(by=['total'],inplace=True)
highest=df[-5:]
highest=highest[['Institute','2019-20','2018-19','2017-18']]

x=[1,2,3]
fig=plt.figure(figsize =(15, 5))
for i in range(5) :
    plt.plot(x,[highest.iloc[i][3],highest.iloc[i][2],highest.iloc[i][1]],label=highest.iloc[i][0])

plt.xticks(x,['2017-18','2018-19','2019-20'] )
plt.legend()
plt.title('Top 5 college trends',fontweight="bold")
plt.xlabel("Year")
plt.ylabel("No. of Consultancy Projects")
#plt.savefig('Outputs/Top-5-college-trends-consultancy-projects.jpg',dpi=300)
# plt.show() 
