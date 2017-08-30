from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user_id = StringField('user_id', validators = [DataRequired()])
    user_password = StringField('user_password', validators = [DataRequired()])