from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re
import time
import requests

'''
https://store.steampowered.com/app
https://store.steampowered.com/apphoverpublic/
'''

class SteamUserGamesFinder:

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def get_html(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path='chrome-win/chrome.exe' ,headless=False, slow_mo=100, timeout=300)
            page = browser.new_page()
            page.goto('https://steamcommunity.com/login/home/?goto=')
            time.sleep(2)
            page.fill(
                '#responsive_page_template_content > div.page_content > div:nth-child(1) > div > div > div > div._3XCnc4SuTz8V8-jXVwkt_s > div > form > div:nth-child(1) > input',
                self.user)
            page.fill(
                '#responsive_page_template_content > div.page_content > div:nth-child(1) > div > div > div > div._3XCnc4SuTz8V8-jXVwkt_s > div > form > div:nth-child(2) > input',
                self.password)
            time.sleep(1)
            #login button
            page.click(
                '#responsive_page_template_content > div.page_content > div:nth-child(1) > div > div > div > div._3XCnc4SuTz8V8-jXVwkt_s > div > form > div._16fbihk6Bi9CXuksG7_tLt > button')
            time.sleep(10)
            page.reload()
            time.sleep(2)
            print(page.url)
            page.click('#responsive_page_template_content > div.no_header.profile_page > div.profile_content > div > div.profile_rightcol > div.responsive_count_link_area > div.profile_item_links > div:nth-child(1) > a')
            time.sleep(2)
            return page.content()


    def get_games(self, html_content):
        soup = BeautifulSoup(html_content, 'lxml')
        games_links = soup.find_all('a', href=re.compile('^https://store.steampowered.com/app'))
        if len(games_links) > 0:
            return games_links
        else:
            return False


    def getGame_Info(self, id):
        url = 'https://store.steampowered.com/apphoverpublic/' + id
        s = requests.Session()
        response = s.get(url)
        if not response.ok:
            return False
        else:
            try:

                soup = BeautifulSoup(response.content, 'lxml')
                game_name = soup.find('h4', class_='hover_title').text
                return game_name
            except:
                return None


    def remove_duplicates(self, games_list):
        clean_list = list(dict.fromkeys(games_list, None))
        return clean_list


    def Find(self):
        game_links = []
        all_games = []
        htmp_content = self.get_html()
        games = self.get_games(htmp_content)
        if games:
            for game_link in games:
                game_links.append(game_link.get('href'))

            clean_games_links = self.remove_duplicates(game_links)

            for new_game_link in clean_games_links:
                id = new_game_link.split('/')[-1]
                game_name = self.getGame_Info(id)
                if game_name:
                    all_games.append(game_name)
            return all_games
        else:
            print('No games found')



if __name__ == '__main__':
    games = SteamUserGamesFinder('j3zfacac', 'nnz8bqrxc').Find()
    print(games)