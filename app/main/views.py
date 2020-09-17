from flask import render_template, redirect, url_for, abort, flash, request, current_app, make_response
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import main
from .. import db
from ..models import User, Post

from .forms import RegistryForm, LoginForm, PostForm

@main.route('/')
def index():
    return render_template('index.html')



@main.route('/registry', methods=['POST','GET'])
def registry():
    form = RegistryForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        password_hash = generate_password_hash(password)
        user = User(email=email, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        flash('Registrierung erfolgreich')
        return redirect(url_for('main.index'))



    return render_template('registry.html', form=form)


@main.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and check_password_hash(user.password_hash, form.password.data):

            login_user(user)
            flash("eingeloggt")
            return redirect(url_for('main.index'))
        else:
            print("else tree")


    return render_template('login.html', form=form)





@main.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@login_required
@main.route("/new_post", methods=['POST', 'GET'])
def create_new_post():
    form = PostForm()

    if form.validate_on_submit():
        heading = form.heading.data
        body = form.body.data
        print(heading)
        print(body)

        post = Post(heading=heading, body=body)
        db.session.add(post)
        db.session.commit()

    return render_template("create_new_post.html", form=form)


@main.route('/change_post')
def change_post():
    posts = Post.query.all()
    return render_template('einsaetze.html', posts=posts)




@main.route('/posts')
def posts():

    posts = Post.query.all()

    return render_template('einsaetze.html', posts=posts)





# @main.route('/', methods=['GET', 'POST'])
# def index():
#     form = PostForm()
#     if current_user.can(Permission.WRITE) and form.validate_on_submit():
#         post = Post(body=form.body.data,
#                     author=current_user._get_current_object())
#         db.session.add(post)
#         db.session.commit()
#         return redirect(url_for('.index'))
#     page = request.args.get('page', 1, type=int)
#     show_followed = False
#     if current_user.is_authenticated:
#         show_followed = bool(request.cookies.get('show_followed', ''))
#     if show_followed:
#         query = current_user.followed_posts
#     else:
#         query = Post.query
#     pagination = query.order_by(Post.timestamp.desc()).paginate(
#         page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
#         error_out=False)
#     posts = pagination.items
#     return render_template('index.html', form=form, posts=posts,
#                            show_followed=show_followed, pagination=pagination)




#
# @main.route('/edit-profile', methods=['GET', 'POST'])
# @login_required
# def edit_profile():
#     form = EditProfileForm()
#     if form.validate_on_submit():
#         current_user.name = form.name.data
#         current_user.location = form.location.data
#         current_user.about_me = form.about_me.data
#         db.session.add(current_user._get_current_object())
#         db.session.commit()
#         flash('Your profile has been updated.')
#         return redirect(url_for('.user', username=current_user.username))
#     form.name.data = current_user.name
#     form.location.data = current_user.location
#     form.about_me.data = current_user.about_me
#     return render_template('edit_profile.html', form=form)







