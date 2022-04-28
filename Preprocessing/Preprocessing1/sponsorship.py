#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 18:53:48 2021

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
    df1=abc[-4].df
    df1.columns=df1.loc[0]
    df1=df1[1:]        
    f,_=filename[file].split('.')
    df1.insert(0, "Institute",code_institute[f], True)
    data.append(df1)
    
table=data[0].copy() 
manual=[] 
for i in range(1,100) :
    dim=data[i].shape
    
    if dim[0] == 4 and data[i].iloc[0,1]=='Total no. of Sponsored Projects':
       table= pd.concat([table, data[i]], axis=0)
    else :
        manual.append(i)
        
manual_ins=[]
for x in manual :
    dfx=data[x]
    manual_ins.append(list(dfx['Institute'].values))
    
f_list=[]
for ls in manual_ins :
    f_list.append(ls[0])

def isf(f) :
    for x in f_list :
        if f == x :
            return 1
    return 0
            
d1=[]
d2=[]
for file in filename.keys() :
    f,_=filename[file].split('.')
    if isf(code_institute[f]) :
        print(1)
        abc=camelot.read_pdf(file,pages="all")
        df1=abc[-4].df
        df2=abc[-5].df
        df1.insert(0, "Institute",code_institute[f], True)
        df2.insert(0, "Institute",code_institute[f], True)
        d1.append(df1)
        d2.append(df2)
        
left=[]
for i in range(32) :
    dim1=d1[i].shape
    dim2=d2[i].shape
    if ((i == 21) or (i==1) or (i==7)) :
        df1=d1[i]
        df1.columns=table.columns
        table= pd.concat([table, df1], axis=0)
    elif dim2[0]==5 :
        df1=d2[i]
        df1.columns=table.columns
        df1=df1[1:] 
        table= pd.concat([table, df1], axis=0)
    elif dim1[0]==4:
        df1=d1[i]
        if df1.iloc[0,1]=='Total no. of Sponsored Projects' :
            df1.columns=table.columns
            df1=df1[1:] 
            table= pd.concat([table, df1], axis=0)
        else :
           df1.columns=table.columns
           df1=df1[1:] 
           print(i)
           table= pd.concat([table, df1], axis=0)
    elif dim1[0]+dim2[0]==5 :
        df1=d2[i]
        df2=d1[i]
        df1=df1[1:]
        df1.columns=table.columns
        df2.columns=table.columns
        table= pd.concat([table, df2], axis=0)  
        table= pd.concat([table, df1], axis=0)
    elif i!= 20 :
        df1=d1[i]
        df1.columns=table.columns
        table= pd.concat([table, df1], axis=0)
    else :
        df1=d1[i]
        df1.columns=table.columns   
        df1=df1[1:]
        table= pd.concat([table, df1], axis=0)
       
left_ins=['National Institute of Technology Silchar ','Savitribai Phule Pune University ','Dr. B. R. Ambedkar National Institute of Technology ']  
temp={'Institute':left_ins,'Financial Year':['Total no. of Sponsored Projects']*3,'2019-20':['33','150','37'],'2018-19':['23','101','22'],'2017-18':['13','92','9']}      
temp_pd=pd.DataFrame(temp)  
table= pd.concat([table,temp_pd],axis=0)       
t1={'Institute':['Saveetha Institute of Medical and Technical Sciences '],'Financial Year':['Total Amount Received (Amount in Rupees)'],'2019-20':['11132000'],'2018-19':['26438000'],'2017-18':['5740000']}  
t1_pd=pd.DataFrame(t1)  
table= pd.concat([table,t1_pd],axis=0)        
table=table[table['Financial Year']!='Amount Received in Words']      
table.to_csv('Outputs/sponsorship.csv',index=False)       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        