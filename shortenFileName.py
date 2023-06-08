# Author: Mohamed Sassi
# This script can be used to shorten the long names of json files 
# Example: test123456.json ----> test.json
# It's a parametric script with 2 parameters: 
#    1) The full folder path like "C:\Users\msass\Documents\Peex2023\testjson"
#    2) The number of charakters to delete from the file name. In above example
#        the number is 6 
# Example of calling this script:
# python test1.py "C:\Users\msass\Documents\Peex2023\testjson" 6

import os, sys
import glob

# Working sirectory shoould be given as first parameter
wd=sys.argv[1]

# print working directory to just double check if it is the intended folder
print(wd)

# Desired slicing should be added as second paramater 
dl=-int(sys.argv[2])
#print(dl)

# change directory
wd=os.chdir(wd)
cwd = os.getcwd()

for file in glob.glob("*.json"):
    file_name = os.path.splitext(file)[0]
    extension = os.path.splitext(file)[1]
    file_before = file_name + extension
    file_after = file_name[:dl] + extension
    if(len(file_name) > -dl):
        try:
            os.rename(file, file_after)
        except OSError as e:
            #print(e)
            print(f'{file_before} can\'t be renamed')
        else:
            print(f'Renamed {file_before} to {file_after}')
    else:
        print(f'{file_before} can\'t be renamed')
        