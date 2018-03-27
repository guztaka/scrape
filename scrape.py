# coding: utf-8

import requests
from bs4 import BeautifulSoup
import csv

url = 'URL/TO/HERE'

res = requests.get(url)
data = BeautifulSoup(res.text, 'html.parser')

tables = data.findAll('table', class_='table222')  # why table222?

# csv file open
with open('kokka.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # reading tables and writing to file
    for queue in tables:
        for tr in queue.findAll('tr'):
            try:
                # print(f"リンク：{tr.a['href']}")
                # print(f"資格名：{tr.a.text}")
                # print(f"偏差値：{tr.span.text}")
                data = [tr.a['href'], tr.a.text, tr.span.text]
                writer.writerow(data)
            except:
                pass

    f.close()
