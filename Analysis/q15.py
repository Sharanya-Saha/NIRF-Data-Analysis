# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 01:19:08 2021

@author: Utkarsh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import os

#os.chdir(r"C:\Users\Utkarsh\Desktop\IITK Sem I\Data Mining CS685\Project")

df1 = pd.read_csv(r"./Datasets/phd 2021 2020 2019.csv")
x1 =df1.copy()
x1

df = x1.copy()
df = df[(df['Ph.D (Student pursuing doctoral program till 2019-20)']=='Full Time')|(df['Ph.D (Student pursuing doctoral program till 2019-20)']=='Part Time')]
df.fillna(-1,inplace=True)
df = df[df['a']!=-1]
df['a'] = df['a'].astype('int')
df['b'] = df['b'].astype('int')
df['c'] = df['c'].astype('int')
df.columns = ['Institute','Type of PhD','2019-20','2018-19','2017-18']
df

df1 = df.copy()
df1 = df1[df1['Type of PhD']=='Full Time']
df1['Average No. of Full Time phd students'] = round(((df1['2019-20']+df1['2018-19']+df1['2017-18'])/3),0).astype('int')
df1.reset_index(drop=True, inplace=True)
df1 = df1[['Institute','Average No. of Full Time phd students']]
df1

df2 = df.copy()
df2 = df2[df2['Type of PhD']=='Part Time']
df2['Average No. of Part Time phd students'] = round(((df2['2019-20']+df2['2018-19']+df2['2017-18'])/3),0).astype('int')
df2.reset_index(drop=True, inplace=True)
df2 = df2[['Institute','Average No. of Part Time phd students']]
df2

final = pd.concat([df1,df2],axis=1)
final = final.loc[:,~final.columns.duplicated()]
final

final.to_csv('./Outputs/phd.csv',index=False)

ans = final.nlargest(5,'Average No. of Full Time phd students')
plt.style.use('seaborn-whitegrid')
plt.barh(ans['Institute'].to_list(), ans['Average No. of Full Time phd students'].to_list(),height=0.6)
def addlabels(x,y):
    for i in range(len(x)):
        plt.text( y[i]+30,i, y[i],ha='center',fontsize=11)
x =  (ans['Institute']).to_list()
y = round(ans['Average No. of Full Time phd students'],0).to_list()
addlabels(x, y)
plt.xlim([0,1000])
plt.ylabel('Institute', fontweight ='bold')
plt.xlabel('Number of students', fontweight ='bold', fontsize = 10)
plt.title('Top colleges having highest number of PhD students (Full Time)')
# plt.show()

ans = final.nlargest(5,'Average No. of Part Time phd students')
plt.style.use('seaborn-whitegrid')
plt.barh(ans['Institute'].to_list(), ans['Average No. of Part Time phd students'].to_list(),height=0.6)
def addlabels(x,y):
    for i in range(len(x)):
        plt.text( y[i]+10,i, y[i],ha='center',fontsize=11)
x =  (ans['Institute']).to_list()
y = round(ans['Average No. of Part Time phd students'],0).to_list()
addlabels(x, y)
plt.xlim([0,400])
plt.ylabel('Institute', fontweight ='bold')
plt.xlabel('Number of students', fontweight ='bold', fontsize = 10)
plt.title('Top colleges having highest number of PhD students (Part Time)')
# plt.grid()
# plt.show()
