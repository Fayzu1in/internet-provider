import json 
import os
import django
from django.db.models.signals import post_save
from django.dispatch import receiver
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'providers.settings')
django.setup()
from data.models import Coverages


with open('../api/json/flink-coverage.json', 'r') as file:
    flink_coverage = json.load(file)
    
with open('../api/json/comnet-coverage.json', 'r') as file:
    comnet = json.load(file)

with open('../api/json/overall-coverage.json', 'r') as file:
    coverage = json.load(file)
    

#? inserting values 
def inserting(arr):
    print(f'Array length: {len(arr)}')
    for i in arr:
        providers = ''
        if len(i['providers']) > 1:
            for j in i['providers']:
                providers = 'freelink, comnet'
        else:
            providers = i['providers'][0]
        print(providers)
        new = Coverages(district=i['district'], street=i['street'], providers=providers)
        new.save()
inserting(coverage)

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
