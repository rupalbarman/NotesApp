from flask import render_template, Blueprint, request, redirect, url_for
from .forms import NoteForm
from application.models import Note
from application import db 

notes_blueprint = Blueprint('notes', __name__, template_folder = 'templates')

@notes_blueprint.route('/')
@notes_blueprint.route('/index')
def index():
	return render_template('index.html')

@notes_blueprint.route('/notes')
def notes():
	all_notes = Note.query.all()
	return render_template('notes.html', notes = all_notes)

@notes_blueprint.route('/add', methods = ['GET', 'POST'])
def add():
	form = NoteForm(request.form)
	if request.method == 'GET':
		return render_template('add_note.html', form = form)
	else:
		if form.validate_on_submit():
			new_note = Note(form.note_title.data, form.note_description.data)
			db.session.add(new_note)
			db.session.commit()
			print('New Note, {}, added!'.format(new_note.note_title), 'success')
			return redirect(url_for('notes.index'))