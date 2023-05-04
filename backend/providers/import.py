import json 
import requests



data = requests.get('http://127.0.0.1:8000/api/v1/coverage/').json()
for i in data:
    print(i)
    print('-----------------')


with open('../api/json/data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=3, ensure_ascii=False)
