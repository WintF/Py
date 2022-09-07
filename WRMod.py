### Find files specifics

import os
import glob

os.chdir('D:\Work_Folder')
files = glob.glob('*.txt')

print(files)

