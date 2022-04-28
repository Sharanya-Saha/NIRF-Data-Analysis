import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore")

actual_intake_df = pd.read_csv('Datasets/Total_Strength_three_years.csv')
actual_intake_df


# In[49]:


actual_intake_df['Total_Strength_All_Years'] = actual_intake_df['Total Strength_2021'] + actual_intake_df['Total Strength_2020'] +  actual_intake_df['Total Strength_2019']
actual_intake_df


# In[50]:


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

df2['Total_Earnings'] = df2['2017-18'] + df2['2018-19'] + df2['2019-20']

df2['Strength_2020'] = np.nan
df2['Strength_2019'] = np.nan
df2['Strength_2018'] = np.nan
df2['Strength_Total'] = np.nan


# In[51]:


for i in df2.index:
    try:
        tempdf = actual_intake_df[actual_intake_df['Institute']==df2.iloc[i]['Institute']]
        df2.iloc[i,5] = tempdf.iloc[0]['Total Strength_2021']
        df2.iloc[i,6] = tempdf.iloc[0]['Total Strength_2020']
        df2.iloc[i,7] = tempdf.iloc[0]['Total Strength_2019']
        df2.iloc[i,8] = tempdf.iloc[0]['Total_Strength_All_Years']
    except:
        pass
        # print(df2.iloc[i]['Institute'])
df2


# In[53]:


df3 = df2.dropna()
df3


# In[54]:


df3.reset_index(drop=True,inplace=True)
df3


# In[55]:


df3['2020_Ratio'] = df3['2019-20'] / df3['Strength_2020']
df3['2019_Ratio'] = df3['2018-19'] / df3['Strength_2019']
df3['2018_Ratio'] = df3['2017-18'] / df3['Strength_2018']
df3['Total_Ratio'] = df3['Total_Earnings'] / df3['Strength_Total']
df3


# In[56]:


df4 = df3.drop(['2019-20','2018-19','2017-18','Total_Earnings','Strength_2020','Strength_2019','Strength_2018','Strength_Total'],axis=1)
df4


# In[57]:


res_2018 = df4.sort_values(by=['2018_Ratio'],ascending=False)
res_2018
res_2018[['Institute','2018_Ratio']].to_csv('Outputs/EDP to Strength ratio 2018.csv',index=False)


# In[58]:


fig, ax = plt.subplots(figsize =(10, 7))
ax.plot(['2018','2019','2020'],res_2018.iloc[0,[3,2,1]])
plt.title(res_2018.iloc[0,0])
plt.xlabel('Years')
plt.ylabel('EDP Earning to Student Strength Ratio')
# plt.show()



# In[59]:


fig, ax = plt.subplots(figsize =(10, 7))
ax.plot(['2018','2019','2020'],res_2018.iloc[1,[3,2,1]])
plt.title(res_2018.iloc[1,0])
plt.xlabel('Years')
plt.ylabel('EDP Earning to Student Strength Ratio')
# plt.show()



# In[60]:


fig, ax = plt.subplots(figsize =(10, 7))
ax.plot(['2018','2019','2020'],res_2018.iloc[2,[3,2,1]])
plt.title(res_2018.iloc[2,0])
plt.xlabel('Years')
plt.ylabel('EDP Earning to Student Strength Ratio')
# plt.show()



# In[61]:


res_2019 = df4.sort_values(by=['2019_Ratio'],ascending=False)
res_2019
res_2019[['Institute','2019_Ratio']].to_csv('Outputs/EDP to Strength ratio 2019.csv',index=False)


# In[62]:


fig, ax = plt.subplots(figsize =(10, 7))
ax.plot(['2018','2019','2020'],res_2019.iloc[0,[3,2,1]])
plt.title(res_2019.iloc[0,0])
plt.xlabel('Years')
plt.ylabel('EDP Earning to Student Strength Ratio')
# plt.show()



# In[63]:


fig, ax = plt.subplots(figsize =(10, 7))
ax.plot(['2018','2019','2020'],res_2019.iloc[1,[3,2,1]])
plt.title(res_2019.iloc[1,0])
plt.xlabel('Years')
plt.ylabel('EDP Earning to Student Strength Ratio')
# plt.show()


# In[64]:


fig, ax = plt.subplots(figsize =(10, 7))
ax.plot(['2018','2019','2020'],res_2019.iloc[2,[3,2,1]])
plt.title(res_2019.iloc[2,0])
plt.xlabel('Years')
plt.ylabel('EDP Earning to Student Strength Ratio')
# plt.show()


# In[65]:


res_2020 = df4.sort_values(by=['2020_Ratio'],ascending=False)
res_2020
res_2020[['Institute','2020_Ratio']].to_csv('Outputs/EDP to Strength ratio 2020.csv',index=False)


# In[66]:


fig, ax = plt.subplots(figsize =(10, 7))
ax.plot(['2018','2019','2020'],res_2020.iloc[0,[3,2,1]])
plt.title(res_2020.iloc[0,0])
plt.xlabel('Years')
plt.ylabel('EDP Earning to Student Strength Ratio')
# plt.show()


# In[67]:


fig, ax = plt.subplots(figsize =(10, 7))
plt.plot(['2018','2019','2020'],res_2020.iloc[1,[3,2,1]])
plt.title(res_2020.iloc[1,0])
plt.xlabel('Years')
plt.ylabel('EDP Earning to Student Strength Ratio')
# plt.show()


# In[68]:


fig, ax = plt.subplots(figsize =(10, 7))
plt.plot(['2018','2019','2020'],res_2020.iloc[2,[3,2,1]])
plt.title(res_2020.iloc[2,0])
plt.xlabel('Years')
plt.ylabel('EDP Earning to Student Strength Ratio')
# plt.show()


# In[69]:


res_Total = df4.sort_values(by=['Total_Ratio'],ascending=False)
res_Total
res_Total[['Institute','Total_Ratio']].to_csv('Outputs/EDP to Strength ratio Total.csv',index=False)
