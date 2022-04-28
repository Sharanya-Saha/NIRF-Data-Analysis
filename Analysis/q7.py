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



no_movement = df[df['Provisions for movement from one building to another']!='Yes']
# no_movement




no_movement = no_movement[['Institute']]
# no_movement
no_movement.to_csv('Outputs/Movement Facilities.csv',index=False)




percentages = ['Yes','No']
data = [100-len(no_movement),len(no_movement)]





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


plt.title('Chart Showing percentage of colleges with Facility of movement for Physically abled People')
# plt.show()

