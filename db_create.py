from application import db
from application.models import Note
from application.models import User
# create the database and the database table
db.create_all()
# insert Note data
Note1 = Note('Slow-Cooked Tacos', 'Delicious chicken that has been simmering in taco seasoning and sauce.  Perfect with hard-shelled tortillas!')
Note2 = Note('Hamburgers', 'Classic dish elevated with pretzele buns.')
Note3 = Note('Grilled Chicken', 'Grilled chicken served with pitas, hummus, and sauted veggies.')
db.session.add(Note1)
db.session.add(Note2)
db.session.add(Note3)
db.session.commit()

User1 = User('admin', 'admin')
db.session.add(User1)
db.session.commit()