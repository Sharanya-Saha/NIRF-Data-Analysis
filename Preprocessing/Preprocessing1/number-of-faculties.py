#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 10:27:31 2021

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
        
faculties=[]
for file in filename.keys() :
    pdf_file = open(file, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    page = read_pdf.getPage(-1)
    page_content = page.extractText()
    #print(page_content.encode('utf-8'))
    if page_content[-4].isalpha() :
        fac=page_content[-3:]
    else :
        fac=page_content[-4:]
    f,_=filename[file].split('.')
    faculties.append([code_institute[f],fac])
    
faculty=pd.DataFrame(faculties,columns=['Institute','Number of Faculties'])
faculty.to_csv('Outputs/number-of-faculties.csv',index=False)