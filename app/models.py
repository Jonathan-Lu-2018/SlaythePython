from datetime import datetime
from . import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#Creates a user database with id, username, email, and hashed password columns

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    availability_start = db.Column(db.String(64))
    availability_end = db.Column(db.String(64))
    length = db.Column(db.Integer)
    events = db.relationship('Event', backref='author', lazy='dynamic')
    #the user is related to the post that they post

    def __repr__(self):
        return f'<user: {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#User information to create an event
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    title = db.Column(db.String(35), index=True, nullable=False)
    description = db.Column(db.Text, index=True, nullable=False)
    date = db.Column(db.String(256), index=True, nullable=False)
    startTime = db.Column(db.String(256), index=True, nullable=False)
    endTime = db.Column(db.String(256), index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<event: {self.name}, {self.title}, {self.description}, {self.date}, {self.startTime}, {self.endTime}'

#Provides a link to the users table since flask-login doesnt have access to database
@login.user_loader
def load_user(id):
    return User.query.get(int(id))