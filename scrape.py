# coding: utf-8

import requests
from bs4 import BeautifulSoup

url = 'http://shikaku-fan.net/英検（実用英語技能検定）/'

res = requests.get(url)
data = BeautifulSoup(res.text, 'html.parser')
print('資格のタイトル：　' + data.select_one('#big').text)
print('資格のカテゴリ：　' + data.select_one('#main_h > div.type2').text)
print('資格の難易度：　' + data.find_all('table', {'class': 'table555'}).text)
# print('資格の難易度：　' + data.select_one('#main_h > table.table555 > tbody > tr:nth-child(1) > th:nth-child(1)').text)
