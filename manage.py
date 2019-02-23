from flask_script import Manager, Server, Shell
from socialcops import app
from socialcops import db

# (optional) - include models if you want to!
import socialcops.models as models

def _make_context():
  """ context for passing into to the shell command """
  return dict(app=app, db=db, models=models)

# set manager
manager = Manager(app)

# add commands
manager.add_command("runserver", Server())
manager.add_command("shell", Shell(make_context = _make_context))

if __name__ == "__main__":
  manager.run()