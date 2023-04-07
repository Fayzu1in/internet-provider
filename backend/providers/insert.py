import json
import os
import django
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'providers.settings')
django.setup()
from data.models import Coverages, AllProviders


with open('../api/json/flink-coverage.json', 'r') as file:
    flink_coverage = json.load(file)

with open('../api/json/comnet-coverage.json', 'r') as file:
    comnet = json.load(file)

with open('../api/json/overall-coverage.json', 'r') as file:
    coverage = json.load(file)


# ? inserting values
def inserting(arr):
    print(f'Array length: {len(arr)}')
    providers = AllProviders.objects.all()
    for i in arr:
        # print(i['providers'])
        new = Coverages.objects.create(district=i['district'], street=i['street'])
        # for j in i['providers']:
        #     for k in providers:
        #         # print(k)
        #         if j.capitalize() == k.name:
        #             # print(f'{i}: {j.capitalize()} = {k.name}')
        #             prov = AllProviders.objects.get(name=k.name)
        #             print(prov)
        #             new.providers.add(prov)
        with transaction.atomic():
            new.save()
            for related_item in i['providers']:
                related_model = AllProviders.objects.get(name=related_item.capitalize())
                new.providers.add(related_model)


        print(new)
        # new.save()


# inserting(coverage)

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
        obj = {
            'district': i['district'],
            'street': i['street'],
            'providers': [
            ]
        }
        for j in i['providers']:
            obj_2 = {
                'provider': j,
                'houses': ''
            }
            obj['providers'].append(obj_2)
        new_arr.append(obj)
    return new_arr


new_coverage = rewriting_json(coverage)


with open('../api/json/new-overall-coverage.json', 'w', encoding='utf-8') as file:
    json.dump(new_coverage, file, indent=4, ensure_ascii=False)