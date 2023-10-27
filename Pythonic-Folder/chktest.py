import requests
from threading import Thread, Lock
from colorama import Fore, init
import time
import os





init(convert=True)

red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW 
white = Fore.WHITE
cyan = Fore.CYAN


def check(proxy):
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'Connection': 'keep-alive',

        }

        try:
            response = requests.get('https://api.ipify.org', headers=headers, proxies={"https": f'http://{proxy}'}, timeout=10)

            if response.status_code == 200:
                latency = round(response.elapsed.total_seconds() * 1000)
                print(f'{green}Good {response.text} | Latency: {latency}')
                with open('Alive_proxies.txt', 'a') as f:
                    f.writelines([proxy, '\n'])
                    f.close()

            else:
                print(f'{red}Dead {proxy}')

        except Exception as e:
            print(f'{yellow}Dead ERROR {proxy}')
            pass

if __name__ == '__main__':
     
     proxies = []

     proxyfile = open('c:/users/sabah/Scraped_proxies.txt', 'r')
     proxieslist = proxyfile.readlines()
     for proxy in proxieslist:
          proxies.append(proxy)
    
     threads = []


     for i in range(200):

        for prx in proxies:
            prx = prx.strip()
            th = Thread(target=check, args=(prx,))
            th.start()
            threads.append(th)
            time.sleep(0.06)

     for th in threads:
        th.join()
