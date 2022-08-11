from models import Users, Posts, Tag, PostTag, db
from app import app

db.drop_all()
db.create_all()

Users.query.delete()
Posts.query.delete()
Tag.query.delete()
PostTag.query.delete()

db.session.add()

db.session.commit()