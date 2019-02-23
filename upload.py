import falcon,json
from tasks import upload
from celery.task.control import revoke

class upload_data(object):
	def on_post(self,req,resp):


		result = upload.delay()
		res.status = falcon.HTTP_200




class stop(object):
	def on_get(self, req, resp):
		task_id = req.get_header('taskid')
		revoke(task_id,terminate=True, signal='SIGKILL')
		res.status = falcon.HTTP_200 
        res.body = ('Task has been terminated. Please upload the correct file')
