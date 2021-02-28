from sqlalchemy_utils import URLType

from app import db
from flask_login import UserMixin

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    #TODO:
    # Groups Belonging - Relationship
    # Restaurants Liked - Relationship

    
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #TODO:
    created_by = db.relationship('User')
    name = db.Column(db.String(80), nullable=False, unique=True)
    money_goal = db.Column(db.Float(precision=2), nullable=False)
    location = db.Column(db.String(80), nullable=False, unique=True)
    code = db.Column(db.String(80), nullable=False, unique=True)
    # End Date
    # Atendees - Relationship
    # Restaurants - Relationship

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #TODO:
    name = db.Column(db.String(80), nullable=False, unique=True)
    created_by = db.relationship('User')
    location = db.Column(db.String(80), nullable=False, unique=True)
    type = db.Column(db.String(80), nullable=False, unique=True)
    price_rang = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(), nullable=False)
    photo_url = db.Column(URLType)
    # Users who like it


user_group_table = db.Table('user_group_table',
                            db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                            db.Column('group_id', db.Integer, db.ForeignKey('group.id')))
user_restaurant_table = db.Table('user_restaurant_table',
                            db.Column('user_id', db.Integer,db.ForeignKey('user.id')),
                            db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id')))
group_restaurant_table = db.Table('group_restaurant_table',
                            db.Column('group_id', db.Integer,db.ForeignKey('group.id')),
                            db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id')))
