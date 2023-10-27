import requests
import cloudscraper
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
from bs4 import BeautifulSoup as bs
import undetected_chromedriver as uc
import  random_user_agent.user_agent
import random

cs = cloudscraper.create_scraper()

resp = cs.post('https://steamcommunity.com/login/getrsakey/', data={'username': 'apkaless'})


print(resp.text, '\n')
resp = json.loads(resp.text)
pub = resp['publickey_mod']
exp = resp['timestamp']

print(exp)
# print(pub)
# print(exp)
# pub = int(resp['publickey_mod'], 16)
# exp = int(resp['publickey_exp'], 16)
# print(pub)
# print(exp)

res = cs.post('https://steamcommunity.com/login/dologin/', data={'username': 'apkaless', 'password': 'apkaless22', 'rsatimestamp': f'{exp}'})

resp = json.loads(res.text)
print(resp)