import requests

import json

from bs4 import BeautifulSoup as bs
import re


def get_data(url):
    response = requests.get(url).text
    parsed = bs(response, 'html.parser')
    all_divs = parsed.find_all('div', {'class': 'CoverageAreaAccordion'})[0]
    coverage = all_divs.find_all(
        'div', {'class': 'CoverageAreaAccordion__panelTitlesWr'})
    array = []

    for i in coverage:
        street = i.find('div', {'class': 'CoverageAreaAccordion__street'})
        street = str(street).split(
            '<div class="CoverageAreaAccordion__panelTitle CoverageAreaAccordion__street">')[-1][:-6]

        houses = i.find('div', {'class': 'CoverageAreaAccordion__houses'})
        houses = str(houses).split(
            '<div class="CoverageAreaAccordion__panelTitle CoverageAreaAccordion__houses">')[-1][:-6]
        match = re.match(r'<div+', houses)
        final_arr = []
        if match:
            houses = None
        # print(houses)
        # print('--------------------------------------')
        else:
            houses_arr = houses.split(',')
        for i in houses_arr[:-1]:
            i = re.sub(' ', '', i)
            final_arr.append(i)
        obj = {
            'street': street,
            'houses': final_arr
        }
        array.append(obj)
    with open('json/comnet-coverage.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(array, indent=3, ensure_ascii=False))
    return array
    # with open('data.txt', 'w', encoding='UTF-8') as file:
    #     file.write(parsed.prettify())

# ? async function to get the result
# async def summarize():
#     array = await get_data('https://comnet.uz/uz-tashkent/home-users/cover-zone')
#     return array


def get_plans():
    array = [
        {
            'name': 'Econom+',
            'info': {
                'speed': '30 Mb/s',
                'price': '119 000'
            }
        },

        {
            'name': 'Comfort+',
            'info': {
                'speed': '60 Mb/s',
                'price': '159 000'
            }
        },

        {
            'name': 'Pro+',
            'info': {
                'speed': '100 Mb/s',
                'price': '199 000'
            }
        },

        {
            'name': 'Turbo+',
            'info': {
                'speed': '200 Mb/s',
                'price': '299 000'
            }
        },
    ]
    with open('json/comnet-plans.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(array, indent=3, ensure_ascii=False))
    return array


# plans = get_plans()
# #? Tashkent
# cover_tashkent = get_data(
#     'https://comnet.uz/uz-tashkent/home-users/cover-zone')

# ? Fargona
# cover_fergana = get_data('https://comnet.uz/uz-tashkent/home-users/cover-zone')


with open('json/comnet-plans.json', 'r', encoding='utf-8') as file:
    comnet_plans = json.load(file)

with open('json/comnet-coverage.json', 'r', encoding='utf-8') as file:
    comnet_coverage = json.load(file)
