#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 18:33:57 2021

@author: sharanya
"""

import pandas as pd
from matplotlib import pyplot as plt
pd.options.mode.chained_assignment = None

def Visualization(df,year) :
    highest=df[-5:]
    lowest=df[0:5]
    highest.sort_values(by=[year],inplace=True,ascending=False)
    highest.columns=['Institute','Amount Received']
    lowest.columns=['Institute','Amount Received']
    highest.to_csv(f'Outputs/top5-consultancy-funding-{year}',index=False)
    lowest.to_csv(f'Outputs/bottom5-consultancy-funding-{year}',index=False)
    total= df[year].sum()
    top5_total=highest['Amount Received'].sum()
    left=total-top5_total
    highest.loc[len(highest.index)] = ['Rest of the colleges', left]
    highest['Percentage']=(highest['Amount Received']/total)*100
    fig = plt.figure(figsize =(15, 10))
    plt.pie(highest['Percentage'], labels = highest['Institute'],startangle=360, autopct='%1.0f%%')
    plt.title(f'Outputs/Visualization of fundings recieved through consultancy projects for {year}',fontweight="bold")
    #plt.savefig(f'Outputs/Visualization of fundings recieved through consultancy projects for {year}.jpg',dpi=300)
    # plt.show()   
    


df=pd.read_csv('Datasets/cosultancy.csv')
cols=['2019-20','2018-19','2017-18']
for col in cols :
    df[col] = df[col].astype(int)

amount_df=df[df['Financial Year']=='Total Amount Received (Amount in Rupees)']
amt_2019=amount_df[['Institute','2019-20']]
amt_2018=amount_df[['Institute','2018-19']]
amt_2017=amount_df[['Institute','2017-18']]

amt_2017.sort_values(by=['2017-18'],inplace=True)
amt_2018.sort_values(by=['2018-19'],inplace=True)
amt_2019.sort_values(by=['2019-20'],inplace=True)

Visualization(amt_2017, '2017-18')
Visualization(amt_2018, '2018-19')
Visualization(amt_2019, '2019-20')
