#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
from selenium.webdriver.common import by
import os
from colorama import Fore

def channelChanger(headers, hwtok, driver, s):

    while True:

        os.system('cls')
        channel = input(f'\n{blue}[?] {white}What Channel Number You Would Like To Change To >>> ')

        if channel != '':
            break
        else:
            continue

    payload = {
                'y.Channel': f'{channel.strip()}',
                'y.AutoChannelEnable': '0',
                'y.X_HW_HT20': '1',
                'y.RegulatoryDomain': 'IQ',
                'y.TransmitPower': '100',
                'y.X_HW_Standard': '11bgn',
                'x.DtimPeriod': '1',
                'x.BeaconPeriod': '100',
                'x.RTSThreshold': '2346',
                'x.FragThreshold': '2346',
                'x.X_HW_Token': f'{hwtok}',
            }


    changeChannel = s.post('http://192.168.100.1/html/network/set.cgi?x=InternetGatewayDevice.LANDevice.1.WLANConfiguration.1.X_HW_AdvanceConf&y=InternetGatewayDevice.LANDevice.1.WLANConfiguration.1&RequestFile=html/network/wlan.asp', data=payload, headers=headers)
    
    if changeChannel.text:
        print(f'\n{blue}[+] {green}Channel Has Been Changed To >>> {white}{channel}')
        time.sleep(2)
        try:
            driver.close()
        except:
            exit(0)

    else:
        exit(0)


def blockClients_(headers, hwtok, driver, s):

    while True:
        os.system('cls') 

        ask = input('''Choose Option: 
                        
                    1) Block 

                    2) Unblock 
                        
                    [option]==> ''')
        
        if ask.strip() == '1':
            val = 1
        elif ask.strip() == '2':
            val = 0
        else:
            continue

        break

    url = 'http://192.168.100.1/html/security/set.cgi?x=InternetGatewayDevice.X_HW_Security&RequestFile=html/security/macfilter.asp'

    payload = {
        'x.MacFilterRight': f'{val}',
        'x.X_HW_Token': f'{hwtok}'
    }

    go = s.post(url, data=payload, headers=headers)

    if go.text:
        if val == 1:
        
            print(f'\n{green}[+] {white}All Clients Has Been Blocked.\n')
            time.sleep(2)
        else:
            print(f'\n{green}[+] {white}All Clients Has Been UnBlocked.\n')
        try:
            driver.close()
        except:
            exit(0)
    else:
        print(f'\n{red}[-] {white}Something Went Wrong.\n')
        time.sleep(2)
        exit(0)

def router():

    while True:
        os.system('cls')
        
        ask = input('''Choose Option: 
                    
                    1) Change Channel

                    2) Block/Unblock Clients
                    
                    [option]==> ''')
        
        channel_op = False

        blockClients = False

        if ask.strip() == '1':
            channel_op = True
        elif ask.strip() == '2':
            blockClients = True
        else:
            os.system('cls')
            continue

        break

    with requests.Session() as s:

        option = webdriver.ChromeOptions()

        option.add_argument('--no-sandbox')
        option.add_argument('--headless')
        option.add_experimental_option('detach', True)

        driver = webdriver.Chrome(options=option)

        while True:

            driver.get('http://192.168.100.1')

            os.system('cls')

            print(f'\n{green}[+] {blue}Please Wait...\n')

            try:

                time.sleep(1)
                driver.find_element(by.By.ID, 'txt_Username').send_keys('telecomadmin')
                time.sleep(1)
                driver.find_element(by.By.ID, 'txt_Password').send_keys('admintelecom')
                time.sleep(1)
                driver.find_element(by.By.ID, 'button').click()
                time.sleep(1)
                sid = driver.get_cookie('Cookie')['value']

                if sid:
                    break

                else:
                    continue

            except:
                continue

        headers2 = {
            'Referer': 'http://192.168.100.1/',
            'Cookie': f'Cookie={sid}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

        headers3 = {
            'Referer': 'http://192.168.100.1/html/network/set.cgi?',
            'Cookie': f'Cookie={sid}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

        headers4 = {
            'Referer': 'http://192.168.100.1/html/security/macfilter.asp',
            'Cookie': f'Cookie={sid}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        
        res2 = s.get('http://192.168.100.1/html/network/wlan.asp', headers=headers2)

        hwonttoken = bs(res2.text, 'html.parser').find(name='input', attrs={'id': 'hwonttoken'}).attrs['value']

        if hwonttoken:

            if channel_op:
                channelChanger(headers=headers3, hwtok=hwonttoken, driver=driver, s=s)
            else:
                blockClients_(headers=headers4, hwtok=hwonttoken, driver=driver, s=s)
        else:
            print(f'\n{red}[-] Token Not Found.\n')

if __name__ == '__main__':
    blue = Fore.BLUE
    green = Fore.GREEN
    white = Fore.WHITE
    red = Fore.RED

    router()