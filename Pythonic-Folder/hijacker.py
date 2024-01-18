from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
from bs4 import BeautifulSoup as bs
import requests
import re
import json
from colorama import Fore, init
import os
from threading import Thread
import time
from time import sleep
import urllib.request
import subprocess
import customtkinter
import winreg
import userpaths
from equip import apkaless_pic_data, app


apkaless_pic_data = apkaless_pic_data

app_data = app

create_app_icon = open('app.png', 'wb')

create_apkaless_pic = open('apkaless.jpg', 'wb')

create_apkaless_pic.write(apkaless_pic_data)

create_app_icon.write(app_data)

create_apkaless_pic.close()

create_app_icon.close()

def get_proxies():

    class SCRAPER:

        init = init(convert=True)
        white = Fore.WHITE
        green = Fore.GREEN

        proxies = []

        timeout = 10


        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
        
        def __init__(self) -> None:
            pass

        def proxy_1():

            proxies = []

            url = 'https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc'

            try:

                res = requests.get(url, headers=SCRAPER.headers, timeout=SCRAPER.timeout)

                for inp in res.json()['data']:

                    ip = inp['ip']
                    port = inp['port']

                    proxy = ip + ':' + port

                    result_Widget.insert(END, proxy + '\n')

                    SCRAPER.proxies.append(proxy)
            except:
                pass

            url = 'https://www.proxyscan.io/api/proxy?last_check=9800&country=fr,us,ru&uptime=50&ping=800&limit=20&type=socks4,socks5,http,https'
            
            for i in range(1, 10):

                try:

                    res = requests.get(url, SCRAPER.headers, timeout=SCRAPER.timeout)

                    for jd in res.json():

                        ip = jd['Ip']

                        port = jd['Port']

                        proxy = ip + ':' + port

                        result_Widget.insert(END, proxy + '\n')

                        SCRAPER.proxies.append(proxy)
                except:
                    pass

            return proxies

        
        def proxy_2():

            try:

                proxies = []

                urls = ['https://free-proxy-list.net/', 'https://hidemyna.me/en/proxy-list/']

                for url in urls:

                    res = requests.get(url, headers=SCRAPER.headers, timeout=SCRAPER.timeout)

                    res = json.dumps(res.text)

                    sp = bs(res, 'html.parser')

                    table = sp.find('table')

                    trs = table.find_all('tr')

                    for tds in trs[1:]:

                        ip = tds.find_all('td')[0].getText()

                        port = tds.find_all('td')[1].getText()

                        proxy = ip + ':' + port


                        result_Widget.insert(END, proxy + '\n')

                        SCRAPER.proxies.append(proxy)
                
                url = 'https://proxyhub.me/'

                for n in range(1, 100):

                    res = requests.get(url, headers=SCRAPER.headers, cookies={'page': str(n), 'anonymity': 'all'}, timeout=SCRAPER.timeout)

                    res = json.dumps(res.text)

                    sp = bs(res, 'html.parser')

                    table = sp.find('table')

                    trs = table.find_all('tr')

                    for tds in trs[1:]:

                        ip = tds.find_all('td')[0].getText()

                        port = tds.find_all('td')[1].getText()

                        proxy = ip + ':' + port

                        result_Widget.insert(END, proxy + '\n')

                        SCRAPER.proxies.append(proxy)

                return proxies
            
            except:
                pass
        
        def proxyScraper():

            try:

                proxies = []

                urls = ['https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all', 'https://proxy-daily.com/', 'https://spys.me/proxy.txt', 'https://rootjazz.com/proxies/proxies.txt', 'https://www.proxy-list.download/api/v1/get?type=http', 
                        'https://www.proxy-list.download/api/v1/get?type=https', 'https://proxyspace.pro/https.txt', 'https://proxyspace.pro/http.txt', 
                        'https://proxylist.live/nodes/free_1.php?page=1&showall=1', 'https://openproxylist.xyz/http.txt', 'https://openproxy.space/list/http', 'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt',
                        'https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt', 'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
                        'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt', 'https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt',
                        'https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt', 'https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt',
                        'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt', 'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt',
                        'https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt', 'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt',
                        'https://rootjazz.com/proxies/proxies.txt', 'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt', 'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
                        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
                        'https://raw.githubusercontent.com/ToShukKr/rProxyList/main/proxy-list.txt', 'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
                        'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt', 'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt',
                        'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks4.txt',
                        'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/socks4_proxies.txt',
                        'https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt', 'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt',
                        'https://raw.githubusercontent.com/iptotal/free-proxy-list/master/socks4.txt', 'https://raw.githubusercontent.com/NotUnko/autoproxies/main/socks4.txt',
                        'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt', 'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt']

                for url in urls:

                    res = requests.get(url, headers=SCRAPER.headers, timeout=SCRAPER.timeout)

                    scraped_proxies = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', res.text)

                    SCRAPER.proxies.extend(scraped_proxies)

                return proxies
            
            except:
                pass
        
        def proxyScraper_2():

            proxies = []

            headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
            }

            urls = ['https://www.freeproxy.world/', 'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=2', 'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=3', 'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=4', 'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=5']

            for url in urls:

                try:

                    res = requests.get(url, headers=headers, timeout=SCRAPER.timeout)

                    res = json.dumps(res.text)

                    sp = bs(res, 'html.parser')

                    table = sp.find('table')

                    trs = table.find_all('tr')

                    for tds in trs[2:]:

                        try:

                            ip = tds.find_all('td')[0].getText()

                            port = tds.find_all('td')[1].getText()

                            proxy = ip + ':' + port

                            proxy = proxy.split('\\n')

                            full_proxy = proxy[1] + ':' + proxy[3]

                            result_Widget.insert(END, full_proxy + '\n')

                            SCRAPER.proxies.append(full_proxy)

                        except:
                            pass
                except:
                    pass

            return proxies
        

    if __name__ == '__main__':

        white = Fore.WHITE
        green = Fore.GREEN
        red = Fore.RED

        get_prx.config(state='disabled')
        load_prx_btn.config(state='disabled')
        save_prx_btn.config(state='disabled')
        check_prx_btn.config(state='disabled')

        threads = []

        for i in range(1):

            th1 = Thread(target=SCRAPER.proxy_1)

            th2 = Thread(target=SCRAPER.proxy_2)

            th3 = Thread(target=SCRAPER.proxyScraper)

            th4 = Thread(target=SCRAPER.proxyScraper_2)

            th1.start()
            threads.append(th1)
            time.sleep(1)
            th2.start()
            threads.append(th2)
            time.sleep(1)
            th3.start()
            threads.append(th3)
            time.sleep(1)
            th4.start()
            threads.append(th4)
            time.sleep(1)
        
        for thread in threads:
            thread.join()

        try:

            proxies = SCRAPER.proxies

            b = len(proxies)

            new: list = [prx for prx in dict.fromkeys(proxies)]

            a = len(new)

            result_Widget.delete('1.0', END)

            for prx in new:

                result_Widget.insert(END, prx + '\n')

        except Exception as e:
            print(e)
            pass

        finally:

            messagebox.showinfo(title='Proxy Scraper', message=f'{a} Proxies')

            get_prx.config(state='active')
            load_prx_btn.config(state='active')
            save_prx_btn.config(state='active')
            check_prx_btn.config(state='active')


def open_file(*e):

    filepath = filedialog.askopenfilename()

    file = open(filepath, 'r', encoding='utf8')

    text = file.read()

    textWidget.delete('1.0', END)

    textWidget.insert('1.0', text)

    return None



def save_file(*e):

    text = textWidget.get('1.0', END)

    askforfile = filedialog.asksaveasfile('w', title='Save File As', filetypes=[('Text File', '.txt'), ('HTML File', '.html'), ('PY File', '.py'), ('CPP File', '.cpp'), ('CUSTOM', '.*')], defaultextension='.txt')

    askforfile.write(text)

    askforfile.close()

    return None


def undo():

    try:

        textWidget.edit_undo()

        return None
    
    except:
        pass


def redo():

    try:

        textWidget.edit_redo()

        return None
    
    except:
        pass


def cut():

    text = textWidget.index('insert')


    text = text.split('.')[0] + '.0'

    current_text = textWidget.get(text, END)
    
    textWidget.clipboard_clear()

    textWidget.clipboard_append(current_text)

    textWidget.delete(text, END)

    return None

def copy():

    text = textWidget.index('insert')

    text = text.split('.')[0] + '.0'

    current_text = textWidget.get(text, END)
    
    textWidget.clipboard_clear()

    textWidget.clipboard_append(current_text)

    return None


def paste():

    text = textWidget.clipboard_get()
    
    current_cursor_index = textWidget.index('insert')

    cindex = current_cursor_index.split('.')[0] + '.0'

    textWidget.insert(cindex, text)
    
    return None

def find():

    text = simpledialog.askstring(title='Find Text', prompt='Type The Text')

    result = textWidget.search(text, '1.0', END)

    if result:

        textWidget.see(result)

        infomessage = messagebox.showinfo(title='Text Result', message='Found at Line ' + result)

    else:
        
        messagebox.showinfo(title='Text Result', message='Text Not Found')

    return None


def themes_window():

    color_values = colorchooser.askcolor()

    textWidget.config(bg=color_values[1])

    return None


def theme1():

    textWidget.config(bg='#000000', fg='#69C913', insertbackground='#69C913')

    return None

def theme2():

    textWidget.config(bg='gray', fg='white', insertbackground='black')

    return None

def theme3():

    textWidget.config(bg='#D0C8CD', fg='purple', insertbackground='black')
    return None


def load_proxy():
        
    get_prx.config(state='disabled')
    load_prx_btn.config(state='disabled')
    save_prx_btn.config(state='disabled')
    check_prx_btn.config(state='disabled')

    try:

        proxy_file = filedialog.askopenfilename()

        file = open(proxy_file, 'r', encoding='utf8')

        text = file.read()

        result_Widget.delete('1.0', END)

        result_Widget.insert(END, text)
    
    except:
        pass

    finally:

        get_prx.config(state='active')
        load_prx_btn.config(state='active')
        save_prx_btn.config(state='active')
        check_prx_btn.config(state='active')

def save_prx():

    get_prx.config(state='disabled')
    load_prx_btn.config(state='disabled')
    save_prx_btn.config(state='disabled')
    check_prx_btn.config(state='disabled')

    try:

        file = filedialog.asksaveasfile(mode='w', filetypes=[('Text File', '.txt')], defaultextension='.txt')

        text = result_Widget.get('1.0', END)

        file.write(text)

        file.close()
        
    except:
        pass

    finally:

        get_prx.config(state='active')
        load_prx_btn.config(state='active')
        save_prx_btn.config(state='active')
        check_prx_btn.config(state='active')

def check_prx():

    class HttpProxyChecker():
        """"
        (Http Type Proxy)
        Return True If The Given Proxy Is Working, 
        Return False If The Given Proxy Is Dead
        """
        def __init__(self, proxy: str, timeout: float) -> None:
            self.proxy = proxy
            self.timeout = timeout
        

        def __buildHandler__(self):

            proxyHandler = urllib.request.ProxyHandler(proxies={'https': f'http://{self.proxy}'})

            return proxyHandler
        
        def __build_opener__(self, handler):

            return urllib.request.build_opener(handler)
        
        def __install_opener__(self, opener):

            return urllib.request.install_opener(opener)
        
        def start_checker(self):
            handler = self.__buildHandler__()
            opener = self.__build_opener__(handler)
            self.__install_opener__(opener)

            try:

                resp = urllib.request.urlopen('https://github.com', timeout=self.timeout)
                return True
            
            except Exception as e:
                return False
            
        def remove_duplicated(self, anyList: list) -> list:

            cleaned_list = [dict.fromkeys(anyList)]

            return cleaned_list


    class Socks4ProxyChecker():
        """"
        (Socks4 Type Proxy)
        Return True If The Given Proxy Is Working, 
        Return False If The Given Proxy Is Dead
        """
        def __init__(self, proxy: str, timeout: float) -> None:
            self.proxy = proxy
            self.timeout = timeout
        

        def __buildHandler__(self):

            proxyHandler = urllib.request.ProxyHandler(proxies={'https': f'socks4://{self.proxy}'})

            return proxyHandler
        
        def __build_opener__(self, handler):

            return urllib.request.build_opener(handler)
        
        def __install_opener__(self, opener):

            return urllib.request.install_opener(opener)
        
        def start_checker(self):
            handler = self.__buildHandler__()
            opener = self.__build_opener__(handler)
            self.__install_opener__(opener)

            try:

                resp = urllib.request.urlopen('https://github.com', timeout=self.timeout)
                return True
            
            except Exception as e:
                return False
            
        def remove_duplicated(self, anyList: list) -> list:

            cleaned_list = [dict.fromkeys(anyList)]

            return cleaned_list

    class Socks5ProxyChecker():
        """"
        (Socks5 Type Proxy)
        Return True If The Given Proxy Is Working, 
        Return False If The Given Proxy Is Dead
        """
        def __init__(self, proxy: str, timeout: float) -> None:
            self.proxy = proxy
            self.timeout = timeout
        

        def __buildHandler__(self):

            proxyHandler = urllib.request.ProxyHandler(proxies={'https': f'socks5://{self.proxy}'})

            return proxyHandler
        
        def __build_opener__(self, handler):

            return urllib.request.build_opener(handler)
        
        def __install_opener__(self, opener):

            return urllib.request.install_opener(opener)
        
        def start_checker(self):
            handler = self.__buildHandler__()
            opener = self.__build_opener__(handler)
            self.__install_opener__(opener)

            try:

                resp = urllib.request.urlopen('https://github.com', timeout=self.timeout)
                return True
            
            except Exception as e:
                return False
            
        def remove_duplicated(self, anyList: list) -> list:

            cleaned_list = [dict.fromkeys(anyList)]

            return cleaned_list
        
    http_proxies = []
    socks4_proxies = []
    socks5_proxies = []
    errors = []

    def save_proxy(proxy_proxy, proxy_type):

        with open(f'{proxy_type}.txt', 'a', encoding='utf8') as f:

            f.writelines([proxy_proxy, '\n'])

        return True
    
    def checker(proxy: str):
        red = Fore.RED
        green = Fore.GREEN
        lblue = Fore.LIGHTBLUE_EX
        http_checker = HttpProxyChecker(proxy, 10).start_checker()
        socks4_checker = Socks4ProxyChecker(proxy, 10).start_checker()
        socks5_checker = Socks5ProxyChecker(proxy, 10).start_checker()

        if http_checker:
            http_proxies.append(proxy)
            result_Widget.insert(END, proxy + '\n')
            save_proxy(proxy, 'http')
        elif socks4_checker:
            socks4_proxies.append(proxy)
            result_Widget.insert(END, proxy + '\n')
            save_proxy(proxy, 'socks4')
        elif socks5_checker:
            socks5_proxies.append(proxy)
            result_Widget.insert(END, proxy + '\n')
            save_proxy(proxy, 'socks5')
        else:
            errors.append(proxy)

        
    if __name__ == '__main__':

        red = Fore.RED
        green = Fore.GREEN
        white = Fore.WHITE
        lblue = Fore.LIGHTBLUE_EX

        get_prx.config(state='disabled')
        load_prx_btn.config(state='disabled')
        save_prx_btn.config(state='disabled')
        check_prx_btn.config(state='disabled')

        threads = []

        text = result_Widget.get('1.0', END)

        proxies_list = text.split('\n')

        result_Widget.delete('1.0', END)
        
        for proxy in proxies_list:
            th = Thread(target=checker, args=(proxy,))
            th.start()
            threads.append(th)
            sleep(0.03)

        for thread in threads:
            thread.join()
        
        h = len(http_proxies)
        s4 = len(socks4_proxies)
        s5 = len(socks5_proxies)

        total_proxies = h + s4 + s5

        messagebox.showinfo(title='Proxy Checker', message=f'{total_proxies} Proxies Are Working')

        get_prx.config(state='active')
        load_prx_btn.config(state='active')
        save_prx_btn.config(state='active')
        check_prx_btn.config(state='active')

def update_widget(textobj, text):

    textobj.delete('1.0', END)

    textobj.insert(END, text + '\n')
    
def system_repair():

    update_widget(system_widget, 'Repairing... ')

    repair_disk_btn.config(state='disabled')

    repair_sys_btn.config(state='disabled')
    
    proc = subprocess.Popen('sfc /scannow', shell=True)

    out, err = proc.communicate()

    proc = str(proc)

    repair_disk_btn.config(state='active')

    repair_sys_btn.config(state='active')

    if '0' in proc:

        system_widget.delete('1.0', END)

        system_widget.insert(END, 'System Repaired Successfully.' + '\n\n' + 'Did not find any integrity violations.' + '\n')
    
    else:

        update_widget(system_widget, f'Error ==> {proc}')

    return None


def disk_repair():

    update_widget(system_widget, 'Repairing... ')

    repair_disk_btn.config(state='disabled')

    repair_sys_btn.config(state='disabled')

    proc = subprocess.Popen('chkdsk /f /r /x', shell=True)

    out, err = proc.communicate()

    proc = str(proc)

    repair_disk_btn.config(state='active')

    repair_sys_btn.config(state='active')
    
    if '0' in proc:

        system_widget.delete('1.0', END)

        system_widget.insert(END, 'Disk Repaired Successfully.' + '\n')
    
    else:

        update_widget(system_widget, f'Error ==> {proc}')

    return None



def network_optimization():

    def find_adapter_registry_key(tr_name):

        res = subprocess.check_output('reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}', shell=True)


        devices = re.findall(r'HKEY_LOCAL_MACHINE\\.+',res.decode().strip())

        for device in devices[1:]:

            res = subprocess.check_output(f'reg query {device}', shell=True).decode().strip()

            if tr_name in res:

                return device




    def get_transport_name():
        res = subprocess.check_output('getmac', shell=True).decode().strip()
        return re.search(r'{[(\d|\s)].+}', res).group()



    def find_high_value(device):

        res = subprocess.check_output(f'reg query {device}\\Ndi\params\*SpeedDuplex\enum', shell=True)

        decoded_res = res.decode().strip()

        key = re.search(r'HKEY_LOCAL_MACHINE\\.+', decoded_res).group()

        clean_res = decoded_res.strip(key)

        final_res = clean_res.strip()

        return re.findall(r'\d+', final_res)


    def change_device_properties(device: str, spd: str):

        res = subprocess.check_output(f'reg add {device} /v *SpeedDuplex /t REG_SZ /d {spd} /f && reg add {device} /v *TCPChecksumOffloadIPv4 /t REG_SZ /d 3 /f && reg add {device} /v *TCPChecksumOffloadIPv6 /t REG_SZ /d 3 /f && reg add {device} /v *UDPChecksumOffloadIPv4 /t REG_SZ /d 3 /f && reg add {device} /v *UDPChecksumOffloadIPv6 /t REG_SZ /d 3 /f && reg add {device} /v WolShutdownLinkSpeed /t REG_SZ /d 2 /f', shell=True)

        time.sleep(1.5) 

        network_optimizer.insert(END, f'{res.decode()}\n[console]: The Progress Has Been Done !\n')


    if __name__ == '__main__':

        ntwrk_btn.config(state='disabled')

        device = find_adapter_registry_key(get_transport_name())

        values = find_high_value(device)

        values = list(dict.fromkeys(values))

        new_list = [int(i) for i in values]

        new_list.sort()

        highest_value = new_list[-1]

        change_device_properties(device, highest_value)

        time.sleep(1)

        ntwrk_btn.config(state='active')

        exit(0)


def clean():

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
                clean_widget.insert(END, f'\nc:/users/{user}/appdata/Local/Temp\n______________________\n')
                state = subprocess.check_output('rmdir /s /Q Temp', shell=True, stderr=subprocess.STDOUT).decode()
                if 'Access is denied.' in state:
                    clean_widget.insert(END, f'\n[+] Cleaner is Finished\n')
                    break
                clean_widget.insert(END, f'\n[+] Cleaner is Finished\n')
                break
            elif x == 2:
                temp = False
                pre = True
                temp2 = False
                x = x - 1
                os.chdir('c:/Windows/Prefetch')
                clean_widget.insert(END, f'\nc:/Windows/Prefetch\n______________________\n')

            elif x == 3:
                temp = True
                pre = False
                temp2 = False
                x = x - 1
                os.chdir('c:/Windows/Temp')
                clean_widget.insert(END, f'\nc:/Windows/Temp\n______________________\n')
                
            elif x <= 0:
                exit(0)

            files_list = os.listdir()
            

            for file in files_list:

                not_empty_folders = []

                try:

                    state = subprocess.check_output(f'rmdir {file} /s /Q', shell=True, stderr=subprocess.STDOUT).decode()


                    clean_widget.insert(END, f'Folder Deleted --> {file}\n')

                    deleted_files.append(file)

                except subprocess.CalledProcessError as e:

                        if '267' in str(e):

                            state = subprocess.check_output(f'del {file}', shell=True, stderr=subprocess.STDOUT).decode()

                            clean_widget.insert(END, f'File Deleted --> {file}\n')

                            deleted_files.append(file)

                        elif '145' in str(e):

                            try:

                                os.chdir(file)

                                not_empty_folders.append(file)

                                for file in os.listdir():

                                    if os.path.isdir(file):

                                        state = subprocess.check_output(f'rmdir {file} /s /Q', shell=True, stderr=subprocess.STDOUT).decode()

                                        clean_widget.insert(END, f'Folder Deleted --> {file}\n')

                                        deleted_files.append(file)

                                    else:    
                                        state = subprocess.check_output(f'del {file}', shell=True, stderr=subprocess.STDOUT).decode()

                                        clean_widget.insert(END, f'File Deleted --> {file}\n')

                                        deleted_files.append(file)
                            
                                if temp:
                                    os.chdir('c:/Windows/Temp')
                                elif pre:
                                    os.chdir('c:/Windows/prefetch')
                                elif temp2:
                                    os.chdir(f'c:/users/{user}/appdata/Local/')
                                    
                                state = subprocess.check_output(f'rmdir {not_empty_folders[0]} /s /Q', shell=True, stderr=subprocess.STDOUT).decode()

                                clean_widget.insert(END, f'Folder Deleted --> {not_empty_folders[0]}\n')

                                deleted_files.append(not_empty_folders[0])

                            except:
                                pass

        return len(deleted_files)

    if __name__ == '__main__':


        current_username = os.getlogin()


        files_deleted = cleaner(current_username)


        clean_widget.insert(END,f'[+] Files Deleted : {files_deleted}')


def r6_server_(region_):

    def ServerChanger(region):


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

            
        try:

            a, old, new = ServerChanger(region=region_)

            if a:

                r6_.insert(END,f'\n[+] New Server: {new}\n\n[-] Old Server: {old}\n\n')

        except:

            r6_.insert(f'\n[x] Please Type One Of These Numbers 1, 2, 3\n')

class image_resizer:

    def __init__(self, width, height) -> None:

        self.height = height
        self.width = width

    def read_image_data(self, img_path):

        image = Image.open(img_path, mode='r')

        return image
    
    def resize(self, img_path):

        img_data = self.read_image_data(img_path)

        resized_img = img_data.resize((self.width, self.height))

        image = ImageTk.PhotoImage(resized_img)

        return image


def idm_trial():

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

            return True
        
        except:

            return False
        
    if __name__ == '__main__':

        idm_btn.config(state='disabled')

        hku = winreg.HKEY_USERS

        sub_key = find_registry_sub_key(hku)

        if sub_key:

            if delete_IDM_registry_key(hku, sub_key):

                idm_widget.insert(END, '[+] IDM Trial Reset Done!\n')

                idm_widget.insert(END, '[+] IDM Trial Status: 30 Days\n')
                
                idm_widget.insert(END, '[+] Coded By: Apkaless The Eagle\n')

                idm_widget.insert(END, '[+] Instagram: Apkaless\n')

                idm_widget.insert(END, '[+] Github: github.com/Apkaless\n')

            else:
                idm_widget.insert(END, '[-] Unknown Error!\n')

        else:
            idm_widget.insert(END, 'No Key Was Found!\n')
        
        idm_btn.config(state='active')

    return None

def combo_editor() -> str:

    filepath = filedialog.askopenfilename()

    with open(filepath, 'r', encoding='utf8') as f:

        file_data = f.read().splitlines()

        with open('clean_combolist.txt', 'w') as res:

            for combo in file_data:

                combo = combo.split('|')[0].strip()

                res.writelines([combo, '\n'])

                combo_widget.insert(END, combo + '\n')

            res.close()

    return True

def save_combo():

    text = combo_widget.get('1.0', END)

    try:

        file = filedialog.asksaveasfile(mode='w', filetypes=[('Text File', '.txt')], defaultextension='.txt')

        text = combo_widget.get('1.0', END)

        file.write(text)

        file.close()
    
    except:
        pass

resizer = image_resizer(15, 15)

window = Tk()

window.geometry('1920x1080')

window.title('Text Editor')

programIcon = PhotoImage(file='app.png')

window.iconphoto(True, programIcon)

window.resizable(width=False, height=True)

style = ttk.Style()
 
style.theme_create('pastel', settings={
    ".": {
        "configure": {
            "background": '#ffffcc', # All except tabs
            "font": 'red'
        }
    },
    "TNotebook": {
        "configure": {
            "background":'black', # Your margin color
            "tabmargins": [2, 5, 0, 0], # margins: left, top, right, separator
        }
    },
    "TNotebook.Tab": {
        "configure": {
            "background": 'green', # tab color when not selected
            "padding": [10, 2], # [space between text and horizontal tab-button border, space between text and vertical tab_button border]
            "font":"black"
        },
        "map": {
            "background": [("selected", '#ccffff')], # Tab color when selected
            "expand": [("selected", [1, 1, 1, 0])] # text margins
        }
    }
})
 
style.theme_use('pastel')

notebook = ttk.Notebook(window, style='TNotebook')

tab1 = Frame(notebook, height=1080, width=1920)

tab2 = Frame(notebook, height=1080, width=1920, bg='black', pady=10, padx=10)

tab3 = Frame(notebook, height=1080, width=1920, bg='black', pady=10, padx=10)

about_tab = Frame(notebook, height=1080, width=1920, bg='black')

notebook.add(tab1, text='Text Editor')

notebook.add(tab2, text='Tools 1')

notebook.add(tab3, text='Tools 2')

notebook.add(about_tab, text='About')

notebook.pack()

about_Frame = Frame(about_tab, background='black', width=500, height=500)

about_Frame.place(y=350, x=725)

nlabel = Label(about_Frame, text='Coded By Apkaless.\n\nFrom IRAQ', fg='Green', bg='black', font=('Arial', 10))

nlabel.place(x=190, y=200)

nlabe2 = Label(about_Frame, text='Instagram: Apkaless\n\nGithub: https://github.com/apkaless', fg='Green', bg='black', font=('Arial', 10))

nlabe2.place(x=150, y=280)

nlabe3 = Label(about_Frame, text='Enjoy (:', fg='Green', bg='black', font=('Arial', 10))

nlabe3.place(y=450, x=225)

apkaless_pic = ImageTk.PhotoImage(Image.open('apkaless.jpg'))

apkaless_label = Label(about_Frame, image=apkaless_pic, compound='center')

apkaless_label.pack()

apkaless_label.place(anchor='center', relx=0.5, rely=0.2)

scroll = Scrollbar(window, orient='vertical')

scroll.pack(side='right', fill='y')

canvas = Canvas(tab2, background='black', bd=1, highlightbackground='black', highlightcolor='black',highlightthickness=2, relief='flat')

canvas.pack(fill='both', expand=True)

canvas_scrollbar = Scrollbar(canvas, command=canvas.yview)

canvas_scrollbar.pack(side='right', fill='y')

canvas.config(yscrollcommand=canvas_scrollbar.set)


openfile = resizer.resize('icons/folder.png')

saveimg = resizer.resize('icons/diskette.png')

extimg = resizer.resize('icons/switch.png')

redoimg = resizer.resize('icons/refresh-arrow.png')

undoimg = resizer.resize('icons/rotate-arrow.png')

copyimg = resizer.resize('icons/copy.png')

cutimg = resizer.resize('icons/scissors.png')

pasteimg = resizer.resize('icons/paste.png')

findimg = resizer.resize('icons/search.png')

menubar = Menu(window, background='#ffcc99', foreground='black')

FileMenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='File', menu=FileMenu)

FileMenu.add_command(label='Open', command=open_file, image=openfile, compound='left', accelerator='CTRL + N')

FileMenu.add_command(label='Save As', command=save_file, image=saveimg, compound='left', accelerator='CTRL + S')

FileMenu.add_separator()

FileMenu.add_command(label='Exit', image=extimg, compound='left', command=window.quit)

window.bind_all('<Control-n>', open_file)

window.bind_all('<Control-N>', open_file)

window.bind_all('<Control-s>', save_file)

window.bind_all('<Control-S>', save_file)

EditMenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='Edit', menu=EditMenu)

EditMenu.add_command(label='Undo', command=undo, image=undoimg, compound='left')

EditMenu.add_command(label='Redo', command=redo, image=redoimg, compound='left')

EditMenu.add_separator()

EditMenu.add_command(label='Cut', command=cut, image=cutimg, compound='left')

EditMenu.add_command(label='Copy', command=copy, image=copyimg, compound='left')

EditMenu.add_command(label='Paste', command=paste, image=pasteimg, compound='left')

EditMenu.add_separator()

EditMenu.add_command(label='Find', command=find, image=findimg, compound='left')

SettingsMenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='Settings', menu=SettingsMenu)

Themes = Menu(SettingsMenu, tearoff=0)

SettingsMenu.add_cascade(label='Themes', menu=Themes)

Themes.add_command(label='Theme 1', command=theme1)

Themes.add_command(label='Theme 2', command=theme2)

Themes.add_command(label='Theme 3', command=theme3)

textWidget = Text(tab1, pady=10, padx=10)

textWidget.config(font=('Arial', 12), fg='#69C913', undo=True, yscrollcommand=scroll.set, height=1080, width=1920, bg='black', insertbackground='#69C913')

textWidget.pack(fill='both')

scroll.config(command=textWidget.yview, bg='black')

fr = Frame(canvas, bd=5, relief='flat', highlightthickness=2, highlightcolor='green', highlightbackground='black', pady=10, bg='black')

fr2 = Frame(fr, bd=5, relief='flat', pady=10, bg='black')

fr2.pack(side='bottom')

fr.place(x=0,y=0)

fr3 = Frame(canvas, bg='black', width=900, height=500, bd=5, relief='flat', highlightbackground='black', highlightcolor='green', highlightthickness=2, padx=10, pady=10)

fr3.pack(side='right')

fr3.place(y=0, x=1260)

fr4 = Frame(fr3, bd=5, relief='flat', pady=10, bg='black')

fr4.pack(side='bottom')

fr5 = Frame(canvas, bg='black', width=768, height=500, bd=5, relief='flat', highlightbackground='black', highlightcolor='green', highlightthickness=2, padx=10, pady=10)

fr5.pack(side='left')

fr5.place(y=600, x=0)

fr6 = Frame(fr5, bd=5, relief='flat', pady=10, bg='black')

fr6.pack(side='bottom')

fr7 = Frame(canvas, bg='black', width=768, height=500, bd=5, relief='flat', highlightbackground='black', highlightcolor='green', highlightthickness=2, padx=10, pady=10)

fr7.place(x=1260, y=600)

fr8 = Frame(fr7, bg='black', width=768, height=500, bd=5, relief='flat', highlightbackground='black', highlightcolor='green', highlightthickness=2, padx=10, pady=10)

fr8.pack(side='bottom')

fr9 = Frame(tab3, bg='black', bd=5, highlightbackground='cyan', highlightcolor='green', highlightthickness=2, height=500, width=578, padx=10, pady=10)

fr9.pack(side='left')

fr9.place(x=0, y=0)

fr10 = Frame(fr9, bg='black', bd=5, relief='flat', padx=10, pady=10)

fr10.pack(side='bottom')

fr11 = Frame(tab3, bg='black', bd=5, highlightbackground='cyan', highlightcolor='green', highlightthickness=2, height=778, width=400, padx=10, pady=10)

fr12 = Frame(fr11, bg='black', bd=5, relief='flat', height=200, width=400, highlightbackground='green', highlightcolor='red', highlightthickness=2)

fr12.place(x=0, y=662, relx=0.5, anchor='center')

fr11.place(x=1500, y=0)

combo_widget = Text(fr11, font=('Barlow', 12))

combo_widget.config(bd=5, relief='flat', highlightcolor='green', highlightbackground='cyan', highlightthickness=1, bg='black', fg='green', insertbackground='green')

combo_widget.place(width=370, height=500)

combo_widget.bind('<Key>', lambda e: 'break')

combo_btn = Button(fr12, text='Edit Combo', width=15, height=2, bd=5, relief='flat', highlightcolor='cyan', highlightbackground='cyan', highlightthickness=1, bg='black', fg='green', activebackground='black', activeforeground='red')

combo_btn.config(command=Thread(target=combo_editor).start)

combo_btn.place(relx=0.5, rely=0.5, anchor='center')

save_combo_btn = Button(fr12, text='Save Combo', width=15, height=2, bd=5, relief='flat', highlightcolor='cyan', highlightbackground='cyan', highlightthickness=1, bg='black', fg='green', activebackground='black', activeforeground='red')

save_combo_btn.config(command=Thread(target=save_combo).start)

save_combo_btn.place(relx=0.5, rely=0.2, anchor='center')

idm_widget = Text(fr9, font=('Barlow', 12))

idm_widget.config(bd=5, relief='flat', highlightcolor='green', highlightbackground='cyan', highlightthickness=1, bg='black', fg='green', insertbackground='green')

idm_widget.pack(side='left')

idm_widget.bind('<Key>', lambda e: 'break')

idm_widget.bind('<FocusIn>', lambda e: (r6_btn_1.config(state='disabled'), r6_btn_2.config(state='disabled'), r6_btn_3.config(state='disabled')))

idm_widget.bind('<FocusOut>', lambda e: (r6_btn_1.config(state='active'), r6_btn_2.config(state='active'), r6_btn_3.config(state='active')))

idm_btn = Button(fr10, text='Reset IDM Trial', width=15, height=2)

idm_btn.config(bd=5, relief='flat', highlightcolor='cyan', highlightbackground='cyan', highlightthickness=1, bg='black', fg='green', activebackground='black', activeforeground='red', command=Thread(target=idm_trial).start)

idm_btn.pack(side='bottom', pady=10)

r6_ = Text(fr9, font=('Barlow', 12))

r6_.config(bd=5, relief='flat', highlightcolor='green', highlightbackground='cyan', highlightthickness=1, bg='black', fg='green', insertbackground='green')

r6_.pack(side='right')

r6_.bind('<Key>', lambda e: 'break')

r6_.bind('<FocusIn>', lambda e: (idm_btn.config(state='disabled')))

r6_.bind('<FocusOut>', lambda e: (idm_btn.config(state='active')))

r6_btn_1 = Button(fr10, text='EU Server', width=15, height=2)

r6_btn_1.config(bd=5, relief='flat', highlightcolor='cyan', highlightbackground='cyan', highlightthickness=1, bg='black', fg='green', activebackground='black', activeforeground='red', command=Thread(target=r6_server_, args=('2', )).start)

r6_btn_1.pack(side='bottom', pady=10)

r6_btn_2 = Button(fr10, text='Middle East Server', width=15, height=2)

r6_btn_2.config(bd=5, relief='flat', highlightcolor='cyan', highlightbackground='cyan', highlightthickness=1, bg='black', fg='green', activebackground='black', activeforeground='red', command=Thread(target=r6_server_, args=('1', )).start)

r6_btn_2.pack(side='bottom', pady=10)

r6_btn_3 = Button(fr10, text='Default', width=15, height=2)

r6_btn_3.config(bd=5, relief='flat', highlightcolor='cyan', highlightbackground='cyan', highlightthickness=1, bg='black', fg='green', activebackground='black', activeforeground='red', command=Thread(target=r6_server_, args=('3', )).start)

r6_btn_3.pack(side='bottom', pady=10)

result_Widget = Text(fr, font=('Barlow', 12))

get_prx = Button(fr2, text='Get Proxies', width=10, height=2, command=Thread(target=get_proxies).start)

get_prx.config(bd=5, relief='flat', highlightcolor='cyan', highlightbackground='cyan', highlightthickness=1, bg='black', fg='green', activebackground='black', activeforeground='red')

get_prx.pack(padx=10, pady=10, side='left')

load_prx_btn = Button(fr2, text='Load Proxies', width=10, height=2, command=load_proxy)

load_prx_btn.config(bd=5, relief='flat', highlightcolor='cyan', highlightbackground='cyan', highlightthickness=1, bg='black', fg='green', activebackground='black', activeforeground='red')

load_prx_btn.pack(padx=10, pady=10, side='left')

save_prx_btn = Button(fr2, text='Save Proxies', width=10, height=2, command=save_prx)

save_prx_btn.config(bd=5, relief='flat', highlightcolor='cyan', highlightbackground='cyan', highlightthickness=1, bg='black', fg='green', activebackground='black', activeforeground='red')

save_prx_btn.pack(padx=10, pady=10, side='left')

check_prx_btn = Button(fr2, text='Check Proxies', width=10, height=2, command=Thread(target=check_prx).start)

check_prx_btn.config(bd=5, relief='flat', highlightcolor='cyan', highlightbackground='cyan', highlightthickness=1, bg='black', fg='green', activebackground='black', activeforeground='red')

check_prx_btn.pack(padx=10, pady=10, side='left')

scroll2 = Scrollbar(fr)

result_Widget.config(bd=5, relief='flat', highlightcolor='green', highlightbackground='cyan', highlightthickness=1, bg='black', fg='green', insertbackground='green', yscrollcommand=scroll2.set)

scroll2.config(command=result_Widget.yview)

scroll2.pack(fill='y', side='right')

result_Widget.pack(side='left')

result_Widget.bind('<Key>', lambda e: 'break')

system_widget = Text(fr3, bg='black', bd=5, relief='flat', highlightbackground='cyan', highlightthickness=1, highlightcolor='green', font=('Barlow', 10), fg='green', insertbackground='green')

system_widget.pack()

repair_sys_btn = Button(fr4, text='System Repair', background='black', fg='green', activeforeground='cyan', activebackground='black', bd=5, relief='flat', highlightcolor='cyan', highlightbackground='cyan', highlightthickness=2)

repair_sys_btn.config(command=Thread(target=system_repair).start)

repair_sys_btn.pack(side='left')

repair_disk_btn = Button(fr4, text='Disk Repair', background='black', fg='green', activeforeground='cyan', activebackground='black', bd=5, relief='flat', highlightcolor='cyan', highlightbackground='cyan', highlightthickness=2)

repair_disk_btn.config(command=Thread(target=disk_repair).start)

repair_disk_btn.pack(side='left', padx=10)

print(system_widget.bind('<Key>', lambda e: 'break'))

network_optimizer = Text(fr5, bg='black', bd=5, relief='flat', highlightbackground='cyan', highlightthickness=1, highlightcolor='green', font=('Barlow', 10), fg='green', insertbackground='green')

network_optimizer.pack()

ntwrk_btn = Button(fr5, text='Network Optimizer', width=15, height=2)

ntwrk_btn.config(bd=5, relief='flat', highlightcolor='cyan', highlightbackground='cyan', highlightthickness=1, bg='black', fg='green', activebackground='black', activeforeground='red', command=Thread(target=network_optimization).start)

ntwrk_btn.pack(pady=15)

network_optimizer.bind('<Key>', lambda e: 'break')

clean_widget = Text(fr7, bg='black', bd=5, relief='flat', highlightbackground='cyan', highlightthickness=1, highlightcolor='green', font=('Barlow', 10), fg='green', insertbackground='green')

clean_widget.pack()

clean_btn = Button(fr8, text='System Cleaner', width=15, height=2)

clean_btn.config(bd=5, relief='flat', highlightcolor='cyan', highlightbackground='cyan', highlightthickness=1, bg='black', fg='green', activebackground='black', activeforeground='red', command=Thread(target=clean).start)

clean_btn.pack()

clean_widget.bind('<Key>', lambda e: 'break')

window.config(menu=menubar)

os.remove('apkaless.jpg')

os.remove('app.png')

window.mainloop()