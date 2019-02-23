# flask imports go here
from flask import Flask
from flask_mongoengine import MongoEngine
import os

# declaring the app
app = Flask(__name__)
# get the base dir
base_dir = os.path.dirname(os.path.abspath(__file__))
app.config.from_pyfile(os.path.join(base_dir, '../app.cfg'))
app.config['MONGODB_SETTINGS'] = {
    'db': 'socialcops',
    'host': 'mongodb://localhost/database_name'
}
UPLOAD_FOLDER = os.path.join(base_dir, '/media/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
print(UPLOAD_FOLDER)

# create db
db = MongoEngine(app)

# importing views
import socialcops.views

# import models
from socialcops.models.models import Data,Teams
