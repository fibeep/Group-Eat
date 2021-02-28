from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from app import bcrypt
from app.models import User, Group, Restaurant
from app.auth.forms import LoginForm, SignUpForm
from app.main.forms import RestaurantForm, GroupForm, JoinGroupForm
# Import Forms

from app import app, db


main = Blueprint('main', __name__)

# TODO:

# Homepage Route
@main.route('/')
def homepage():
    return render_template('base.html')
# Create Group

# Create Restaurant

# Group Route

# Restaurant Details Route

# User Profile Page
