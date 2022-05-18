# -*- coding: utf-8 -*-
"""
Created on Thu May 19 01:17:49 2022

@author: ausafumarkhan
"""
'''
This will take a path and identifies file and directory
'''
import os.path # import os--> os.path is a part of os module

path="F:\\git_repos\\python_scripting"

if os.path.isdir(path):
    print(f"{path} is a directory")
else:
    print(f"{path} is a file")


#### Few examples of os module

'''
1. 
print(os.path.sep)

2.
if path=F:\git_repos\python_scripting
print(os.path.basename(path)) # print ---> python_scripting

3.
print(os.path.dirname(path))

4.
print(os.path.join(path1,path2)) # to include separator between two paths

5.
print(os.path.split(path)) # split path into head and tail

6.
print(os.pah.getsize(path)) # size of directory or file

7.
print(os.path.exits(path)) # o/p as true or false

8.
print(os.path.isfile(path))

9.
print(os.path.isdir(path))

10.
print(os.path.islink(path))

11.
print(os.path.getctime(path))

12.
print(os.path.getatime(path))

13.
print(os.path.getmtime(path))

'''


