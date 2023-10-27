import subprocess
import time
import requests
from colorama import Fore, init
from datetime import datetime



def  intro():
        
        status = check_status()
        print(f'''{red}

 ▄▄▄       ██▓███   ██ ▄█▀▄▄▄       ██▓    ▓█████   ██████   ██████ 
▒████▄    ▓██░  ██▒ ██▄█▒▒████▄    ▓██▒    ▓█   ▀ ▒██    ▒ ▒██    ▒ 
▒██  ▀█▄  ▓██░ ██▓▒▓███▄░▒██  ▀█▄  ▒██░    ▒███   ░ ▓██▄   ░ ▓██▄   
░██▄▄▄▄██ ▒██▄█▓▒ ▒▓██ █▄░██▄▄▄▄██ ▒██░    ▒▓█  ▄   ▒   ██▒  ▒   ██▒
 ▓█   ▓██▒▒██▒ ░  ░▒██▒ █▄▓█   ▓██▒░██████▒░▒████▒▒██████▒▒▒██████▒▒
 ▒▒   ▓▒█░▒▓▒░ ░  ░▒ ▒▒ ▓▒▒▒   ▓▒█░░ ▒░▓  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
  ▒   ▒▒ ░░▒ ░     ░ ░▒ ▒░ ▒   ▒▒ ░░ ░ ▒  ░ ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░
  ░   ▒   ░░       ░ ░░ ░  ░   ▒     ░ ░      ░   ░  ░  ░  ░  ░  ░  
      ░  ░         ░  ░        ░  ░    ░  ░   ░  ░      ░        ░  
                                                                    
                            
                    ===================================
                    | {red}[Instagram]: {white}Apkalees           {red}|
                    {red}| {red}[Status]   : {white}{status}             {red}|
                    {red}===================================
      
''')
        
        return status


def check_status():

    try:
          
        requests.get('https://google.com')

        status = 'Online'

    except:
         pass
         status = 'Offline'

    return status

def TurnWinDefOff():

    try:
         
        res = subprocess.check_output('netsh advfirewall set allprofiles state off', shell=True).decode()
        
    except subprocess.CalledProcessError as e:
         with open('error.txt', 'a') as f:
              
              f.write(str(e))
    
    return res





def TurnWinDefOn():


    try:
         
        res = subprocess.check_output('netsh advfirewall set allprofiles state on', shell=True).decode()

    except subprocess.CalledProcessError as e:
         with open('error.txt', 'a') as f:
              
              f.write(str(e))
    
    return res


if __name__ == '__main__':

    init(convert=True)
    red = Fore.RED
    white = Fore.WHITE
    blue = Fore.BLUE
    lmg = Fore.LIGHTMAGENTA_EX
    yellow = Fore.YELLOW

    status = intro()

    if status == 'Online':
         pass
    
    else:
        input(f'\n{red}[{str(datetime.time(datetime.now())).split(".")[0]}] [CONSOLE]: {white}You Are Not Connected To The Internet !! ')
        exit(0)
        
    input(f'\n{red}[{str(datetime.time(datetime.now())).split(".")[0]}] [CONSOLE]: {white}Press {blue}[ENTER] {white}To Start The {lmg}Magic !! ')

    TurnWinDefOff()

    time.sleep(1)

    print(f'\n\n{red}[{str(datetime.time(datetime.now())).split(".")[0]}] [CONSOLE]: {white}Your {lmg}Magic {white}Has Been {blue}Connected {white}To Your Network !! {yellow}Play Your Game Now !! \n')

    time.sleep(0.03)

    input(f"\n{red}[{str(datetime.time(datetime.now())).split('.')[0]}] [CONSOLE]: {yellow}** Don't Close The Application {white}Press {blue}[ENTER] {white}When You Exit From Your Game !! ")

    time.sleep(2)

    TurnWinDefOn()

    input(f"\n\n{red}[{str(datetime.time(datetime.now())).split('.')[0]}] [CONSOLE]: {white}You Are Safe Now, {white}Press {blue}[ENTER] {white}To Close The Application !! ")

    time.sleep(2)