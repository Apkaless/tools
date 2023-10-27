import os
import time
import userpaths
from colorama import Fore, init




def logo():

    init(convert=True)

    print(f'''{green}            
    ▄▄▄       ██▓███   ██ ▄█▀▄▄▄       ██▓    ▓█████   ██████   ██████    
    ▒████▄    ▓██░  ██▒ ██▄█▒▒████▄    ▓██▒    ▓█   ▀ ▒██    ▒ ▒██    ▒    
    ▒██  ▀█▄  ▓██░ ██▓▒▓███▄░▒██  ▀█▄  ▒██░    ▒███   ░ ▓██▄   ░ ▓██▄      
    ░██▄▄▄▄██ ▒██▄█▓▒ ▒▓██ █▄░██▄▄▄▄██ ▒██░    ▒▓█  ▄   ▒   ██▒  ▒   ██▒   
    ▓█   ▓██▒▒██▒ ░  ░▒██▒ █▄▓█   ▓██▒░██████▒░▒████▒▒██████▒▒▒██████▒▒   
    ▒▒   ▓▒█░▒▓▒░ ░  ░▒ ▒▒ ▓▒▒▒   ▓▒█░░ ▒░▓  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░   
    ▒   ▒▒ ░░▒ ░     ░ ░▒ ▒░ ▒   ▒▒ ░░ ░ ▒  ░ ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░   
    ░   ▒   ░░       ░ ░░ ░  ░   ▒     ░ ░      ░   ░  ░  ░  ░  ░  ░     
        ░  ░         ░  ░        ░  ░    ░  ░   ░  ░      ░        ░     
                                                                        
        

    {green}[+] {white}Tool      {green}==> {white}R6 Server Changer
              
    {green}[+] {white}Instagram {green}==> {white}Apkaless

    {green}[+] {white}Github    {green}==> {white}https://github.com/apkaless

    {green}[+] {white}Rainbow Six Siege

    {green}===========================================================================
        ''')

def ServerChanger():

    region = input(f'''    {green}Select Server : 

    {green}[1] {white}UAE Middle East Server

    {green}[2] {white}EU European Server

    {green}[3] {white}Default

    {green}=========|--->{white} ''')

    if region.isdigit():
        pass

    else:
        return False


    regions = {

        'uae': 'playfab/uaenorth',
        'eu': 'playfab/westeurope',
        'def': 'default'
    }

    if int(region) == 1:

        server = regions['uae']
        serverName = 'UAE Server'

    elif int(region) == 2:

        server = regions['eu']
        serverName = 'EU Server'
    
    elif int(region) == 3:

        server = regions['def']
        serverName = 'Default'

    else:
        return None

    docFolder = userpaths.get_my_documents()

    os.chdir(docFolder)

    os.chdir('My Games')

    os.chdir('Rainbow Six - Siege')

    gameSettingsFile = os.listdir()


    for gameFolder in gameSettingsFile:

        if gameFolder.startswith('Ben'):
            continue

        try:

            os.chdir(gameFolder)

            config_list = os.listdir()

            for gFile in config_list:


                with open(gFile, 'r+') as f:

                    config = f.read().splitlines()

                    dataCenter = config[-3]

                    if 'DataCenter' in dataCenter:
                        
                        data = dataCenter.split('=')

                        full_server = data[0] + '=' + server

                        config[-3] = full_server

                        buff = '\n'.join(config)

                        f.write(buff)

                        f.write('\n')

                        os.chdir('..')

                    else:

                        dataCenter = config[-2]

                        data = dataCenter.split('=')

                        full_server = data[0] + '=' + server

                        config[-2] = full_server

                        buff = '\n'.join(config)

                        f.write(buff)

                        f.write('\n')

                        os.chdir('..')
        except:
            return None


    try:

        oldServer = data[1].split("/")[1]

    except:

        oldServer = data[1]


    newServer = serverName

    return True, oldServer, newServer

if __name__ == '__main__':

    green = Fore.GREEN
    white = Fore.WHITE
    red = Fore.RED
    blue = Fore.BLUE

    while True:
        
        os.system('cls')

        logo()

        try:

            a, old, new = ServerChanger()

            if a:

                print(f'\n{green}[+] {white}New Server: {new}\n\n{red}[-] {white}Old Server: {old}\n\n')

                input('Press ENTER To Exit...')
                
                os.system('cls')
                
                break

        except:

            os.system('cls')

            print(f'\n{red}[x] {white}Please Type One Of These Numbers 1, 2, 3\n')

            time.sleep(3)

            continue