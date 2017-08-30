from flask import Flask
from flask_sqlalchemy import SQLAlchemy

################
#### config ####
################
#app = Flask(__name__)
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
db = SQLAlchemy(app)
####################
#### blueprints ####
####################
from application.users.views import users_blueprint
from application.notes.views import notes_blueprint
# register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(notes_blueprint)