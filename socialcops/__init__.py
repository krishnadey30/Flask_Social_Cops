# flask imports go here
from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from flask_mongoengine import MongoEngine
import os

# declaring the app
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'socialcops',
    'host': 'mongodb://localhost/database_name'
}
UPLOAD_FOLDER = '/path/to/the/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# create db
db = MongoEngine(app)
# get the base dir
base_dir = os.path.dirname(os.path.abspath(__file__))
app.config.from_pyfile(os.path.join(base_dir, '../app.cfg'))


# importing views
import socialcops.views

# import models
from socialcops.models.models import Data,Teams
