"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Users(db.Model):

    __tablename__ = 'users'

    # @classmethod
    # def get_all_hungry(cls):
    #     return cls.query.filter(Pet.hunger > 20).all()
    # def  __repr__(self):
    #     return f'<Pet id ={self.id}'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(10), nullable=False)
    last_name = db.Column(db.String(10), nullable=False)
    image_url = db.Column(db.String(200), nullable = True)