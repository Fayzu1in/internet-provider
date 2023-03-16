import requests

import json 
import re 
from bs4 import BeautifulSoup as bs 


def get_data(url):
    arr = []
    response = requests.get(url)
    parsed = bs(response.text, 'html.parser')
    div = parsed.find_all('div', {'class': 'calc-card-item'})
    for i in div:
        title = i.find('div', {'class': 'calc-card-item-head'}).text
        name = i.find('div', {'class': 'calc-card-item-usluga'}).find('span').text
        speed = i.find_all('div', {'class': 'calc-card-item-circle'})
        night, day = speed[0].text, speed[-1].text
        night = re.sub('\n', '', night)
        if night != 'ДОГОВОРНАЯ' and night != 'БЕЗЛИМИТНЫЙ':
            night = night[1:]
        night = re.sub('мбит', ' Mbit/s', night)
        night = re.sub('МБит', ' Mbit/s', night)
        night = re.sub('кбит', ' Kbit/s', night)
        day = re.sub('\n', '', day)
        if day != 'ДОГОВОРНАЯ' and day != 'БЕЗЛИМИТНЫЙ':
            day = day[1:]
        day = re.sub('мбит', ' Mbit/s', day)
        day = re.sub('МБит', ' Mbit/s', day)
        day = re.sub('кбит', ' Kbit/s', day)
        price = i.find('div', {'class': 'calc-card-item-price-inner'}).text
        price = re.sub('суммес', '', price)
        price = re.sub('  ', '', price)
        price = re.sub('[.]', ' ', price)
        price = re.sub(r'[\r\n]', '', price)
        obj = {
            "name": name,
            'info': {
            'title': title,
            'speed': day,
            'price': price,
            'night': night,
            'more': ''
            }
        }
        arr.append(obj)
        # for j in speed:
        #     row = j.find_all('div', {'class': 'row'})
        #     print(row)
        #     print('-------------------------------')
    return arr 


istv = get_data('https://istv.uz/internet/tarifs/')
physic = istv[:20]

for i in physic:
    i['type'] = 'physic'

yuridic = istv[20:]

for i in yuridic:
    i['type'] = 'yuridic'

istv = physic + yuridic
print(istv)

with open('json/istv-plans.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(istv, indent=3,  ensure_ascii=False))


# with open('json/istv-plans.json', 'r') as file:
#     istv = json.load(file )
