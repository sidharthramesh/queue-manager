from celery import shared_task, task

@task
def add(a,b):
    return a+b


