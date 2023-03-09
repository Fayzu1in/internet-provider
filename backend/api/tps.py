import requests 

from bs4 import BeautifulSoup as bs 

import json 

import re 


def get_plans(url):
    response = requests.get(url).text 
    parsed = bs(response, 'html.parser')

    packages = parsed.find_all('div', {'class': 'col-md-4 col-sm-12'})
    print(packages)



# get_plans('https://etc.uz/tps/tariff')