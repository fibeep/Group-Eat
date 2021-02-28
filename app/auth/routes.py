from flask import Blueprint
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from app import bcrypt
# Import Models
# Import Forms

from app import app, db
auth = Blueprint('auth', __name__)


# TODO: 

# Create your routes here.

# Create Signup

# Create Login

# Create Log Out
