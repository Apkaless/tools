import winreg
import time
import os




def find_registry_sub_key(hku):

    for sub_key in range(6):

        try:

            reg = winreg.EnumKey(hku, sub_key)

            if reg.endswith('Classes'):

                return reg
            
            else:
                continue
            
        except Exception as e:

            return False

def delete_IDM_registry_key(hku, sub_key):

    try:

        winreg.DeleteKey(hku, sub_key + '\WOW6432Node\CLSID\{07999AC3-058B-40BF-984F-69EB1E554CA7}')
        print(sub_key)
        return True
    
    except:

        return False
    
if __name__ == '__main__':

    os.system('cls')

    print('''
    ___          __         __              
   /   |  ____  / /______ _/ /__  __________
  / /| | / __ \/ //_/ __ `/ / _ \/ ___/ ___/
 / ___ |/ /_/ / ,< / /_/ / /  __(__  |__  ) 
/_/  |_/ .___/_/|_|\__,_/_/\___/____/____/  
      /_/                                   

      
[+] Name      : IDM Trial Reset

[+] Instagram : Apkalees

[+] Github    : https://github.com/apkaless


''')

    input('Press Enter To Start...')

    os.system('cls')

    hku = winreg.HKEY_USERS

    sub_key = find_registry_sub_key(hku)

    if sub_key:

        if delete_IDM_registry_key(hku, sub_key):

            print('\n[+] IDM Trial Reset Done!\n')

            print('\n[+] IDM Trial Status: 30 Days\n')
            
            print('\n[+] Coded By: Apkaless The Eagle\n')

            print('\n[+] Instagram: Apkalees\n')

            print('\n[+] Github: github.com/Apkaless\n')

            time.sleep(5)

            exit(0)
            
        else:
            print('\n[-] Unknown Error!\n')

            time.sleep(3)

            exit(0)
    else:
         print('\nNo Key Was Found!\n')