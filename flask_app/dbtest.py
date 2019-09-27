from application import db
from application.models import Users, Posts
db.create_all()
#user1 = Users(email='sean.oreilly@gmail.com', password='password')
#db.session.add(user1)
#db.session.commit()
#Users.query.first()
