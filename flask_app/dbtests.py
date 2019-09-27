from application import db
from application.models import Posts
db.create_all()
#p1=Posts(first_name="B", last_name="Gc", title="testtwo", content="testtestesttwo")
#db.session.add(p1)
db.session.commit()
#results = Posts.query.all()
#print(results)
