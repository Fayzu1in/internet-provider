import requests
from bs4 import BeautifulSoup as bs
import re
import json
url = 'https://uztelecom.uz/uz/jismoniy-shaxslarga/internet-2/tariflar-2'


#! Uzmobile
def get_tarif_lines(url):
    global all_tarif_lines
    response = requests.get(url).text
    parsed = bs(response, 'html.parser')
    tarifs = parsed.find_all('div', {'class': 'item'})
    array = []
    for i in tarifs:
        tarif_info = i.find_all('span', {'class': 'title'})
        for a in tarif_info:
            # ? Tarif lines
            # ? tarif title
            # print(re.findall(r'[A-Z]+', a.text)[0])
            # ? tarif price
            # print(re.findall(r'[0-9]+.[0-9]+', a.find_all('span', {'class':'sub'})[0].text)[0], '\n', '-----------------')
            obj = {
                'title': re.findall(r'[A-Z]+', a.text)[0],
                'starting_price': re.findall(r'[0-9]+.[0-9]+', a.find_all('span', {'class': 'sub'})[0].text)[0]
            }
            final_obj = {
                'provider': 'UZMOBILE',
                'info': obj
            }

        array.append(final_obj)

    return array


def get_full_lines(url, tarif_name):
    response = requests.get(url+tarif_name).text
    parsed = bs(response, 'html.parser')
    tarifs = parsed.find_all('div', {'class': 'item'})
    name = parsed.find_all('h2')[0].text
    array = []
    for i in tarifs:
        # print(i)
        # ? full tarif info including name and price
        tarif_data = i.find_all('div', {'class': 'name'})[0]

        # ? speed data through taking it from strong tag in div
        speed = i.find_all('div', {'class': 'internet'})[
            0].find_all('strong')[0].text

        # ? full title text
        title = tarif_data.find_all('strong')[0].text

        price_sum = tarif_data.find_all('span')[0].text
        price = re.findall(r'[0-9]+.[0-9]+', price_sum)[0]
        obj = {
            'title': title,
            'speed': speed,
            'price': price
        }
        final_obj = {
            'name': name,
            'info': obj
        }
        #!Printing the results
        # print(title+ ' = ' +price)
        # print('------------------------------------')
        array.append(final_obj)
    return array
    # tarif_data.append(final_obj)


#! Getting the tarif lines info
# plans =  get_tarif_lines(url)
#! Getting the all tarifs info
# yangi = get_full_lines('https://uztelecom.uz/uz/jismoniy-shaxslarga/internet-2/tariflar-2/', 'yangi')
# unlim =  get_full_lines('https://uztelecom.uz/uz/jismoniy-shaxslarga/internet-2/tariflar-2/', 'unlim-21')
#! Printing data
# print(plans)
# print(yangi)
# print(unlim)

def get_maktab_talaba(url):
    response = requests.get(url).text
    parsed = bs(response, 'html.parser')

    name = parsed.find('h1').text

    # ? getting speed
    speed = parsed.find_all(
        'div', {'class': 'li_wraps'})[-1].find('strong').text
    # print(speed)

    # ? getting the price first with sums then only digits
    price_sums = parsed.find_all(
        'div', {'class': 'item w-12'})[0].find('h2').text
    price = re.findall(r'[0-9]+.[0-9]+', price_sums)[0]

    obj = {
        'name': name,
        'info': {
            'title': name,
            'speed': speed,
            'price': price
        }
    }
    array = []
    array.append(obj)
    return array
    # print(price)


# maktab = get_maktab_talaba('https://uztelecom.uz/uz/jismoniy-shaxslarga/internet-2/tariflar-2/maktab-4/maktab-2')
# talaba = get_maktab_talaba('https://uztelecom.uz/uz/jismoniy-shaxslarga/internet-2/tariflar-2/maktab-4/talaba-2')


def summarize():
    global yangi, unlim, talaba, maktab
    all_lines = get_tarif_lines(
        'https://uztelecom.uz/uz/jismoniy-shaxslarga/internet-2/tariflar-2')

    yangi = get_full_lines(
        'https://uztelecom.uz/uz/jismoniy-shaxslarga/internet-2/tariflar-2/', 'yangi')
    unlim = get_full_lines(
        'https://uztelecom.uz/uz/jismoniy-shaxslarga/internet-2/tariflar-2/', 'unlim-21')
    maktab = get_maktab_talaba(
        'https://uztelecom.uz/uz/jismoniy-shaxslarga/internet-2/tariflar-2/maktab-4/maktab-2')
    talaba = get_maktab_talaba(
        'https://uztelecom.uz/uz/jismoniy-shaxslarga/internet-2/tariflar-2/maktab-4/talaba-2')
    array = yangi + unlim + maktab + talaba
    # with open('txt/uzonline.txt', 'w+', encoding='UTF-8') as file:
    #     file.write(
    #         f'Tarif lines Uzonline: {json.dumps(all_lines, indent=3)}\nAll Tarifs: {json.dumps(array, indent=3)}')
    with open('json/uzonline-plans.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(array, indent=3, ensure_ascii=False))

    with open('json/uzonline-lines.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(all_lines, indent=3, ensure_ascii=False))
    return all_lines, array


with open('json/uzonline-lines.json', 'r', encoding='utf-8') as file:
    uzonline_lines = json.load(file)

with open('json/uzonline-plans.json', 'r', encoding='utf-8') as file:
    uzonline_plans = json.load(file)
