"""Blogly application."""

from distutils.command.build_scripts import first_line_re
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Users

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'シーッ,それは秘密です'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def list_users():
    users = Users.query.all()
    return render_template('home.html', users=users)


@app.route('/<int:user_id>')
def show_user(user_id):
    user = Users.query.get_or_404(user_id)
    return render_template('details.html', user=user)


@app.route('/AddUser')
def add_user():
    return render_template('AddUser.html')


@app.route('/submit_user')
def submit_user():
    f_name = request.args['f_name']
    l_name = request.args['l_name']
    img_url = request.args['img_url']
    entry = Users(first_name=f_name, last_name=l_name, image_url=img_url)
    db.session.add(entry)
    db.session.commit()
    return redirect('/')


@app.route('/<int:user_id>/edit_user')
def edit_user(user_id):
    user = Users.query.get_or_404(user_id)
    return render_template('editUser.html', user=user)


@app.route('/<int:user_id>/submit_edit')
def submit_edit(user_id):
    this_user = Users.query.get(user_id)
    e_f_name = request.args['e_f_name']
    e_l_name = request.args['e_l_name']
    e_img_url = request.args['e_img_url']

    this_user.image_url = e_img_url
    if e_f_name == '':
        this_user.first_name = this_user.first_name
    else:
        this_user.first_name = e_f_name
    if e_l_name == '':
        this_user.last_name = this_user.last_name
    else:
        this_user.last_name = e_l_name
    if e_img_url == '':
        this_user.image_url = this_user.image_url
    else:
        this_user.image_url = e_img_url

    db.session.add(this_user)
    db.session.commit()
    return redirect('/')

@app.route('/<int:user_id>/delete_user')
def delete_user(user_id):
    death = Users.query.get(user_id)
    db.session.delete(death)
    db.session.commit()
    return redirect('/')
