from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ykycvpylzpifmt:dfdd4e82a555336ad8133feedb971b0f25f3ba0653aaf69cab9298eddb250e1a@ec2-34-254-24-116.eu-west-1.compute.amazonaws.com:5432/d10bdpi7er82iu'
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    # @property
    # def password(self):
    #     raise AttributeError('password is not a readable attribute')
    #
    # @password.setter
    # def password(self, password):
    #     self.password_hash = generate_password_hash(password)
    #
    # def verify_password(self, password):
    #     return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return '<User %r>' % self.email

class Post(UserMixin, db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    heading = db.Column(db.String(256), index=True)
    body = db.Column(db.Text())

    def __repr__(self):
        return '<Beitrag %r>' % self.heading


db.create_all()