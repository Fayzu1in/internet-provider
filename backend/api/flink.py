import requests

from bs4 import BeautifulSoup as bs
import json
import datetime
import re
import os
import django



def get_plans(url):
    try:
        response = requests.get(url).text
        parsed = bs(response, 'html.parser')
        tr = parsed.find_all('tr')[1:]
        array = []
        for i in tr:
            title = i.find('td').find('strong').text
            title = re.sub(r'\r\n\t\t', '', title)
            title = re.sub(r'\xa0', ' ', title)
            speed = i.find_all('td')[2].text
            speed = re.sub(r'\r\n\t\t', '', speed)
            speed = re.sub(r'/с\r\n\t', '', speed)
            speed = speed.split(' ')[0] + ' Mbit/s'
            price = i.find_all('td')[-2].text
            price = re.sub(r'\r\n\t\t', '', price)
            price = re.sub(r'\r\n\t', '', price)
            price = price[:-4]

            obj = {
                'name': 'Unlim',
                'info': {
                    'title': title,
                    'speed': speed,
                    'price': price,
                }
            }
            array.append(obj)
        with open('json/flink-plans.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(array, indent=3, ensure_ascii=False))
        return array
    except:
        return []


def get_coverage(url):
    try:

        response = requests.get(url).text
        parsed = bs(response, 'html.parser')
        panel_groups = parsed.find_all('div', {'class': 'panel-group'})
        districts = ['Чиланзарский район (партнерская сеть)']
        districts_parsed = parsed.find_all('h4', {'class': ''})[1:]
        for i in districts_parsed:
            districts.append(i.text)
            # print(i.text)
        array = []

        for i in range(len(panel_groups)):
            try:
                district = districts[i].split(" (")[0]
            except TypeError:
                district = districts[i]
            if district[0] == ' ':
                district = district[1:]
            panel = panel_groups[i].find_all('div', {'class': 'panel'})
            obj = {
                'district': district
            }
            # houses_arr = []
            for j in panel:
                street = j.find('a').text
                street = re.sub(r'\r\n\t\t\t', '', street)
                houses = j.find('div', {'class': 'panel-body'}).text
                houses = re.sub(r'[\r\n\t]', '', houses)
                houses = re.sub('  ', '', houses)
                if houses[:5] == 'Дома:':
                    houses = houses[6:]
                elif houses[:7] == ' Дома: ':
                    houses = houses[7:]
                # for x in range(len(houses)):
                #     try:
                #         if houses[x][0] == ' ':
                #             houses[x] = houses[x][1:]
                #     except IndexError:
                #         pass
                obj = {
                    'district': district,
                    'street': street,
                    'houses': houses
                }
                # print(houses)
                array.append(obj)
        with open('json/flink-coverage.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(array, indent=3, ensure_ascii=False))
        # print(array)
    except:
        return []


# flink_plans = get_plans('https://flink.uz/sub/view/tarifs')
# flink_coverage = get_coverage('https://flink.uz/sub/view/area')



with open('json/flink-coverage.json', 'r', encoding='utf-8') as file:
    flink_coverage = json.load(file)


with open('json/flink-plans.json', 'r', encoding='utf-8') as file:
    flink_plans = json.load(file)


