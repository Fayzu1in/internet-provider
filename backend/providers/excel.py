import pandas as pd
import json
import os 
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'providers.settings')
django.setup()
from data.models import Coverages, AllProviders



def test(file_name:str):
    df = pd.read_excel(f'../api/excel/{file_name}.xlsx')
    grouped = df.groupby(['Город', 'Район', 'Улица'])
    result = []
    for name, group in grouped:
        d = {
            'city': name[0],
            'district': name[1],
            'street': name[2],
            'providers': ['ISTV'],
            'houses': group['Дом'].tolist()
        }
        result.append(d)
    #? printing result by each object
    # for i in result:
    #     print(i)

    print(result[1])
    print('Total length: ', len(result))
    with open('../api/json/istv_coverage.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=3)
    return result


# test('список')


#? saving into database
with open('../api/json/new-overall-coverage.json') as file:
    data = json.load(file)

for obj in data:
    loc = Coverages(city=obj['city'], district=obj['district'], street=obj['street'], providers=obj['providers'], houses=obj['houses'])
    loc.save()
