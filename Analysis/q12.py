# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 02:12:28 2021

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
x1['Percentage going for higher studies'] = (x1['No. of students\nselected for Higher\nStudies']/x1['No. of students\ngraduating in\nminimum stipulated\ntime'])*100
x1
df1


df2 = pd.read_csv('./Datasets/placement2020.csv')
x2 =df2.copy()
x2 = x2[[ 'Institute', 'Program_name', 'Academic Year.2',
       'No. of students\ngraduating in\nminimum stipulated\ntime',
       'No. of students\nplaced',
       'No. of students\nselected for Higher\nStudies']]
x2['Percentage going for higher studies'] = (x2['No. of students\nselected for Higher\nStudies']/x2['No. of students\ngraduating in\nminimum stipulated\ntime'])*100
x2

df3 = pd.read_csv('./Datasets/placement2019.csv')
x3 =df3.copy()
x3 = x3[[ 'Institute', 'Program_name', 'Academic Year.2',
       'No. of students\ngraduating in\nminimum stipulated\ntime',
       'No. of students\nplaced',
       'No. of students\nselected for Higher\nStudies']]
x3['Percentage going for higher studies'] = (x3['No. of students\nselected for Higher\nStudies']/x3['No. of students\ngraduating in\nminimum stipulated\ntime'])*100
x3


x = pd.concat([x1,x2,x3],axis=0)
# x.sort_values('Institute',ascending=False,inplace=True)
x.reset_index(drop=True, inplace=True)
x['Institute'] = x['Institute'].apply(lambda x: x.strip())
x['Program_name'] = x['Program_name'].apply(lambda x: x.strip())
x.drop_duplicates(keep='first',inplace=True)
x.reset_index(drop=True, inplace=True)
x.head(10)

y = x.copy()
y = y.groupby(['Institute','Academic Year.2']).agg('sum')
y['Academic Year.2'] = y.index.to_numpy()
y['Academic Year.2'] = y['Academic Year.2'].apply(lambda x: x[1])
y['Institute'] = y.index.to_numpy()
y['Institute'] = y['Institute'].apply(lambda x: x[0])
y.reset_index(drop=True, inplace=True)
y['Percentage going for higher studies'] = (y['No. of students\nselected for Higher\nStudies']/y['No. of students\ngraduating in\nminimum stipulated\ntime'])*100
y.fillna(0,inplace=True)
y
final = y.copy()
final

highest =pd.DataFrame()
lowest = pd.DataFrame()

for i in y['Academic Year.2'].unique():
    temp = y.copy().reset_index(drop=True)
    temp = temp[temp['Academic Year.2']==i]
    temp = temp[['Academic Year.2','Institute', 'Percentage going for higher studies']]
    temp.columns = ['Academic Year','Institute', '% Students going for higher studies']
    highest = highest.append(temp.nlargest(1,'% Students going for higher studies'))
    lowest = lowest.append(temp.nsmallest(1,'% Students going for higher studies'))
highest.reset_index(drop=True,inplace=True)
lowest.reset_index(drop=True, inplace=True)

plt.style.use('seaborn-whitegrid') 
ans = pd.DataFrame()
ans = ans.append(highest)
ans.sort_values(['Academic Year','% Students going for higher studies'],axis=0,inplace=True)
plt.barh((ans['Academic Year']+':'+ans['Institute']).to_list(), ans['% Students going for higher studies'],height=0.5)

def addlabels(x,y):
    for i in range(len(x)):
        plt.text( y[i]+4,i, y[i],ha='center',fontsize=13)
x =  (ans['Academic Year']+':'+ans['Institute']).to_list()
y = round(ans['% Students going for higher studies'],1).to_list()
addlabels(x, y)
plt.xlim([0,110])
plt.ylabel('Institute', fontweight ='bold')
plt.xlabel('Percentage of students', fontweight ='bold', fontsize = 10)
plt.title('Yearwise Best Institute in terms of students going for higher education')
# plt.show()

lowest

final = final[['Institute','Academic Year.2','Percentage going for higher studies']]
final.columns = ['Institute','Academic Year','Percentage of students going for higher studies']
final.to_csv('./Outputs/higher_studies.csv',index=False)
final
