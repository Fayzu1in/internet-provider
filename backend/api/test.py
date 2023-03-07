import requests


def test(api):
    response = requests.get('http://127.0.0.1:5000/' + api)
    if response.status_code == 200:
        print(response.text)


test('flink-coverage')

# test('comnet-coverage')

# test('uzonline-plans')
