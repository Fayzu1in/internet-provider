import pandas as pd
import json
import os
import django
from django.db import transaction
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'providers.settings')
django.setup()
from data.models import Coverages, AllProviders


with open('../api/json/flink-coverage.json', 'r') as file:
    flink_coverage = json.load(file)

with open('../api/json/comnet-coverage.json', 'r') as file:
    comnet = json.load(file)

with open('../api/json/overall-coverage.json', 'r') as file:
    coverage = json.load(file)

with open('../api/json/new-overall-coverage.json', 'r') as file:
    new_coverage = json.load(file)

# ? inserting values
def inserting(arr):
    print(f'Array length: {len(arr)}')
    providers = AllProviders.objects.all()
    for i in arr:
        print(i['providers'])
        new = Coverages.objects.create(city=i['city'],
            district=i['district'], street=i['street'], houses=i['houses'])
        with transaction.atomic():
            new.save()
            for related_item in i['providers']:
                related_model = AllProviders.objects.get(
                    name=related_item)
                new.providers.add(related_model)
            # for house in i['houses']:
            #     new.houses += f'{house}, '
        print(new)
        new.save()
        print('Done')

inserting(new_coverage)

# #? inserting comnet into coverage list


def comnet_inserting(coverage, arr):
    matches = 0
    for i in arr:
        for j in coverage:
            if i['street'] == j['street']:
                print(f'{i} ----- {j}')
                matches += 1
    print(matches)

# comnet_inserting(coverage, comnet)


def rewriting_json(arr):
    new_arr = []
    for i in arr:
        if i['district'][0] != 'г':
            obj = {
                'city': 'Ташкент',
                'district': i['district'],
                'street': i['street'],
                'providers': i['providers'],                
                'houses': []
            }
        else:
            obj = {
                'city': i['district'][3:],
                'district': i['district'],
                'street': i['street'],
                'providers': i['providers'],
                'houses': []
            }
        new_arr.append(obj)
    for i in new_arr:
        print(i)
    print('Total length: ', len(new_arr))
    return new_arr


# new_coverage = rewriting_json(coverage)


# with open('../api/json/new-overall-coverage.json', 'w', encoding='utf-8') as file:
#     json.dump(new_coverage, file, indent=4, ensure_ascii=False)
