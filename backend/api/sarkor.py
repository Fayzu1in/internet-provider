import requests

import json
from bs4 import BeautifulSoup as bs
import re


def get_plans(url):
    response = requests.get(url).text
    parsed = bs(response, 'html.parser')
    tarif_cards = parsed.find_all('div', {'class': 'flickity-enabled'})
    print(tarif_cards)
    # for i in tarif_cards:
    #     print(i)
    #     print('---------------------')


get_plans('https://sarkor.uz/rus/tariff/series/wifi_new')
