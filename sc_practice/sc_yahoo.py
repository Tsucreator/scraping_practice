import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re 


for i in range(1, 41):
    target_url = 'https://news.yahoo.co.jp/flash?p={}'.format(str(i))
    res = requests.get(target_url)
    soup = BeautifulSoup(res.content, 'html5lib' )
    parent = soup.find('div', 'newsFeed')
    print(parent)
    targets = parent.findAll('div', 'newsFeed_item_title')

    for target in targets:
        print(target.text)
