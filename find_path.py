import os
#import platform

path=input("Enter the path:")
if os.path.exists(path):
    print(f"The given path:{path} is a valid path")
    if os.path.isfile(path):
        print(f"The given path:{path} is a file")
    else:
        print(f"and {path} is a directory")
else:
    print(f"The given path:{path} is invalid. Please enter the valid path")