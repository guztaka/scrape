# coding: utf-8

import requests
import csv
import urllib.parse as parse
from sys import argv
from bs4 import BeautifulSoup


url = argv[1]

res = requests.get(url)
data = BeautifulSoup(res.text, 'html.parser')

tables = data.findAll('table', class_='table222')  # why table222?

# csv file open
with open(argv[2], 'w', newline='') as f:
    writer = csv.writer(f)

    # reading tables and writing to file
    for queue in tables:
        for tr in queue.findAll('tr'):
            try:
                surl = parse.urlparse(tr.a['href'])
                eurl = parse.quote(''.join(surl[2:3]))
                data = ['://'.join(surl[0:2]) + eurl, tr.a.text, tr.span.text]
                writer.writerow(data)
            except:
                pass

    f.close()
