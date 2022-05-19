# -*- coding: utf-8 -*-
"""
Created on Fri May 20 01:14:36 2022

@author: ausafumarkhan

Example of os.system from OS module
"""
import os

cmd="date"
rt=os.system(cmd)
if rt==0:
    print("Your command has executed successfully")
else:
    print("Command was failed")
    


