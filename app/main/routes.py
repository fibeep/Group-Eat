from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from app import bcrypt
# Import Models
# Import Forms

from app import app, db


main = Blueprint('main', __name__)

# TODO:

# Homepage Route

# Create Group

# Create Restaurant

# Group Route

# Restaurant Details Route

# User Profile Page
