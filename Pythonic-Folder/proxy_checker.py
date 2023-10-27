import requests
from threading import Thread, Lock
from colorama import Fore, init
import time
import os
import cloudscraper

def intro():

    init(convert=True)

    red = Fore.RED
    green = Fore.GREEN
    yellow = Fore.YELLOW 
    white = Fore.WHITE
    cyan = Fore.CYAN
    print(f'''{cyan}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

                         _____                        _____ _               _             
                        |  __ \                      / ____| |             | |            
                        | |__) | __ _____  ___   _  | |    | |__   ___  ___| | _____ _ __ 
                        |  ___/ '__/ _ \ \/ / | | | | |    | '_ \ / _ \/ __| |/ / _ \ '__|
                        | |   | | | (_) >  <| |_| | | |____| | | |  __/ (__|   <  __/ |   
                        |_|   |_|  \___/_/\_\\__, |  \_____|_| |_|\___|\___|_|\_\___|_|   
                                              __/ |                                       
                                             |___/                                        

                                                                                                                                                                                                                                                                                                                   
 
                            {red}|    {cyan}[+] {white}Name        {cyan}: {green}Proxy Checker                  {red}|
                            {red}|                                                     {red}|
                            {red}|    {cyan}[+] {white}Instagram   {cyan}: {green}Apkalees                       {red}| 
                            {red}|                                                     {red}| 
                            {red}|    {cyan}[+] {white}Github      {cyan}: {green}https://github.com/apkaless    {red}| 
                            {red}|                                                     {red}|
                            {red}|    {cyan}[+] {white}Nationality {cyan}: {green}Iraq                           {red}|
          
''')

hits = []
errors = []
total = []
lats = []
http = []
socks4 = []
total_checked = []

def display(hits: int, errors: int, total: int, lat, socks4: int, https: int):

    os.system('cls')

    print(f'''{lc}                  
                                      _____                        _____ _               _             
                                     |  __ \                      / ____| |             | |            
                                     | |__) | __ _____  ___   _  | |    | |__   ___  ___| | _____ _ __ 
                                     |  ___/ '__/ _ \ \/ / | | | | |    | '_ \ / _ \/ __| |/ / _ \ '__|
                                     | |   | | | (_) >  <| |_| | | |____| | | |  __/ (__|   <  __/ |   
                                     |_|   |_|  \___/_/\_\\__, |  \_____|_| |_|\___|\___|_|\_\___|_|   
                                                           __/ |                                       
                                                          |___/  
                                                  
{lc}========================================================================================================================

                                                                                                                                                
                                                    {white}[!] Total Proxies: [{str(total).strip()}]                                                                                                                                                
                                                    {green}[+] Alive Proxies: [{str(hits).strip()}]

                                                    {green}[+] Socks4: [{str(socks4).strip()}]

                                                    {green}[+] Http: [{str(https).strip()}]

                                                    {green}[+] Latency: [{lat} ms]                                                                                                                                                         
                                                    {red}[-] Dead Proxies: [{str(errors).strip()}]

                                                                                                                                                        
{lc}========================================================================================================================

''')
    
def check(proxy):
        
        protos = [f'http://{proxy}', f'socks4://{proxy}']

        for pprox in protos:

            cl = cloudscraper.create_scraper(browser={'browser': 'chrome', 'platform': 'windows', 'mobile': False})

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'Connection': 'keep-alive',

            }

            try:
                    
                response = cl.get('https://api.ipify.org/', headers=headers, proxies={'https': f'{pprox}'}, timeout=10)
                if response.status_code == 200:

                    lat = round(response.elapsed.total_seconds() * 1000)
                    lats.append(lat)
                    hits.append(proxy)

                    if pprox.startswith('http'):

                        http.append(proxy)

                    else:
                        socks4.append(proxy)

                    with open('Live_proxies.txt', 'a') as f:
                        f.writelines([proxy, '\n'])
                        f.close()

                    total_checked.append(proxy)

                else:
                    errors.append(e)
                    total_checked.append(proxy)

            except Exception as e:
                errors.append(e)
                total_checked.append(proxy)
                continue

if __name__ == '__main__':
    os.system('cls')
    white = Fore.WHITE
    green = Fore.GREEN
    red = Fore.RED
    yellow = Fore.YELLOW
    lc = Fore.LIGHTCYAN_EX

    intro()

    input(f'\n{green}[+] {white}Press {green}ENTER {white}To Start Proxies Checker ...')

    os.system('cls')

    while True:

        intro()

        proxies = input(f'\n{green}[+] {white}Proxies File ===> ')

        if proxies:
            pass
        else:
            os.system('cls')
            continue

        try:

            with open(proxies, 'r') as f:

                proxies = f.readlines()

                total = len(proxies)

                threads = []

                for proxy in proxies:

                    prox = proxies.index(proxy)

                    proxies.pop(prox)

                    if len(lats) > 0:
                        lat = lats[-1]
                    else:
                        lat = 0

                    display(hits=len(hits), errors=len(errors), total=total, lat=lat, socks4=len(socks4), https=len(http))

                    if len(total_checked) == total:
                        break

                    proxy = proxy.splitlines()[0].strip()

                    thread = Thread(target=check, args=(proxy,))
                    thread.start()
                    threads.append(thread)
                    time.sleep(0.05)

                for t in threads:
                    t.join()
                
                break

        except FileNotFoundError:
            print(f'\n{yellow}[!] {red}Please Make Sure That File Is Exist.')
            time.sleep(2)
            os.system('cls')
        except KeyboardInterrupt:
            input(f'\n{yellow}[!] {white}Press Enter To Start The Checker Again ...')
            os.system('cls')
            continue
        except MemoryError:
            input(f'\n{yellow}[!] {white}Press Enter To Quit ...')
            os.system('cls')
            break