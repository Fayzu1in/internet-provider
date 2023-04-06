import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'providers.settings')
django.setup()
from data.models import Plan


with open('../api/json/comnet-plans.json', 'r') as file:
    comnet = json.load(file)


with open('../api/json/flink-plans.json', 'r') as file:
    flink = json.load(file)


with open('../api/json/istv-plans.json', 'r') as file:
    istv = json.load(file)


with open('../api/json/sarkor-plans.json', 'r') as file:
    sarkor = json.load(file)


with open('../api/json/tps-plans.json', 'r') as file:
    tps = json.load(file)


with open('../api/json/uzonline-plans.json', 'r') as file:
    uzonline = json.load(file)


all_plans = comnet + flink + istv + sarkor + uzonline + tps


print('comnet:', len(comnet))
print('flink:', len(flink))
print('istv:', len(istv))
print('sarkor:', len(sarkor))
print('uzonline:', len(uzonline))
print('tps:', len(tps))
print('Total:', len(all_plans))


# ? flink inserting data into table
def insert_flink(arr):
    for i in arr:
        # if Plan.objects.get(name=i['name']) is not None:
        new = Plan(
            provider_id=1,
            title=i['info']['title'],
            name=i['name'],
            speed=i['info']['speed'],
            price=i['info']['price'],
            tech='GPON',
            limit='unlim',
            day=i['info']['speed'],
            night=i['info']['speed'],
            info='',
            abonents='physic')
        new.save()


# ? call when you need to add Plans
# insert_flink(flink)


# # #? comnet inserting data into table
def comnet_insert(arr):
    for i in arr:
        new = Plan(
            provider_id=2,
            name=i['name'],
            title=i['name'],
            speed=i['info']['speed'],
            price=i['info']['price'],
            tech='GPON',
            limit='unlim',
            day=i['info']['speed'],
            night=i['info']['speed'],
            info='',
            abonents='physic')
        new.save()


# comnet_insert(comnet)


# # #? sarkor inserting data into table
def sarkor_insert(arr):
    for i in arr:
        new = Plan(
            provider_id=6,
            title=i['info']['title'],
            name=i['name'],
            speed=i['info']['speed'],
            price=i['info']['price'],
            tech='GPON',
            limit='unlim',
            day=i['info']['speed'],
            night=i['info']['night'],
            info=i['info']['more'],
            abonents='physic')
        new.save()


# sarkor_insert(sarkor)


# # #? uzonline inserting data into table
def uzonline_plans(arr):
    for i in arr:
        new = Plan(
            provider_id=5,
            title=i['info']['title'],
            name=i['name'],
            speed=i['info']['speed'],
            price=i['info']['price'],
            tech='GPON',
            limit='unlim',
            day=i['info']['speed'],
            night=i['info']['speed'],
            info='',
            abonents='physic')
        new.save()


# uzonline_plans(uzonline)

# # #? tps inserting data into table


def tps_insert(arr):
    for i in arr:
        new = Plan(
            provider_id=4,
            title=i['info']['title'],
            name=i['name'],
            speed=i['info']['speed'],
            price=i['info']['price'],
            tech='GPON',
            limit='unlim',
            day=i['info']['speed'],
            night=i['info']['speed'],
            info='',
            abonents='physic')
        new.save()


# tps_insert(tps)

# #? istv inserting data into table


def istv_insert(arr):
    for i in arr:
        new = Plan(
            provider_id=3,
            title=i['info']['title'],
            name=i['name'],
            speed=i['info']['speed'],
            price=i['info']['price'],
            tech='GPON',
            limit='unlim',
            day=i['info']['speed'],
            night=i['info']['night'],
            info=i['info']['more'],
            abonents=i['type'])
        new.save()


# istv_insert(istv)

# print(Plan.objects.all())
