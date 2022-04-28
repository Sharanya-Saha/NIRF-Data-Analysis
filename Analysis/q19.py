#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 15:50:31 2021

@author: sharanya
"""

import pandas as pd
from matplotlib import pyplot as plt
pd.options.mode.chained_assignment = None
df1=pd.read_csv('Datasets/cosultancy.csv')
df2=pd.read_csv('Datasets/sponsorship.csv')

cols=['2019-20','2018-19','2017-18']
for col in cols :
    df1[col] = df1[col].astype(int)
    df2[col] = df2[col].astype(int)
    
df1=df1[df1['Financial Year']=='Total no. of Consultancy Projects']
df2=df2[df2['Financial Year']=='Total no. of Sponsored Projects']
df1=df1[['Institute','2019-20','2018-19','2017-18']]
df2=df2[['Institute','2019-20','2018-19','2017-18']]

needed=pd.read_csv('Datasets/Consistent_Institutes.csv')
needed_ls=list(needed['Institute'])
ins_2021=list(df1['Institute'])

not_needed=list(set(ins_2021)-set(needed_ls))

for ins in not_needed :
    df1=df1[df1['Institute']!=ins]
    
for ins in not_needed :
    df2=df2[df2['Institute']!=ins]
    
df1.sort_values(by=['Institute'],inplace=True)
df2.sort_values(by=['Institute'],inplace=True)
df1=df1.reset_index()
df2=df2.reset_index()

df1=df1[['Institute','2019-20','2018-19','2017-18']]
df2=df2[['Institute','2019-20','2018-19','2017-18']]

df1.columns=['Institute','c19-20','c18-19','c17-18']
df2.columns=['Institute','s19-20','s18-19','s17-18']

df1['s19-20']=df2['s19-20']
df1['s18-19']=df2['s18-19']
df1['s17-18']=df2['s17-18']

df1['Total19-20']=df1['s19-20']+df1['c19-20']
df1['Total18-19']=df1['s18-19']+df1['c18-19']
df1['Total17-18']=df1['s17-18']+df1['c17-18']

df1['Reasearch Project%(2017-18)']=df1['s17-18']/df1['Total17-18']
df1['Reasearch Project%(2018-19)']=df1['s18-19']/df1['Total18-19']
df1['Reasearch Project%(2019-20)']=df1['s19-20']/df1['Total19-20']

df1['Consultancy Project%(2017-18)']=df1['c17-18']/df1['Total17-18']
df1['Consultancy Project%(2018-19)']=df1['c18-19']/df1['Total18-19']
df1['consultancy Project%(2019-20)']=df1['c19-20']/df1['Total19-20']

df1['Consultancy Project%(2017-18)']=df1['Consultancy Project%(2017-18)']*100
df1['Consultancy Project%(2018-19)']=df1['Consultancy Project%(2018-19)']*100
df1['consultancy Project%(2019-20)']=df1['consultancy Project%(2019-20)']*100

df1['Reasearch Project%(2017-18)']=df1['Reasearch Project%(2017-18)']*100
df1['Reasearch Project%(2018-19)']=df1['Reasearch Project%(2018-19)']*100
df1['Reasearch Project%(2019-20)']=df1['Reasearch Project%(2019-20)']*100

df1=df1[['Institute','Reasearch Project%(2017-18)','Reasearch Project%(2018-19)','Reasearch Project%(2019-20)','Consultancy Project%(2017-18)','Consultancy Project%(2018-19)','consultancy Project%(2019-20)']]
df1.to_csv('Outputs/Sponsored Research projects and consultancy projects.csv',index=False)
