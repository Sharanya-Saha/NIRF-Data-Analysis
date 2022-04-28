#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 21:01:09 2021

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


ins_2021=[]
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
    ins_2021.append(name)

filename={}
csvs = os.listdir("2019/")
for x in csvs :
        filename[f"2019/{x}"]=x
code_institute_19={}
ins_2019=[]
#file='IR-O-N-10.pdf'
for file in filename.keys() :
    # print(file)
    pdf_file = open(file, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    #print(page_content.encode('utf-8'))
    text=page_content.split(" ")
    
    name=''
    for i in range(15) :
        # print(i)
        try : 
            if text[15+i][0] == '[' :
                code=text[15+i].split(']')
                _,institute_code=code[0].split('[')
                # print(institute_code)
                break
            name=name+text[15+i]+' '
        except :
            pass
    # print(name)
    code_institute_19[institute_code]=name
    ins_2019.append(name)
    
filename={}
csvs = os.listdir("2020/")
for x in csvs :
        filename[f"2020/{x}"]=x
code_institute_20={}
ins_2020=[]
#file='IR-O-N-10.pdf'
for file in filename.keys() :
    # print(file)
    pdf_file = open(file, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    #print(page_content.encode('utf-8'))
    text=page_content.split(" ")
    
    name=''
    for i in range(15) :
        # print(i)
        try : 
            if text[15+i][0] == '[' :
                code=text[15+i].split(']')
                _,institute_code=code[0].split('[')
                # print(institute_code)
                break
            name=name+text[15+i]+' '
        except :
            pass
    # print(name)
    code_institute_20[institute_code]=name
    ins_2020.append(name)
    
names=pd.read_csv('name_changes_2020-2021.csv',header=None)  
names.columns=['2020','2021']  
keys=list(names['2020'])
for i in range(len(keys)) :
    keys[i]=str(keys[i]+' ')
spell_rename=dict(zip(keys,list(names['2021'])))

for s in spell_rename.keys() :
    spell_rename[s]=str(spell_rename[s]+' '*1)
    

for i in range(len(ins_2020)) :
    if ins_2020[i] in spell_rename.keys() :
        # print(ins_2020[i])
        ins_2020[i]=str(spell_rename[ins_2020[i]])
        # print(ins_2020[i])
        
        
        
        
        
        
names=pd.read_csv('name_changes_2019_2021.csv',header=None)  
names.columns=['2019','2021']  
keys=list(names['2019'])
for i in range(len(keys)) :
    keys[i]=str(keys[i]+' ')
spell_rename=dict(zip(keys,list(names['2021'])))

for s in spell_rename.keys() :
    spell_rename[s]=str(spell_rename[s]+' '*1)
    

for i in range(len(ins_2019)) :
    if ins_2019[i] in spell_rename.keys() :
        # print(ins_2019[i])
        ins_2019[i]=str(spell_rename[ins_2019[i]])
        # print(ins_2019[i])


common1=list(set(ins_2021)-set(ins_2020))
inters=list(set(ins_2021)-set(common1))
icommon=list(set(inters)-set(ins_2019))
final_list=list(set(inters)-set(icommon))
tp={'Insititute':final_list}
tp_pd=pd.DataFrame(tp)
tp_pd.to_csv('Outputs/Consistent_Institutes.csv',index=False)

mn=list(set(ins_2021)-set(final_list))
mp={'Insititute':mn}
mp_pd=pd.DataFrame(mp)
mp_pd.to_csv('Outputs/Inconsistent_Institutes.csv',index=False)
