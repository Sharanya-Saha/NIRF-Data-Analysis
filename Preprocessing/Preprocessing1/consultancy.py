#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 11:50:46 2021

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
    df1=abc[-3].df
    df1.columns=df1.loc[0]
    df1=df1[1:]        
    f,_=filename[file].split('.')
    df1.insert(0, "Institute",code_institute[f], True)
    data.append(df1)

table=data[0].copy() 
manual=[] 
for i in range(1,100) :
    dim=data[i].shape
    if dim[0] == 4 :
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
        df1=abc[-3].df
        df2=abc[-4].df
        df1.insert(0, "Institute",code_institute[f], True)
        df2.insert(0, "Institute",code_institute[f], True)
        d1.append(df1)
        d2.append(df2)

left=[]
for i in range(20) :
    print(i)
    dim=d1[i].shape
    if i in [5,7,8,11,13,14,15,17,18] :
        df1=d2[i]
        df1.columns=table.columns
        df1=df1[1:]
        table= pd.concat([table, df1], axis=0)
        
    elif dim[0]==4 :
        print('hello')
        df1=d1[i]
        df1.columns=table.columns
        if i !=10 :
            df1=df1[1:]
        table= pd.concat([table, df1], axis=0)
        
    else :
        left.append(i)
        df1=d1[i]
        df1.columns=table.columns
        table= pd.concat([table, df1], axis=0)
        


left_ins=['Sri Venkateswara University ','Osmania University ','Siksha `O` Anusandhan ','Banaras Hindu University ','Amrita Vishwa Vidyapeetham ']
temp={'Institute':left_ins,'Financial Year':['Total no. of Consultancy Projects']*5,'2019-20':['434','182','59','2','142'],'2018-19':['629','217','41','2','8351'],'2017-18':['678','162','25','2','7639']} 
temp_pd=pd.DataFrame(temp)  
table= pd.concat([table,temp_pd],axis=0) 
table=table[table['Financial Year']!='Amount Received in Words']
table.to_csv('Outputs/cosultancy.csv',index=False)