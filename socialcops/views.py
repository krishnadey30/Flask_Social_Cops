# views go here
from socialcops import app
from socialcops.models.models import Person
from flask import render_template,request,redirect, url_for,send_from_directory
import os
from werkzeug.utils import secure_filename

@app.route('/')
def socialcops():
  return render_template("index.html")

@app.route('/test')
def test():
  return "i am the test route"

@app.route('/person')
def person():
  p1 = Person.query.first_or_404()
  #Eprint(p1)
  return "name = {}, age= {}".format(p1.first_name, 18)

@app.route('/person/new')
def new_author():
    """Creates a new author by a giving name (via GET parameter)
    e.g.: GET /author/new?name=Francisco creates a author named Francisco
    """
    author = Person(first_name=request.args.get('name', ''),last_name = request.args.get('last_name',''),age = request.args.get('age',18))
    author.save()
    return 'Saved :)'


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
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
