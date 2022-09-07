### Find files specifics

import os
import glob
import winreg


os.chdir('D:\Work_Folder')
files = glob.glob('*.txt')

print(files)


def getPath():
    # Open the key and return the handle object.
    hKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "COMODO")

    # Read the value.
    result = winreg.QueryValueEx(hKey, "AutoAdminLogon")

    # Close the handle object.
    result = result[0]
    return result
    winreg.CloseKey(hKey)