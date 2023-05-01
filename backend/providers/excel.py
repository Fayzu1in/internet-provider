import pandas as pd
import json
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'providers.settings')
django.setup()

from data.models import Coverages, AllProviders

def test(file_name: str):
    df = pd.read_excel(f'../api/excel/{file_name}.xlsx')
    grouped = df.groupby(['Город', 'Район', 'Улица'])
    result = []
    for name, group in grouped:
        print(name)
        d = {
            'city': name[0],
            'district': name[1],
            'street': name[2],
            'providers': ['ISTV'],
            'houses': group['Дом'].tolist()
        }
        result.append(d)
    # ? printing result by each object
    # for i in result:
    #     print(i)

    print(result[1])
    print('Total length: ', len(result))
    with open('../api/json/istv_coverage.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=3)
    return result


# test('список')


# ? saving into database
def save():
    with open('../api/json/new-overall-coverage.json') as file:
        data = json.load(file)

    for obj in data:
        loc = Coverages(city=obj['city'], district=obj['district'],
                        street=obj['street'], providers=obj['providers'], houses=obj['houses'])
        loc.save()

# save()


def sarkor_coverage():
    df = pd.read_excel(f'../api/excel/саркор1.xlsx')
    grouped = df.groupby(['город', 'район', 'микро р-н'])
    result = []
    for name, group in grouped:
        print(name[0], name[1], name[2])
        # print(name[1])
        d = {
            'city': name[0],
            'district': name[1],
            'street': name[2],
            'providers': ['Sarkor'],
            'houses': group['дом'].tolist(),
            "sarkor_houses": group['дом'].tolist()
        }
        result.append(d)

    with open('../api/json/sarkor_coverage.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=3)

    # data = []

# iterate over the rows of the dataframe
    # df = pd.read_excel('file.xlsx')

# Group the data by city, district, and street, and aggregate the houses into a list
    # grouped = df.groupby(['город', 'район', 'микро р-н', 'улица'])['дом'].apply(list).reset_index()

    # # Convert the grouped dataframe to a list of dictionaries
    # data = grouped.to_dict(orient='records')

    # # Write the data to a JSON file
    # with open('data.json', 'w') as f:
    #     json.dump(data, f)


sarkor_coverage()
