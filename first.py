import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)

arr = []
for child in root.iter('item'):
    if child.tag == 'item':
        arr.append({'pubDate': child.find('pubDate').text, 'title': child.find('title').text})

json.dump(arr, open('news.json', 'w', encoding="utf-8"), ensure_ascii=False)