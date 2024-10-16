import requests
from bs4 import BeautifulSoup

HOST = 'https://stopgame.ru'
URL = 'https://stopgame.ru/news'
HEADERS = {
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36'
}

def get_html(url, params =''):
    r = requests.get(url, headers = HEADERS, params = params)
    return r.text
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div',class_='_card_11mk8_1').find('a').get('href')
    return HOST+div

