import requests

import json

from bs4 import BeautifulSoup as bs
import re


def get_coverage(url):
    response = requests.get(url).text
    parsed = bs(response, 'html.parser')
    all_divs = parsed.find_all('div', {'class': 'CoverageAreaAccordion'})[0]
    coverage = all_divs.find_all(
        'div', {'class': 'accordion__item'})
    array = []

    for i in coverage:
        # print(i)
        try:
            district = i.find('div', {'class':'accordion__heading'})
            district = district.find('h2').text
            # print(district)
        except:
            district = ''
        panels = i.find_all('div', {'class': 'CoverageAreaAccordion__panelTitlesWr'})
        for j in panels: 
            street = j.find('div', {'class': 'CoverageAreaAccordion__street'})
            try:
                street = street.text 
            except AttributeError:
                street = ''
            houses = j.find('div', {'class': "CoverageAreaAccordion__houses"})
            try: 
                final_arr = []
                houses = houses.text.split(',')
                for k in houses:
                    try: 
                        if k[0] == ' ':
                            k = re.sub(' ', '', k)
                        final_arr.append(k)
                    except IndexError:
                        pass    
            except AttributeError:
                houses = []
            obj = {
                'district': district,
                'street': street, 
                'houses': final_arr
            }
            array.append(obj)
            print(array)
    with open('json/comnet-coverage.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(array, indent=3, ensure_ascii=False))
    return array


# ? async function to get the result
# async def summarize():
#     array = await get_coverage('https://comnet.uz/uz-tashkent/home-users/cover-zone')
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
# cover_tashkent = get_coverage(
#     'https://comnet.uz/home-users/cover-zone')

# ? Fargona
# cover_fergana = get_coverage('https://comnet.uz/uz-tashkent/home-users/cover-zone')


with open('json/comnet-plans.json', 'r', encoding='utf-8') as file:
    comnet_plans = json.load(file)

with open('json/comnet-coverage.json', 'r', encoding='utf-8') as file:
    comnet_coverage = json.load(file)
