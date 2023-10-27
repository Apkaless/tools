import re
import os
import subprocess
import platform


def system_Detection():

    isWindows = False

    if 'Windows' or 'windows' in platform.platform:

        isWindows = True
    
    else:
        pass

    return isWindows

def windows_Key(key_string=str):

    res = re.search('([A-Z0-9]{5}-[A-Z0-9]{5}-?){2}+[A-Z0-9]{5}', key_string)

    if res:
        return res.group()
    else:
        print('\nYour Windows Not Activated.\n')

if __name__ =='__main__':

    if system_Detection():

        os.system('cls')

        start_action = input('\nPress Enter To Run The Script...')

        os.system('cls')

        query = subprocess.check_output('reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform"', shell=True).decode()

        key = windows_Key(query)

        if key:

            print('\nActivation Key : ' + key + '\n')
            
        os.system('PAUSE')

    else:
        print('\nYour Operation System Not Supported!.\n')