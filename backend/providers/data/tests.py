from django.test import TestCase

import requests
import json


def api_test(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)


async def get_coverage_async(url):
    response = await requests.get(url)
    if response.status_code == 200:
        print(await response.text)
