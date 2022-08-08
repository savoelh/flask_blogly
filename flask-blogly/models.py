"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Users(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(10), nullable=False)
    last_name = db.Column(db.String(10), nullable=False)
    image_url = db.Column(db.String(200), nullable = True)

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

class Posts(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    created_at =  db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    users = db.relationship('Users', backref='posts')
