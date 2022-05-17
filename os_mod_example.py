# -*- coding: utf-8 -*-
"""
Created on Tue May 17 23:27:42 2022

@author: Ausaf Umar Khan
"""


import os
print(os.sep) # It will print the separator \ for windows and / for linux OS

print(os.getcwd()) # print current working directory

print(os.listdir()) # list directory as a list

print(type(os.listdir())) #print class as list 

print(os.mkdir("F:\\test_dir")) # create a empty directory in F drive

print(os.makedirs("F:\\abc\\ab\\a")) # create directory recursively like "mkdir -p" in linux

# os.removedirs("F:\\xyz") # Delete the directory

# os.remove("F:\\tes_file") # Delete the file

# os.rmdir(path) 

# os.rename(src, dst)

# print(os.environ)
