from models import Users, db
from app import app

db.drop_all()
db.create_all()

Users.query.delete()

