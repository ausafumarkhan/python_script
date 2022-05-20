# -*- coding: utf-8 -*-
"""
Created on Sat May 21 01:25:50 2022

@author: ausafuamrkhan

os.walk(path): This module is used to generate directory and file names in a 
directory tree by walking
"""

import os

'''
path="F:\\git_repos\\python_scripting"


print(list(os.walk(path))) #convert generator output of os.walk(path) to list
for each in os.walk(path):
   print(each)
    
for r,d,f in os.walk(path,topdown=False): # r--> path , d--> directory f--> file
    print(f)         # topdown Bydefault its 'true', false means bottom to top
'''

# Script to search file with entire path

req_file=input("Enter the file name to search:")
for r,d,f in os.walk("F:\\git_repos\\python_scripting"):
    for each_file in f:
        if each_file==req_file:
            print(os.path.join(r, each_file))