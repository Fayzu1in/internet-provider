import requests


def test(api):
    response = requests.get('http://127.0.0.1:5000/' + api)
    if response.status_code == 200:
        print(response.text)


# test('flink-coverage')

# test('comnet-coverage')

# test('uzonline-plans')






def click_test():
    response = requests.post(data={'title': 'test'}, url='http://127.0.0.1:8000/api/v1/click/')

    print(response.status_code, response.text)


click_test()