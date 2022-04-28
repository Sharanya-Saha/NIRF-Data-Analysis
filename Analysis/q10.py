
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/executive-development-program.csv')
df


# In[34]:


df['Financial Year'].unique()


# In[35]:


df2 = df[df['Financial Year']=='Total Annual Earnings (Amount in Rupees)(Excluding Lodging\n& Boarding Charges)']
df2


# In[36]:


df2.reset_index(drop=True,inplace=True)
df2


# In[37]:


df2 = df2.drop(['Financial Year'],axis=1)
df2


# In[38]:


df2['2017-18'] = pd.to_numeric(df2['2017-18'])
df2['2018-19'] = pd.to_numeric(df2['2018-19'])
df2['2019-20'] = pd.to_numeric(df2['2019-20'])
df2


# In[39]:


# For 2017-18
df3 = df2.sort_values(by=['2017-18'],ascending=False)
df3

df3.reset_index(drop=True,inplace=True)
df3
df3[['Institute','2017-18']].to_csv('Outputs/2017-18 EDP Earnings.csv',index=False)


# In[40]:




percentages = list(df3.iloc[:5,0]) + ['Others']
data = [df3.iloc[0,1],df3.iloc[1,1],df3.iloc[2,1],df3.iloc[3,1],df3.iloc[4,1],
        df3.iloc[:,1].sum()-(df3.iloc[0,1]+df3.iloc[1,1]+df3.iloc[2,1]+df3.iloc[3,1]+df3.iloc[4,1])]



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


plt.title('Chart Showing percentage of Earnings of Insitutes from Executive Programs in session 2017-18')
# show plot
# plt.show()


# In[41]:


# For 2018-19
df3 = df2.sort_values(by=['2018-19'],ascending=False)
df3

df3.reset_index(drop=True,inplace=True)
df3

df3[['Institute','2018-19']].to_csv('Outputs/2018-19 EDP Earnings.csv',index=False)


# In[42]:




percentages = list(df3.iloc[:5,0]) + ['Others']
data = [df3.iloc[0,1],df3.iloc[1,1],df3.iloc[2,1],df3.iloc[3,1],df3.iloc[4,1],
        df3.iloc[:,1].sum()-(df3.iloc[0,1]+df3.iloc[1,1]+df3.iloc[2,1]+df3.iloc[3,1]+df3.iloc[4,1])]




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

plt.title('Chart Showing percentage of Earnings of Insitutes from Executive Programs in session 2018-19')
# show plot
# plt.show()


# In[43]:


# For 2019-20
df3 = df2.sort_values(by=['2019-20'],ascending=False)
df3

df3.reset_index(drop=True,inplace=True)
df3

df3[['Institute','2019-20']].to_csv('Outputs/2019-20 EDP Earnings.csv',index=False)


# In[44]:



percentages = list(df3.iloc[:5,0]) + ['Others']
data = [df3.iloc[0,1],df3.iloc[1,1],df3.iloc[2,1],df3.iloc[3,1],df3.iloc[4,1],
        df3.iloc[:,1].sum()-(df3.iloc[0,1]+df3.iloc[1,1]+df3.iloc[2,1]+df3.iloc[3,1]+df3.iloc[4,1])]



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

plt.title('Chart Showing percentage of Earnings of Insitutes from Executive Programs in session 2019-20')
# show plot
# plt.show()


# In[45]:


# For all years
df2['Total_Earnings'] = df2['2017-18'] + df2['2018-19'] + df2['2019-20']
df2
df3 = df2.sort_values(by=['Total_Earnings'],ascending=False)
df3

df3[['Institute','Total_Earnings']].to_csv('Outputs/Total EDP Earnings.csv',index=False)



df3 = df3.drop(['2019-20','2018-19','2017-18'],axis=1)
df3

df3.reset_index(drop=True,inplace=True)
df3


percentages = list(df3.iloc[:5,0]) + ['Others']
data = [df3.iloc[0,1],df3.iloc[1,1],df3.iloc[2,1],df3.iloc[3,1],df3.iloc[4,1],
        df3.iloc[:,1].sum()-(df3.iloc[0,1]+df3.iloc[1,1]+df3.iloc[2,1]+df3.iloc[3,1]+df3.iloc[4,1])]



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

plt.title('Chart Showing percentage of Earnings of Insitutes from Executive Programs')
# show plot
# plt.show()

