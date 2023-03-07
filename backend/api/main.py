from typing import Union
from uzonline import uzonline_lines, uzonline_plans

from fastapi import FastAPI
from comnet import comnet_coverage, comnet_plans
from flink import flink_coverage, flink_plans
import uvicorn
app = FastAPI()


@app.get('/uzonline-lines')
def start():
    return uzonline_lines


@app.get('/uzonline-plans')
def start():
    return uzonline_plans


@app.get('/comnet-plans')
def start():
    return comnet_plans


@app.get('/comnet-coverage')
def start():
    return comnet_coverage


@app.get('/flink-plans')
def start():
    return flink_plans


@app.get('/flink-coverage')
def start():
    return flink_coverage


# ? Command to run uvicorn server from terminal (test)
# ? uvicorn main:app --reload
if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, reload=True, access_log=False)
