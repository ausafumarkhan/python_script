# -*- coding: utf-8 -*-
"""
Created on Sat May 21 01:46:13 2022

@author: ausafumarkhan
"""
# Script will find the valid drive in Windows OS

import os 
import string

pd_names=string.ascii_uppercase
vd_names=[]

for each_drive in pd_names:
    if os.path.exists(each_drive+":\\"):
        vd_names.append(each_drive+":\\")
print(vd_names)

for each_drive in vd_names:
    for r,d,f in os.walk(each_drive):
        for each_file in f:
            print(os.path.join(r,each_file))
            
