import pandas as pd
import json
import os
import django
from django.db import transaction
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'providers.settings')
django.setup()
from data.models import Coverages, AllProviders
import re 

with open('../api/json/flink-coverage.json', 'r') as file:
    flink_coverage = json.load(file)

with open('../api/json/comnet-coverage.json', 'r') as file:
    comnet = json.load(file)

with open('../api/json/overall-coverage.json', 'r') as file:
    coverage = json.load(file)

with open('../api/json/new-overall-coverage.json', 'r') as file:
    new_coverage = json.load(file)


with open('../api/json/final-coverage.json', 'r') as file:
    final_coverage = json.load(file)


with open('../api/json/data.json', 'r') as file:
    data = json.load(file)

# ? inserting values
def inserting(arr):
    print(f'Array length: {len(arr)}')
    providers = AllProviders.objects.all()
    for i in arr:
        print(i['providers'])
        try: 
            houses_arr = i["houses"]
            # houses_arr = sorted(houses_arr)
            houses = ''
            for j in houses_arr:
                houses += str(j) + ' '
        except:
            houses = ''
        try: 
            sarkor_arr = i["sarkor_houses"]
            # sarkor_arr = sorted(sarkor_arr)
            sarkor = ''
            for j in sarkor_arr:
                sarkor += str(j) + ' '
        except:
            sarkor = ''
        try:
            uzonline_arr = i["uzonline_houses"]
            # uzonline_arr = sorted(uzonline_arr)
            uzonline = ''
            for j in uzonline_arr:
                uzonline += str(j) + ' '
        except:
            uzonline = ''
        try:
            ars_inform_arr = i["ars_inform_houses"]
            # ars_inform_arr = sorted(ars_inform_arr)
            ars_inform = ''
            for j in ars_inform_arr:
                ars_inform += str(j) + ' '
            
        except:
            ars_inform = ''
        try:
            freelink_arr = i["freelink_houses"]
            # freelink_arr = sorted(freelink_arr)
            freelink = ''
            for j in freelink_arr:
                freelink += str(j) + ' '
        except:
            freelink = ''

        try:
            comnet_arr = i["comnet_houses"]
            # comnet_arr = sorted(comnet_arr)
            comnet = ''
            for j in comnet_arr:
                comnet += str(j) + ' '

        except:
            comnet = ''

        try: 
            city_net_arr = i["city_net_houses"]
            # city_net_arr = sorted(city_net_arr)
            city_net = ''
            for j in city_net_arr:
                city_net += str(j) + ' '

        except:
            city_net = ''
        
        try: 
            gals_arr = i["gals_houses"]
            # gals_arr = sorted(gals_arr)
            gals = ''
            for j in gals_arr:
                gals += str(j) + ' '
        except:
            gals = ''
        
        try: 
            spectr_arr = i["spectr_houses"]
            # spectr_arr = sorted(spectr_arr)
            spectr = ''
            for j in spectr_arr:
                spectr += str(j) + ' '
        except:
            spectr = ''
      
        new = Coverages.objects.create(
            city=i['city'],
            district=i['district'], 
            street=i['street'], 
            houses=houses, 
            sarkor_houses=sarkor, 
            uzonline_houses=uzonline, 
            ars_inform_houses=ars_inform, 
            freelink_houses=freelink, 
            comnet_houses=comnet,
            city_net_houses=city_net,
            gals_houses=gals,
            spectr_houses=spectr
            )
        with transaction.atomic():
            new.save()
            for related_item in i['providers']:
                related_model = AllProviders.objects.get(
                    name=related_item)
                new.providers.add(related_model)
        print(new)
        new.save()
        print('Done')

inserting(final_coverage)

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
