import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)

arr = []
for child in root.iter('item'):
    data = {}

    for dataPart in child:
        data[dataPart.tag] = dataPart.text

    arr.append(data)

json.dump(arr, open('news2.json', 'w', encoding="utf-8"), ensure_ascii=False)