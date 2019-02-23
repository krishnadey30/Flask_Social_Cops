from celery import Celery

import time

app = Celery('tasks', backend='rpc://', broker='pyamqp://socialcops:socialcops@localhost:5672/socialcop_host')

@app.task
def upload(filename):
	time.sleep(60)


@app.task
def create_teams(filename):
	time.sleep(70)
