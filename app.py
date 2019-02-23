from celery import Celery

import time

app = Celery('tasks', backend='rpc://', broker='pyamqp://socialcops:socialcops!23@localhost:5672/socialcop_host')

@app.task
def upload():
	time.sleep(60)
	return "hello"