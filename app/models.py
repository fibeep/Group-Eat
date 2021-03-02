from sqlalchemy_utils import URLType

from app import db
from flask_login import UserMixin

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


user_group_table = db.Table('user_group_table',
                        db.Column('user_id', db.Integer,db.ForeignKey('user.id')),
                        db.Column('group_id', db.Integer,db.ForeignKey('group.id'))
                        )
user_restaurant_table = db.Table('user_restaurant_table',
                        db.Column('user_id', db.Integer,db.ForeignKey('user.id')),
                        db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id'))
                        )
group_restaurant_table = db.Table('group_restaurant_table',
                        db.Column('group_id', db.Integer, db.ForeignKey('group.id')),
                        db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id'))
                        )

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    groups = db.relationship('Group', secondary=user_group_table)
    # Restaurants Liked - Relationship

    
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #TODO:
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')
    name = db.Column(db.String(80), nullable=False)
    max_atendees = db.Column(db.Float(precision=2), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    code = db.Column(db.String(80), nullable=False, unique=True)
    atendees = db.relationship('User', secondary=user_group_table)
    restaurants = db.relationship('Restaurant', secondary=group_restaurant_table)
    

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #TODO:
    name = db.Column(db.String(80), nullable=False)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')
    location = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80), nullable=False)
    price_range = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(), nullable=False)
    photo_url = db.Column(URLType)
    group_id = db.Column(Integer, ForeignKey('group.id'))
    # Users who like it
    liked_by = db.relationship('User')



