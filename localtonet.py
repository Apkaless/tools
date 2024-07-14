import time
import requests
import cloudscraper
import playwright
import asyncio
import os
import subprocess
from pathlib import Path
from bs4 import BeautifulSoup as bs
from playwright.sync_api import sync_playwright
from colorama import Fore, init


init(convert=True)
red = Fore.RED
green = Fore.GREEN
cyan = Fore.CYAN
lb = Fore.LIGHTBLUE_EX
lc = Fore.LIGHTCYAN_EX
white = Fore.WHITE

class LOCALTONET:

    def __init__(self, api_key) -> None:
        self.api = api_key
        self.authTokUrl = 'https://localtonet.com/api/GetAuthTokens'
        self.TcpUdpCreationUrl = 'https://localtonet.com/tunnel/createtcpudp'
        self.loginUrl = 'https://localtonet.com/Identity/Account/Login'
        self.localPath = os.getcwd()
        self.headers = {
                    'accept': 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {self.api}',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
                }
        
        self.token = self.GetAuthToken()
        self.verifyToken = self.GetVerifyToken()

    def launchAppThread(self, auth):
        appPath = os.path.join(self.localPath, 'localClient')
        os.chdir(appPath)
        start_command = f'start localclient.exe authtoken {auth}'
        subprocess.check_output(start_command, shell=True)
        return True
    
    def CreateTcpUdpTunnel(self, port: str):

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True, slow_mo=50)
            context = browser.new_context()
            page = browser.new_page()
            print('🔃 Please Wait...')
            while True:
                time.sleep(1)
                try:
                    page.goto(self.loginUrl, wait_until='load')
                    break
                except:
                    continue
            time.sleep(1)
            print(f'\n{green}🔃 {cyan}Trying Logging in')
            page.fill('#Input_Email', 'sabah.hsab1234@gmail.com')
            page.fill('#Input_Password', 'Ya1122334455')
            page.click('#kt_sign_up_submit')
            time.sleep(2)
            os.system('cls')
            print(f'\n{green}[🗸] {cyan}Logged in')
            while True:
                time.sleep(1)
                try:
                    page.goto('https://localtonet.com/tunnel/tcpudp')
                    break
                except:
                    continue
            time.sleep(1)
            os.system('cls')
            try:
                page.get_by_role('button', name='Delete').click()
                time.sleep(1)
                page.get_by_role('button', name='Yes').click()
                print(f'\n{green}[🗸] {cyan}Old Tunnel Has Been Deleted To Create A New One.')
            except:
                pass
            time.sleep(2)
            os.system('cls')
            print(f'\n{green}🔃 Creating {cyan}TCP/UDP {green}Tunnel')
            page.click('#createTcpUdpForm > div.row.col-lg-9 > div:nth-child(1) > div > span > span.selection > span')
            time.sleep(1)
            page.fill('#kt_body > span.select2-container.select2-container--bootstrap5.select2-container--open > span > span.select2-search.select2-search--dropdown > input', 'tcp')
            time.sleep(1)
            page.keyboard.press('Enter')
            time.sleep(1)
            page.click('#createTcpUdpForm > div.row.col-lg-9 > div:nth-child(3) > div > span > span.selection > span')
            time.sleep(1)
            page.fill('#kt_body > span.select2-container.select2-container--bootstrap5.select2-container--open > span > span.select2-search.select2-search--dropdown > input', 'de')
            time.sleep(1)
            page.keyboard.press('Enter')
            time.sleep(1)
            page.fill('#createTcpUdpForm > div:nth-child(2) > div:nth-child(2) > div > input', port)
            time.sleep(1)
            page.click('#createTcpUdpForm > div:nth-child(2) > div:nth-child(5) > button')
            time.sleep(2)
            page.get_by_role('button', name='Start').click()
            page.wait_for_load_state(state='load')
            time.sleep(8)
            html = page.content()
            soup = bs(html, 'lxml')
            tr = soup.find('tr', class_='odd')
            tunnel_id = tr.attrs['id']
            tds = soup.find_all('td', class_='dt-center')
            for td in tds:
                try:
                    server_id = td.span.getText()
                    break
                except Exception as e:
                    continue
        
        return {'Status': 'Running', 'ID': tunnel_id, 'Server': server_id}
        
    def GetAuthToken(self):
        """
        
        Returns The Auth Token Of Localtonet Account Using API Key

        """
        s = requests.Session()

        response = s.get(self.authTokUrl, headers=self.headers)

        return response.json().get('result')[0].get('token')
    

    def GetVerifyToken(self):

        with requests.Session() as s:

            html = s.get('https://localtonet.com/tunnel/tcpudp')

            soup = bs(html.text, "lxml")

            verifyTok = soup.find(name='input', attrs=({'name': '__RequestVerificationToken'}))
            if verifyTok:
                return verifyTok.attrs['value']
            else:
                return 'Unable To Locate Verify Request Token'

