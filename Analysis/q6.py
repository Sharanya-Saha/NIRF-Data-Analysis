#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


df = pd.read_csv('Datasets/pcs.csv')
# df


# In[3]:


def func(x):
    x_split = x.split('%')
    value = x_split[0][-2:]
    if 'more than' in x_split[0]:
        return '>'+value
    elif 'less than' in x_split[0]:
        return '<'+value


# In[4]:


df["Ramps%"] = df['Lifts/Ramps'].apply(func)
df["Toilets%"] = df['Special Toilets'].apply(func)



ramps_less_80 = df[df['Ramps%']!='>80']
# ramps_less_80



ramps_less_80 = ramps_less_80[['Institute','Ramps%']]
# ramps_less_80
ramps_less_80.to_csv('Outputs/Lift Facilities.csv',index=False)


percentages = ['>=80','<80']
data = [100-len(ramps_less_80),len(ramps_less_80)]



def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%".format(pct)
  
# Creating plot
fig, ax = plt.subplots(figsize =(10, 7))
_, _, autotexts = ax.pie(data, 
                                  autopct = lambda pct: func(pct, data),
                                  labels = percentages,
                                  textprops = dict(color ="black"))
  
  
plt.setp(autotexts, size = 8, weight ="bold")

plt.title('Chart Showing percentage of colleges with Lift/Ramp Facilities')
# show plot
# plt.show()
