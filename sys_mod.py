#The sys module provides functions and variables used to manipulates different parts of the Python runtime environment 
'''
This script takes input from user and print accordingly



usr_str=input("Enter your string: ")
usr_action=input("Enter your action (Valid: lower/upper/title): ")

if usr_action=="lower":
    print(usr_str.lower())
elif usr_action=="upper":
    print(usr_str.upper())
elif usr_action=="title":
    print(usr_str.title())
else:
    print("Please enter valid action")

#Above script can be written using sys module

import sys
usr_str=sys.argv[1]
usr_action=sys.argv[2]

if usr_action=="lower":
    print(sys.argv[1].lower())
elif usr_action=="upper":
    print(sys.argv[1].upper())
elif usr_action=="title":
    print(sys.argv[1].title())
else:
    print("Enter the valid action")
# Above script has a drawback, we need to pass three argument for successful execution of the script
'''

import sys

if len(sys.argv)!=3:
    print("Usage: ")
    print(f"{sys.argv[0]} <your string> <lower|upper|title>")
    sys.exit()

usr_str=sys.argv[1]
usr_action=sys.argv[2]

if usr_action=="lower":
    print(sys.argv[1].lower())
elif usr_action=="upper":
    print(sys.argv[1].upper())
elif usr_action=="title":
    print(sys.argv[1].title())
else:
    print("Enter the valid action")
