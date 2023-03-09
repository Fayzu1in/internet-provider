import json 
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'providers.settings')
django.setup()

from data.models import Plan, Coverage

with open('../api/json/flink-coverage.json', 'r', encoding='utf-8') as file:
    flink_coverage = json.load(file)


with open('../api/json/tps-plans.json', 'r', encoding='utf-8') as file:
    tps_plans = json.load(file)


def insert(plans):
    for i in plans:
        new = Plan(provider='tps', name=i['name'], title=i['name'], speed = i['info']['speed'], price=i['info']['price'])
        new.save()
    

# insert(flink_plans)


# def insert_coverage(coverage):
#     for i in coverage:
#         new = Coverage(district=i['district'], street=i['street'], houses=i['houses'])
#         new.save()



insert(tps_plans)
# insert_coverage(flink_coverage)


