import os,sys,arrow
from socialcops import app
from socialcops.models.models import Data,Teams,Task
from flask import render_template,request,redirect, url_for,send_from_directory
from celery.task.control import revoke
from werkzeug.utils import secure_filename
sys.path.append('..')

from app import upload,create_teams

@app.route('/')
def socialcops():
  return render_template("index.html")


@app.route('/stop_task/')
def stop_task():
    """stop the task by giving the task_id (via GET parameter)
    e.g.: GET /stop_task/?id=some_id revokes the task
    """
    task_id = request.args.get('id', '')
    print(revoke(str(task_id)))
    return '''
    <!doctype html>
    <title>Task Stopped</title>
    <h1>Stoping Task</h1>
    <p> We have recieved a request to stop the task with id {}. If the task is still in queue it will be stopped else you have to wait
    </p>
    '''.format(task_id)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)


@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(location)
            task_id = upload.delay(filename)
            task = Task(task_id = str(task_id),file_name = filename,task_type = 1)
            task.save()
            return str(task_id)
            # return redirect(url_for('uploaded_file',filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
@app.route('/create_teams/', methods=['GET', 'POST'])
def create_teams():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(location)
            task_id = create_teams.delay(filename)
            task = Task(task_id = str(task_id),file_name = filename,task_type = 2)
            task.save()
            return str(task_id)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
