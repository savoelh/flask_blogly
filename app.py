
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Users, Posts, Tag, PostTag

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'シーッ,それは秘密です'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def list_users():
    users = Users.query.all()
    tag = Tag.query.all()
    return render_template('home.html', users=users, tag=tag)


@app.route('/<int:user_id>')
def show_user(user_id):
    user = Users.query.get_or_404(user_id)
    my_posts = Posts.query.filter_by(users_id=user_id)
    print(my_posts)
    return render_template('details.html', user=user,  my_posts=my_posts)


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
    user = Users.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/')

@app.route('/<int:user_id>/post', methods=['POST'])
def make_post(user_id):
    user = Users.query.get(user_id)
    p_title = request.form['p_title']
    p_content = request.form['p_content']
    entry = Posts(title=p_title, content=p_content, users_id=user.id)
    db.session.add(entry)
    db.session.commit()
    return redirect(f'/{user.id}')

@app.route('/<int:post_id>/post_edit')
def post_edit(post_id):
    this_post = Posts.query.get(post_id)
    return render_template('/post_edit.html', this_post=this_post)

@app.route('/<int:post_id>/post_edit_submit')
def post_edit_submit(post_id):
    this_post = Posts.query.get(post_id)
    e_p_title = request.args['e_p_title']
    e_p_content = request.args['e_p_content']

    this_post.title = e_p_title
    this_post.content = e_p_content

    db.session.add(this_post)
    db.session.commit()

    return redirect(f'/{this_post.users_id}')

@app.route('/<int:post_id>/remove_post')
def remove_post(post_id):
    this_post = Posts.query.get(post_id)
    db.session.delete(this_post)
    db.session.commit()
    return redirect(f'/{this_post.users_id}')