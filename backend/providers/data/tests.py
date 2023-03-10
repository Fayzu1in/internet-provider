from django.test import TestCase

import requests 
import json 


def api_test(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)



api_test("http://127.0.0.1:8000/api/v1/offers")