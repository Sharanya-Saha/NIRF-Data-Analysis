
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


faculty_df = pd.read_csv('Datasets/number-of-faculties.csv')
faculty_df


# In[16]:


actual_intake_df = pd.read_csv('Datasets/total-actual-strength.csv')
actual_intake_df


# In[17]:


actual_intake_df1 = actual_intake_df[['Institute','Total Students']]
actual_intake_df1


# In[18]:


actual_intake_df2 = actual_intake_df1.groupby(['Institute']).sum()
actual_intake_df2.reset_index(inplace=True)
actual_intake_df2


# In[19]:


set(faculty_df['Institute']) - set(actual_intake_df2['Institute'])


# In[20]:


# faculty_df


# In[21]:


faculty_df['Actual_Strength'] = np.nan


# In[23]:


for i in faculty_df.index:
    tempdf = actual_intake_df2[actual_intake_df2['Institute']==faculty_df.iloc[i]['Institute']]
    if len(tempdf)>0:
        val = tempdf.iloc[0]['Total Students']
    else:
        val = np.nan
    faculty_df.iloc[i,2] = val
faculty_df


# In[24]:


faculty_df['Student_to_Faculty'] = faculty_df['Actual_Strength'] / faculty_df['Number of Faculties']
faculty_df


# In[25]:


student_to_faculty_ratio = faculty_df.sort_values(by=['Student_to_Faculty'] ,na_position='last')
student_to_faculty_ratio


# In[26]:


top_5_ratio = student_to_faculty_ratio.iloc[0:5]
# top_5_ratio
top_5_ratio[['Institute','Student_to_Faculty']].to_csv('Outputs/Top 5 student to faculty ratio.csv',index=False)


# In[27]:


student_to_faculty_ratio[student_to_faculty_ratio['Actual_Strength']!=np.nan].iloc[-5:]


# In[28]:


student_to_faculty_ratio2 = student_to_faculty_ratio.dropna()
# student_to_faculty_ratio2


# In[29]:


worst_5_ratio = student_to_faculty_ratio2.iloc[-5:]
# worst_5_ratio
worst_5_ratio[['Institute','Student_to_Faculty']].to_csv('Outputs/Worst 5 student to faculty ratio.csv',index=False)


# In[30]:


top_3_ratio = student_to_faculty_ratio.iloc[0:3]
worst_3_ratio = student_to_faculty_ratio2.iloc[-3:]


# In[31]:


college_list = list(top_3_ratio['Institute'])+list(worst_3_ratio['Institute'])
ratio_list = list(top_3_ratio['Student_to_Faculty'])+list(worst_3_ratio['Student_to_Faculty'])


# In[32]:


fig, ax = plt.subplots(figsize =(20, 7))
ax.plot(college_list,ratio_list)
plt.xlabel('Colleges')
plt.ylabel('Student to Faculty Ratio')
plt.title('Graph showing best 3 and worst 3 colleges in terms of student to faculty ratio')
# plt.show()
