from celery import Celery

import time

app = Celery('tasks', backend='rpc://', broker='pyamqp://socialcops:socialcops@localhost:5672/socialcops')

@app.task
def upload():
	time.sleep(600)