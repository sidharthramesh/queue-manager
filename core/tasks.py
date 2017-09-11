from celery import shared_task, task
import requests, datetime

@task
def add(a,b):
    return a+b

@task
def ping():
    r = requests.post("https://requestb.in/1dvp3ch1",{"datetime":datetime.datetime.now()})
    return r.status_code