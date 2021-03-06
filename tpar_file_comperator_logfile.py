# -*- coding: utf-8 -*-
"""Tpar_File_comperator_logfile.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uidPu7QrD4yPUITAaiPxXKyc8tQYfGGw
"""

import json
import pandas as pd

from datetime import datetime 
import pytz 

with open('/content/Automation.json') as f:
  data = json.load(f)

source_file=data[0]['source_file']

source=[]
target=[]

source_name= source_file.split("/")[-1].split('.')[0]

IST = pytz.timezone('Asia/Kolkata') 

log_file=source_name + " log_file " + str(datetime.now(IST)).split(".")[0] + ".txt"  

file100 = open(log_file,"a")

for targets in data[0]['target_file']:
  target_files=targets

  target_name = target_files.split("/")[-1].split('.')[0]



  file=open(source_file,"r")
  target_file=open(target_files,"r")

  lines=file.readlines()
  target_line=target_file.readlines()

  variables=[]
  target_variables=[]

  for line in lines:
    if line[0] == '$':
      variables.append(line[:-1])


  for line in target_line:
    if line[0] == '$':
      target_variables.append(line[:-1])


  variables.sort()
  target_variables.sort()

  if len(target_variables) != len(variables):
    target_keyword=[]
    source_keyword=[]
    for i in variables:
      source_keyword.append(i.split("=")[0])
    for j in target_variables:
      target_keyword.append(j.split("=")[0])
    for i in source_keyword:
      if i not in target_keyword:
        file100.write(i + " not present in target file: " + target_name + "\n")
    for j in target_keyword:
      if j not in source_keyword:
        file100.write(j + " not present in source file which is present in target file: " + target_name + "\n")
    
    file100.write("Unequal Number of Variable for target file name: " + target_name + "\n")
    continue
  
  z=0 

  for i in range(0,len(variables)):
    if target_variables[i].split("=")[0] != variables[i].split("=")[0]:
      target_keyword=[]
      source_keyword=[]
      for i in variables:
        source_keyword.append(i.split("=")[0])
      for j in target_variables:
        target_keyword.append(j.split("=")[0])
      for i in source_keyword:
        if i not in target_keyword:
          file100.write(i + " not present in target file: " + target_name + "\n")
      for j in target_keyword:
        if j not in source_keyword:
          file100.write(j + " not present in source file which is present in target file: " + target_name + "\n")

      file100.write("No of variables is same but variables are differnt from source file in text file name: " + target_name + "\n")
      z+=1
      break


  if z!=0:
    continue

  source.append(source_name)
  target.append(target_name)
  
  
  for i in range(0,len(variables)):
    if target_variables[i].split("=")[1] != variables[i].split("=")[1]:
      source.append(variables[i])
      target.append(target_variables[i])

  source.append("**********************************")
  target.append("********************************** ")
  

result=source_name + " " + str(datetime.now(IST)).split(".")[0] + ".csv"  

file100.close()
df = pd.DataFrame({'Source File Values':source,'Target File Values':target})
df.to_csv(result, index=False, encoding='utf-8')

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

file=open(log_file,"a")

file.write("Now the file has more content!")

if len(target_variables) != len(variables):
    target_keyword=[]
    source_keyword=[]
    for i in variables:
      source_keyword.append(i.split("=")[0])
    for j in target_variables:
      target_keyword.append(j.split("=")[0])
    for i in source_keyword:
      if i not in target_keyword:
        file.write("vfgfgfggf")

if len(target_variables) != len(variables):
    target_keyword=[]
    source_keyword=[]
    for i in variables:
      source_keyword.append(i.split("=")[0])
    for j in target_variables:
      target_keyword.append(j.split("=")[0])
    for i in source_keyword:
      if i not in target_keyword:
        file.write("vfgfgfggf")