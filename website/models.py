from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(150))
    state = db.Column(db.String(50))
    zip_code = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    address = db.relationship('Address')

