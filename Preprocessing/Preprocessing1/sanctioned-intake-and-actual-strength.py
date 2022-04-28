#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 09:00:46 2021

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

data1=[]
data2=[]
for file in filename.keys() :
    abc=camelot.read_pdf(file,pages="all")
    print(abc)
    df1=abc[0].df
    df1.columns=df1.loc[0]
    df1=df1[1:]
    df2=abc[1].df
    df2.columns=df2.loc[0]
    df2=df2[1:]
    f,_=filename[file].split('.')
    df1.insert(0, "Institute",code_institute[f], True)
    df2.insert(0,'Institute',code_institute[f],True)
    data1.append(df1)
    data2.append(df2)

    

table1=data1[0].copy()  

for i in range(1,100) :
    dim=data1[i].shape
    if dim[1] == 8 :
       table1= pd.concat([table1, data1[i]], axis=0)
table1.to_csv('Outputs/sanctioned-intake.csv',index=False)

table2=data2[0].copy()  
for i in range(1,100) :
    dim=data2[i].shape
    if dim[1] == 14 :
       table2= pd.concat([table2, data2[i]], axis=0)
       
table2.columns=['Institute','Programs','No. of Male Students','No. of Female Students','Total Students','Within State(Including male& female)','Outside State(Including male& female)','Outside Country(Including male& female)','EconomicallyBackward(Including male & female)','SociallyChallenged (SC+ST+OBC Including male & female)','No. of studentsreceiving full tuition fee reimbursement from the State and Central Government','No. of students receiving full tuition fee reimbursement from Institution Funds','No. of students receiving full tuition fee reimbursement from the Private Bodies','No. of students who are not receiving full tuition fee reimbursement']
table2.to_csv('Outputs/total-actual-strength.csv',index=False)