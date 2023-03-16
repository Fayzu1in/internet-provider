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
    flink_coverage = json.load(file)
    

#? inserting values 
def inserting(arr):
    print(f'Array length: {len(arr)}')
    for i in arr:
        new = Coverages(district=i['district'], street=i['street'], providers='freelink')
        new.save()
# inserting(flink_coverage)


#? adding comnet where its necces