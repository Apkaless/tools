from urllib import parse
from bs4 import BeautifulSoup as bs
import requests
import re
import json
from urllib import parse
from cloudscraper import CloudScraper
import base64



# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
# }


# res = requests.get('https://proxyhub.me/', headers=headers, cookies={'page': '4', 'anonymity': 'all'})

# res = json.dumps(res.text)

# sp = bs(res, 'html.parser')

# table = sp.find('table')

# trs = table.find_all('tr')


# for tds in trs[1:]:

#     ip = tds.find_all('td')[0].getText()

#     port = tds.find_all('td')[1].getText()

#     print(ip + ':' + port)




# ip = tds.find_all('td')[0].getText()

# port = tds.find_all('td')[1].getText()

# print(ip + ':' + port)


# url = 'https://www.proxyscan.io/api/proxy?last_check=9800&country=fr,us,ru&uptime=50&ping=500&limit=20&type=socks4,socks5,http,https'

# res = requests.get(url)

# for jd in res.json():

#     print(jd['Port'])




combo = open(input('combo list: '), 'r').read().splitlines()

for comb in combo:
    
    comb = comb.split('|')

    com = comb[0]

    cleaned_combo = com.strip()

    with open('cleaned_combo.txt', 'a') as f:
        f.writelines([cleaned_combo, '\n'])