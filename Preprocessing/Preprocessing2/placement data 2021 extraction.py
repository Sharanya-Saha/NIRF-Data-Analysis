#!/usr/bin/env python
# coding: utf-8

# In[14]:


from tabula import read_pdf
from tabulate import tabulate
import camelot.io as camelot
import os
import pandas as pd
import numpy as np
import PyPDF2


# In[15]:


# Finding all file names in a folder 2021
file_names = []
for i in os.listdir('2021'):
    # print(i)
    if(i!='failed colleges'):
        file_names.append(i)
file_names


# In[16]:


## Dataframe containing placement data of all colleges
final = pd.DataFrame()
failed_colleges = [] #whose placement data has different shape than others


# In[5]:


k = 0
for file in file_names:
    abc = camelot.read_pdf('2021/'+file, pages="all",flavor='lattice',line_scale=30) # file loation
    # line_space = 30 , this argument helps to read single row tables also. greater the value, higher the chances of detecting smaller tables.
    pdf_file = open('2021/'+file, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    text=page_content.split(" ")
        
    name=''
    for i in range(15) :
        if text[16+i][0] == '[' :
            code=text[16+i].split(']')
            _,institute_code=code[0].split('[')
            #print(institute_code)
            break
        name=name+text[16+i]+' '
    print(name,k)
    k = k+1
    df = []
    i = 0
    while(i<len(abc)):
        df1 = abc[i].df
            
        if(i==len(abc)-1):
            df.append(df1)
            break
        df2 = abc[i+1].df
        # merging conditions for placement tables
        condition = df1.loc[df1.shape[0]-1][0]=='Academic Year'
        condition = condition | ((df1.loc[df1.shape[0]-1][0]=='2013-14') and (df2.loc[0][0]=='2014-15') )
        condition = condition | ((df1.loc[df1.shape[0]-1][0]=='2014-15') and (df2.loc[0][0]=='2015-16') )
        condition = condition | ((df1.loc[df1.shape[0]-1][0]=='2015-16') and (df2.loc[0][0]=='2016-17') )
        condition = condition | ((df1.loc[df1.shape[0]-1][0]=='2016-17') and (df2.loc[0][0]=='2017-18') )
        condition = condition | ((df1.loc[df1.shape[0]-1][0]=='2017-18') and (df2.loc[0][0]=='2018-19') )
        condition = condition | ((df1.loc[df1.shape[0]-1][0]=='2018-19') and (df2.loc[0][0]=='2019-20') )
        
        if (condition):
            x = pd.DataFrame(np.vstack((np.array(df1),np.array(df2))))

            df.append(x)
            i = i+2
        else:
            df.append(df1)
            i =i+1
    x = df[1].copy()
    x.columns = x.loc[0]
    x = x[1:]
    x
    p = []
    for i in range(x.shape[0]):
        programme = x.iloc[i]['(All programs\nof all years)']
        p.append(programme)

    for i in p:
        p_name = i
        j = 2
        y = df[j].copy()
        y.columns = y.loc[0]
        j = j+1
        y = y[1:]
        y['Program_name'] = p_name
        y['Institute'] = name
        try:
            final = final.append(y, ignore_index=True)
        except:
            failed_colleges.append(name+p_name)
        
        


# In[6]:


final


# In[7]:


failed_colleges


# In[8]:


final.to_csv('/Outputs/placement2021.csv', index=False)


# In[9]:


failed_colleges


# # Managing failed colleges, whose dataframe has different shape

# In[10]:


# Finding all file names in a folder
file_names = []
for i in os.listdir('2021/failed colleges'):
    # print(i)
    file_names.append(i)
file_names


# In[11]:


## Dataframe containing placement data of all colleges
final = pd.DataFrame()
failed_colleges = []


# In[12]:


k = 0
for file in file_names:
    abc = camelot.read_pdf('2021/failed colleges/'+file, pages="all",flavor='lattice',line_scale=30) # file loation
    # line_space = 30 , this argument helps to read single row tables also. greater the value, higher the chances of detecting smaller tables.
    pdf_file = open('2021/failed colleges/'+file, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    text=page_content.split(" ")
        
    name=''
    for i in range(15) :
        if text[16+i][0] == '[' :
            code=text[16+i].split(']')
            _,institute_code=code[0].split('[')
            #print(institute_code)
            break
        name=name+text[16+i]+' '
    print(name,k)
    k = k+1
    df = []
    i = 0
    while(i<len(abc)):
        df1 = abc[i].df
            
        if(i==len(abc)-1):
            df.append(df1)
            break
        df2 = abc[i+1].df
        # merging conditions for placement tables
        condition = df1.loc[df1.shape[0]-1][0]=='Academic Year'
        condition = condition | ((df1.loc[df1.shape[0]-1][0]=='2013-14') and (df2.loc[0][0]=='2014-15') )
        condition = condition | ((df1.loc[df1.shape[0]-1][0]=='2014-15') and (df2.loc[0][0]=='2015-16') )
        condition = condition | ((df1.loc[df1.shape[0]-1][0]=='2015-16') and (df2.loc[0][0]=='2016-17') )
        condition = condition | ((df1.loc[df1.shape[0]-1][0]=='2016-17') and (df2.loc[0][0]=='2017-18') )
        condition = condition | ((df1.loc[df1.shape[0]-1][0]=='2017-18') and (df2.loc[0][0]=='2018-19') )
        condition = condition | ((df1.loc[df1.shape[0]-1][0]=='2018-19') and (df2.loc[0][0]=='2019-20') )
        
        if (condition):
            x = pd.DataFrame(np.vstack((np.array(df1),np.array(df2))))

            df.append(x)
            i = i+2
        else:
            df.append(df1)
            i =i+1
    x = df[1].copy()
    x.columns = x.loc[0]
    x = x[1:]
    x
    p = []
    for i in range(x.shape[0]):
        programme = x.iloc[i]['(All programs\nof all years)']
        p.append(programme)

    for i in p:
        p_name = i
        j = 2
        y = df[j].copy()
        y.columns = y.loc[0]
        j = j+1
        y = y[1:]
        y['Program_name'] = p_name
        y['Institute'] = name
        try:
            final = final.append(y, ignore_index=True)
        except:
            failed_colleges.append(name+p_name)
        
        


# In[13]:


final.to_csv('/Outputs/placement2021_different_type_of_data.csv',index=False)


# In[ ]:




