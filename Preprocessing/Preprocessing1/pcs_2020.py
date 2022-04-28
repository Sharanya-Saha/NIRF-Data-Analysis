#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 21:41:06 2021

@author: sharanya
"""
import camelot
import os 
import PyPDF2
import pandas as pd

filename={}
code_institute={}
csvs = os.listdir("2021/")
for x in csvs :
        filename[f"2021/{x}"]=x
        
for file in filename.keys() :
    pdf_file = open(file, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    #print(page_content.encode('utf-8'))
    text=page_content.split(" ")
    
    name=''
    for i in range(15) :
        if text[16+i][0] == '[' :
            code=text[16+i].split(']')
            _,institute_code=code[0].split('[')
            #print(institute_code)
            break
        name=name+text[16+i]+' '
    #print(name)
    code_institute[institute_code]=name  
    
data=[]
for file in filename.keys() :
    abc=camelot.read_pdf(file,pages="all")
    print(abc)
    df1=abc[-1].df
    df1.columns=['Question','Answer']
    #df1=df1[1:]
    #rows=df1.shape[0]
    f,_=filename[file].split('.')
    df1.insert(0, "Institute",code_institute[f], True)
    data.append(df1)


table1=data[0].copy()  

for i in range(1,100) :
    print(i,data[i].Institute)
    table1= pd.concat([table1, data[i]], axis=0)    


df_Q1=table1.loc[table1['Question']=='1. Do your institution buildings have Lifts/Ramps?'].reset_index()
df_Q3=table1.loc[table1['Question']=='3. Do your institution buildings have specially designed toilets for handicapped students?'].reset_index()
df_Q2=table1.loc[table1['Question']!='1. Do your institution buildings have Lifts/Ramps?']
df_Q2=df_Q2.loc[df_Q2['Question']!='3. Do your institution buildings have specially designed toilets for handicapped students?'].reset_index()

df_Q2.rename(columns = {'Answer':'Provisions for movement from one building to another'}, inplace = True)
df_Q1.rename(columns = {'Answer':'Lifts/Ramps'}, inplace = True)
df_Q3.rename(columns = {'Answer':'Special Toilets'}, inplace = True)
df_Q2.drop(['Question','index'],axis='columns', inplace = True)
df_Q3.drop(['Question','index'],axis='columns', inplace = True)
df_Q1.drop(['Question','index'],axis='columns', inplace = True)

institutes=list(df_Q1.Institute)
all_institutes=list(df_Q2.Institute)
q1_remaining=set(all_institutes)-set(institutes)

Q1_extra={'Institute':list(q1_remaining),'Lifts/Ramps':['Yes, more than 80% of the buildings']*3}
df_Q1extra = pd.DataFrame(Q1_extra)
df_Q1= pd.concat([df_Q1,df_Q1extra],axis=0)

institutes=list(df_Q3.Institute)
all_institutes=list(df_Q2.Institute)
q3_remaining=set(all_institutes)-set(institutes)



df_Q1.sort_values(by=['Institute'],inplace=True)
df_Q2.sort_values(by=['Institute'],inplace=True)
df_Q3.sort_values(by=['Institute'],inplace=True)

df_Q1=df_Q1.reset_index()
df_Q2=df_Q2.reset_index()
df_Q3=df_Q3.reset_index()
df_Q1.drop('index', axis='columns' , inplace=True)
df_Q2.drop('index', axis='columns' , inplace=True)
df_Q3.drop('index', axis='columns' , inplace=True)

df_Q1['Provisions for movement from one building to another']=df_Q2['Provisions for movement from one building to another']
df_Q1['Special Toilets']=df_Q3['Special Toilets']

df_Q1.to_csv('Outputs/pcs_2020.csv',index=False)