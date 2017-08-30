from flask_wtf import FlaskForm 
from wtforms import StringField
from wtforms.validators import DataRequired

class NoteForm(FlaskForm):
	note_title = StringField('note_title', validators=[DataRequired()])
	note_description = StringField('note_description', validators=[DataRequired()])