from application import db

class Note(db.Model):
	__tablename__ = 'notes'

	id = db.Column(db.Integer, primary_key = True)
	note_title = db.Column(db.String, nullable = False)
	note_description = db.Column(db.String, nullable = False)

	def __init__(self, title, description):
		self.note_title = title
		self.note_description = description

	def __repr__(self):
		return 'title {}'.format(self.note_title)

class User(db.Model):
	__tablename__ = 'users'

	user_id = db.Column(db.String, primary_key = True)
	user_password = db.Column(db.String, nullable = False)

	def __init__(self, user_id, user_password):
		self.user_id = user_id
		self.user_password = user_password

	def __repr__(self):
		return 'title {}'.format(self.user_id)