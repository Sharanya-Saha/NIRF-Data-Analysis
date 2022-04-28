# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 02:19:35 2021

@author: Utkarsh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import os
warnings.filterwarnings('ignore')

#os.chdir(r"C:\Users\Utkarsh\Desktop\IITK Sem I\Data Mining CS685\Project")

df1 = pd.read_csv('./Datasets/placement2021.csv')
x1 =df1.copy()
x1 = x1[[ 'Institute', 'Program_name', 'Academic Year.2',
       'No. of students\ngraduating in\nminimum stipulated\ntime',
       'No. of students\nplaced',
       'No. of students\nselected for Higher\nStudies']]
x1
df1

df2 = pd.read_csv('./Datasets/placement2020.csv')
x2 =df2.copy()
x2 = x2[[ 'Institute', 'Program_name', 'Academic Year.2',
       'No. of students\ngraduating in\nminimum stipulated\ntime',
       'No. of students\nplaced',
       'No. of students\nselected for Higher\nStudies']]
x2

df3 = pd.read_csv('./Datasets/placement2019.csv')
x3 =df3.copy()
x3 = x3[[ 'Institute', 'Program_name', 'Academic Year.2',
       'No. of students\ngraduating in\nminimum stipulated\ntime',
       'No. of students\nplaced',
       'No. of students\nselected for Higher\nStudies']]
x3

x = pd.concat([x1,x2,x3],axis=0)
# x.sort_values('Institute',ascending=False,inplace=True)
x.reset_index(drop=True, inplace=True)
x['Institute'] = x['Institute'].apply(lambda x: x.strip())
x['Program_name'] = x['Program_name'].apply(lambda x: x.strip())
x.drop_duplicates(keep='first',inplace=True)
x.reset_index(drop=True, inplace=True)
x

y = x.copy()
y = y.groupby(['Institute','Academic Year.2']).agg('sum')
y['Academic Year.2'] = y.index.to_numpy()
y['Academic Year.2'] = y['Academic Year.2'].apply(lambda x: x[1])
y['Institute'] = y.index.to_numpy()
y['Institute'] = y['Institute'].apply(lambda x: x[0])
y.reset_index(drop=True, inplace=True)
y['Percentage of unplaced'] = ((y['No. of students\ngraduating in\nminimum stipulated\ntime'] - y['No. of students\nplaced'] - y['No. of students\nselected for Higher\nStudies'])/y['No. of students\ngraduating in\nminimum stipulated\ntime'])*100
y.fillna(0,inplace=True)
y = y[['Institute','Academic Year.2','Percentage of unplaced']]
y.columns = ['Institute','Academic Year','Percentage of unplaced']
y
final = y.copy()

highest =pd.DataFrame()
lowest = pd.DataFrame()

for i in y['Academic Year'].unique():
    temp = y.copy().reset_index(drop=True)
    temp = temp[temp['Academic Year']==i]
    temp = temp[['Academic Year','Institute', 'Percentage of unplaced']]
    temp.columns = ['Academic Year','Institute', 'Percentage of unplaced']
    highest = highest.append(temp.nlargest(1,'Percentage of unplaced'))
    lowest = lowest.append(temp.nsmallest(1,'Percentage of unplaced'))
highest.reset_index(drop=True,inplace=True)
lowest.reset_index(drop=True, inplace=True)


plt.style.use('seaborn-whitegrid') 
ans = pd.DataFrame()
ans = ans.append(highest)
# ans.sort_values(['Academic Year','% Students going for higher studies'],axis=0,inplace=True)
plt.barh((ans['Academic Year']+':'+ans['Institute']).to_list(), ans['Percentage of unplaced'].to_list(),height=0.5)
def addlabels(x,y):
    for i in range(len(x)):
        plt.text( y[i]+0.7,i, y[i],ha='center',fontsize=13)
x =  (ans['Academic Year']+':'+ans['Institute']).to_list()
y = ans['Percentage of unplaced'].to_list()
addlabels(x, y)
plt.xlim([90,102])
plt.ylabel('Yearwise Institute', fontweight ='bold')
plt.xlabel('Percentage of students', fontweight ='bold', fontsize = 10)
plt.title('Yearwise Highest Percenatge of unplaced students')
# plt.show()

lowest

final.to_csv('./Outputs/unplaced.csv',index=False)
