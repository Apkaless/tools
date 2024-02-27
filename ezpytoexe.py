import subprocess
import os
import time
import requests




def intro():



    print('''
        
    [+] Name      : EZ PY TO EXE 

    [+] Instagram : Apkalees

    [+] Github    : https://github.com/apkaless
              
''')

def converter(fpath, icpath, uac_admin):

    try:
    
        while True:

            try:

                subprocess.check_output('python --version', shell=True)

                break

            except subprocess.CalledProcessError:

                print('Python isn\'t Installed, Installing...\n')
                time.sleep(1)

                try:

                    requests.get('https://google.com')

                except:
                    print('\nYou Don\'t Have Internet Connection!\n')
                    time.sleep(3)
                    exit(0)

                subprocess.check_output('curl https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe -o python.exe', shell=True)

                subprocess.check_output('python.exe /quiet IntsallAllUsers=1 PrePendPath=1 Include_test=0', shell=True)

                time.sleep(1)

                print('\nPython Installed Successfully.\n')

                time.sleep(2)

                os.system('cls')

                continue


        while True:

            try:

                subprocess.check_output('pip --version', shell=True)

                break

            except subprocess.CalledProcessError:

                print('\nPip isn\'t Installed, Installing...\n')
                time.sleep(1)

                subprocess.check_output('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py', shell=True)

                subprocess.check_output('python get-pip.py', shell=True)

                subprocess.check_output('python -m pip install --upgrade pip setuptools wheel')

                time.sleep(1)

                print('\nPip Installed Successfully.\n')

                time.sleep(2)

                os.system('cls')
                
                continue


        while True:

            try:

                subprocess.check_output('pyinstaller -v', shell=True)

                break

            except subprocess.CalledProcessError:
                print('\nPyinstaller isn\'t Installed, Installing...\n')
                time.sleep(1)
                subprocess.check_output('pip install pyinstaller', shell=True)
                subprocess.check_output('pip install Pillow', shell=True)
                print('\nPyinstaller Installed Successfully.\n')
                time.sleep(2)
                os.system('cls')
                continue
        
        while True:

                subprocess.check_output('pip install Pillow', shell=True)
                os.system('cls')

                break

        os.system('cls')

        if uac_admin.upper() == 'Y':

            subprocess.check_output(f'pyinstaller --onefile {fpath} --uac-admin --icon {icpath}', shell=True)

        else:
            subprocess.check_output(f'pyinstaller --onefile {fpath} --icon {icpath}', shell=True)

    except Exception as e:
        print(e)


if __name__ == '__main__':

    try:

        intro()

        input('     Hit ENTER Key To Continue...')


        os.system('cls')

        fpath = input('Drag PY File Here : ')

        icpath = input('\nDrag Icon Here: ')

        uac_admin = input('\nDo You Wanna Add Admin privileges Y/N ? : ')

        converter(fpath, icpath, uac_admin)

    except Exception as e:
        print(e)
