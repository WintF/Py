#import winreg

                       #registry = winreg.ConnectRegistry(socket.gethostname(), winreg.HKEY_LOCAL_MACHINE)
                      #winreg.OpenKey(registry, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon")

                      #path = winreg.OpenKey(registry, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon")


# Python program to explain os.path.exists() method

# importing os module
import os

# Specify path
path = '/usr/local/bin/'

# Check whether the specified
# path exists or not
isExist = os.path.exists(path)
print(isExist)

# Specify path
path = '/backup/TEST.txt'

# Check whether the specified
# path exists or not
isExist = os.path.exists(path)
print(isExist)












