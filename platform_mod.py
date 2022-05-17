# -*- coding: utf-8 -*-
"""
Created on Tue May 10 07:35:58 2022

@author: Ausaf Umar Khan

Platform module is used to access the underlying platfrom's data such as Hardware,
operating system and interpreter version info.

"""

import platform as pt
#---- Other Method to Declare modules in python script ------#
# import platform
# from platform import *
# from platform import system, platform

#print(f"Python Version is: {pt.python.Version()}")
print(f"This is {pt.system()} machine")
print(pt.python_version_tuple())
print(pt.release())
print(pt.platform())
print(pt.machine())
print(pt.architecture())
print(pt.processor())
print(pt.node())
print(pt.uname())