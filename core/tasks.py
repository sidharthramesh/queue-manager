from celery import shared_task, task

@task
def add(a,b):
    return a+b

@task
def send_request():
    import requests, time
    r = requests.post('https://requestb.in/1dvp3ch1', data={"ts":time.time()})
    print r.status_code
    print r.content