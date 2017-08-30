from flask import render_template, Blueprint, redirect, request
from .forms import LoginForm
from application.models import User
from application import db
from sqlalchemy.exc import IntegrityError

users_blueprint = Blueprint('users', __name__, template_folder = 'templates')

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
	    if form.validate_on_submit():
	    	try:
	    		new_user = User(form.user_id.data, form.user_password.data)
	    		print('User', form.user_id.data, form.user_password.data)
	    		db.session.add(new_user)
	    		db.session.commit()
	    		return redirect('/index')
	    	except IntegrityError:
	    		print('already user_id exists')
	    		db.session.rollback()
    return render_template('login.html', form=form)

@users_blueprint.route('/users')
def users():
	all_users = User.query.all()
	return render_template('users.html', users = all_users)