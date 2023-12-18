import os
import subprocess
from colorama import Fore, init



def cleaner(user):

    x = 3

    deleted_files = []

    temp = False
    pre = False
    temp2 = False

    while x <=3:
        
        if x == 1:
            temp = False
            pre = False
            temp2 = True
            x = x - 1
            os.chdir(f'c:/users/{user}/appdata/Local/')
            print(f'\n{yellow}c:/users/{user}/appdata/Local/Temp\n______________________\n')
            print(f'{green}Are You Sure Y/N ? (*Hint: Select Y To Delete Temp Folder)')
            state = subprocess.check_output('rmdir /s Temp', shell=True, stderr=subprocess.STDOUT).decode()
            if 'Access is denied.' in state:
                print(f'\n{green}[+] Cleaner is Finished')
                break
            print(f'\n{green}[+] Cleaner is Finished')
            break
        elif x == 2:
            temp = False
            pre = True
            temp2 = False
            x = x - 1
            os.chdir('c:/Windows/Prefetch')
            print(f'{yellow}c:/Windows/Prefetch\n______________________\n')

        elif x == 3:
            temp = True
            pre = False
            temp2 = False
            x = x - 1
            os.chdir('c:/Windows/Temp')
            print(f'{yellow}c:/Windows/Temp\n______________________\n')
            
        elif x <= 0:
            exit(0)

        files_list = os.listdir()
        

        for file in files_list:

            not_empty_folders = []

            try:

                state = subprocess.check_output(f'rmdir {file}', shell=True, stderr=subprocess.STDOUT).decode()


                print(f'{blue}Folder Deleted --> {red}{file}\n')

                deleted_files.append(file)

            except subprocess.CalledProcessError as e:

                    if '267' in str(e):

                        state = subprocess.check_output(f'del {file}', shell=True, stderr=subprocess.STDOUT).decode()

                        print(f'{green}File Deleted --> {red}{file}\n')

                        deleted_files.append(file)

                    elif '145' in str(e):

                        try:

                            os.chdir(file)

                            not_empty_folders.append(file)

                            for file in os.listdir():

                                if os.path.isdir(file):

                                    print(f'{green}Are You Sure Y/N ? (*Hint: Select Y To Delete Temp Folder)')

                                    state = subprocess.check_output(f'rmdir {file} /s', shell=True, stderr=subprocess.STDOUT).decode()

                                    print(f'{blue}Folder Deleted --> {red}{file}\n')

                                    deleted_files.append(file)

                                else:    
                                    state = subprocess.check_output(f'del {file}', shell=True, stderr=subprocess.STDOUT).decode()

                                    print(f'{green}File Deleted --> {red}{file}\n')

                                    deleted_files.append(file)
                        
                            if temp:
                                os.chdir('c:/Windows/Temp')
                            elif pre:
                                os.chdir('c:/Windows/prefetch')
                            elif temp2:
                                os.chdir(f'c:/users/{user}/appdata/Local/')
                                
                            print(f'{green}Are You Sure Y/N ? (*Hint: Select Y To Delete Temp Folder)')
                            state = subprocess.check_output(f'rmdir {not_empty_folders[0]} /s', shell=True, stderr=subprocess.STDOUT).decode()

                            print(f'{blue}Folder Deleted --> {red}{not_empty_folders[0]}\n')

                            deleted_files.append(not_empty_folders[0])

                        except:
                            pass

    return len(deleted_files)

if __name__ == '__main__':

    init()

    red = Fore.RED
    blue = Fore.BLUE
    green = Fore.GREEN
    yellow = Fore.YELLOW

    current_username = os.getlogin()

    print('''
    
 ▄▄▄·  ▄▄▄·▄ •▄  ▄▄▄· ▄▄▌  ▄▄▄ ..▄▄ · .▄▄ · 
▐█ ▀█ ▐█ ▄██▌▄▌▪▐█ ▀█ ██•  ▀▄.▀·▐█ ▀. ▐█ ▀. 
▄█▀▀█  ██▀·▐▀▀▄·▄█▀▀█ ██▪  ▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄
▐█ ▪▐▌▐█▪·•▐█.█▌▐█ ▪▐▌▐█▌▐▌▐█▄▄▌▐█▄▪▐█▐█▄▪▐█
 ▀  ▀ .▀   ·▀  ▀ ▀  ▀ .▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀▀ 

    ''')
    print(f'{green}Welcome {blue}%s\n{green}This Script Cleans All The Temp Files From Your Windows\nFast And Easy To Use\n'%(current_username))

    input(f'{green}Press ENTER To Start The Cleaner...')

    os.system('cls')

    files_deleted = cleaner(current_username)

    os.system('cls')

    print(f'\n{green}[+] Files Deleted : {red}{files_deleted}')
    
    input(f'\n{green}Press Enter To Exit...')