from sqlalchemy_utils import URLType

from app import db
from flask_login import UserMixin

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = username = db.Column(db.String(80), nullable=False, unique=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    #TODO:
    # Groups Belonging - Relationship
    # Restaurants Liked - Relationship
    
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #TODO:
    # Created By
    # Name
    # End Date
    # Max Num of PPL
    # Location
    # Special Code
    # Atendees - Relationship
    # Restaurants - Relationship

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #TODO:
    # Created By
    # Users who like it
    # Location
    # Type
    # Price
    # Description
    # Picutre

user_group_table = db.Table()
user_restaurant_table = db.Table()
group_restaurant_table = db.Table()
