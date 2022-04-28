# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 02:08:09 2021

@author: Utkarsh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import os

#os.chdir(r"C:\Users\Utkarsh\Desktop\IITK Sem I\Data Mining CS685\Project")


df1 = pd.read_csv('./Datasets/placement2021.csv')
x1 =df1.copy()
x1 = x1[[ 'Institute', 'Program_name', 
       'No. of students\ngraduating in\nminimum stipulated\ntime',
       'No. of students\nplaced',
       'No. of students\nselected for Higher\nStudies','Median salary of\nplaced\ngraduates(Amount in\nRs.)']]
x1
df1

df2 = pd.read_csv('./Datasets/placement2020.csv')
x2 =df2.copy()
x2 = x2[[ 'Institute', 'Program_name', 
       'No. of students\ngraduating in\nminimum stipulated\ntime',
       'No. of students\nplaced',
       'No. of students\nselected for Higher\nStudies','Median salary of\nplaced\ngraduates(Amount in\nRs.)']]
x2

df3 = pd.read_csv('./Datasets/placement2019.csv')
x3 =df3.copy()
x3 = x3[[ 'Institute', 'Program_name', 
       'No. of students\ngraduating in\nminimum stipulated\ntime',
       'No. of students\nplaced',
       'No. of students\nselected for Higher\nStudies','Median salary of\nplaced\ngraduates(Amount in\nRs.)']]
x3
df3

x = pd.concat([x1,x2,x3],axis=0)
x.reset_index(drop=True, inplace=True)
x['Institute'] = x['Institute'].apply(lambda x: x.strip())
x['Program_name'] = x['Program_name'].apply(lambda x: x.strip())
x.drop_duplicates(keep='first',inplace=True)
x['Median salary of\nplaced\ngraduates(Amount in\nRs.)'] = x['Median salary of\nplaced\ngraduates(Amount in\nRs.)'].apply(lambda x:x.split('(')[0]).astype('int')
x.reset_index(drop=True, inplace=True)
x

y = x.copy()
y = y.groupby(['Institute','Program_name'])[['No. of students\ngraduating in\nminimum stipulated\ntime',
       'No. of students\nplaced',
       'No. of students\nselected for Higher\nStudies',
       'Median salary of\nplaced\ngraduates(Amount in\nRs.)']].agg('sum')
y['Program_name'] = y.index.to_numpy()
y['Program_name'] = y['Program_name'].apply(lambda x: x[1])
y['Institute'] = y.index.to_numpy()
y['Institute'] = y['Institute'].apply(lambda x: x[0])
y['Percentage getting placed'] = (y['No. of students\nplaced']/y['No. of students\ngraduating in\nminimum stipulated\ntime'])*100
y = y[['Institute',  'Program_name','Percentage getting placed']]
y.reset_index(drop=True, inplace=True)
y

highest =pd.DataFrame()
lowest = pd.DataFrame()
ans = pd.DataFrame()
for i in y['Institute'].unique():
    temp = y.copy().reset_index(drop=True)
    temp = temp[temp['Institute']==i]
    idx = temp['Percentage getting placed'].idxmax(axis=0)
    percentage,program_name = y.loc[idx]['Percentage getting placed'],y.loc[idx]['Program_name']
    d = {}
    d['Institute'] = i
    d['Program_name'] = program_name
    d['Percentage getting placed'] = percentage
    ans = ans.append(d,ignore_index=True)
ans

ans.to_csv('./Outputs/best_program.csv',index=False)

ans1 = pd.DataFrame()
for i in ans['Program_name'].unique():
    d ={}
    d['Program_name'] = i
    d['Frequency'] = len(ans[ans['Program_name']==i])
    ans1 =ans1.append(d,ignore_index=True)
ans1['Frequency'] = ans1['Frequency'].astype('int')
ans1 

plt.style.use('seaborn-whitegrid') 

plt.barh(ans1['Program_name'].to_list(), ans1['Frequency'].to_list(),height=0.5)
def addlabels(x,y):
    for i in range(len(x)):
        plt.text( y[i]+2,i-0.1, y[i],ha='center',fontsize=11)
x =  ans1['Program_name'].to_list()
y = ans1['Frequency'].to_list()
addlabels(x, y)

plt.ylabel('Program Name', fontweight ='bold')
plt.xlabel('Number of colleges', fontweight ='bold', fontsize = 10)
plt.title('Best Programs in terms of placements')
# plt.show()
