from flask import Blueprint, request, render_template, redirect, url_for, flash
import flask
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime

import flask_login
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


@main.route('/profile')
def profile():
    groups = current_user.groups
    return render_template('profile.html', groups=groups)

# Create Group
@main.route('/create_group', methods=['GET', 'POST'])
@login_required
def create_group():
    """ This route permits group creation"""
    # IF form is submitted an valid:
    # Create new Group object + save to database,
    # flash sucess message,
    # redirect user to group page
    
    form = GroupForm()

    if form.validate_on_submit():
        new_group = Group(
          created_by = flask_login.current_user,
          name = form.name.data,
          max_atendees = form.max_atendees.data,
          location = form.location.data,
          code = form.code.data,
        )
        current_user.groups.append(new_group)
        db.session.add(new_group)
        db.session.commit()
        flash('Group was created successfully')
        return redirect(url_for('main.profile', group=new_group))
    return render_template('create_group.html', form=form)

# Group Detail

@main.route('/group/<group_id>')
@login_required
def group_details(group_id):
    group = Group.query.get(group_id)
    return render_template('group.html', group=group)

# Join Group

@main.route('/join_group', methods=['GET', 'POST'])
@login_required
def join_group():
    
    form = JoinGroupForm()
    if form.validate_on_submit():
        group = Group.query.filter_by(code=form.code.data).one()
        current_user.groups.append(group)
        print(group.atendees)
        db.session.commit()
        flash('Group was joined successfully')
        return redirect(url_for('main.profile', group=group))
    return render_template('join_group.html', form=form)

# Create Restaurant


@main.route('/create_restaurant/group/<group_id>', methods=['GET', 'POST'])
@login_required
def create_restaurant(group_id):
    print(group_id)
    form = RestaurantForm()

    if form.validate_on_submit():
       new_restaurant = Restaurant(
       name = form.name.data,
       location = form.location.data,
       type = form.type.data,
       price_range = form.price_range.data,
       description = form.description.data,
       created_by=flask_login.current_user,
       photo_url = form.photo_url.data,
       group_id=group_id)
       group_id=group_id
       group = Group.query.filter_by(id=group_id).one()
       group.restaurants.append(new_restaurant)
       db.session.add(new_restaurant)
       db.session.commit()
       flash('Restaurant updated succesfully')
       return redirect(url_for('main.restaurant_detail', restaurant_id=new_restaurant.id))

    
    return render_template('create_restaurant.html', form=form, id=group_id)

#Like Restaurant Route

# @main.route('/like_restaurant/<restaurant_id>', methods=['POST'])
# def like_restaurant(restaurant_id):
#     restaurant = Restaurant.query.get(restaurant_id)
#     restaurant.liked_by.append(current_user)
#     return url_for('main.restaurant_detail', restaurant_id=restaurant.id)

# Restaurant Details Route

@main.route('/restaurant/<restaurant_id>', methods=['GET', 'POST'])
@login_required
def restaurant_detail(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    form = RestaurantForm(obj=restaurant)

    if form.validate_on_submit():
       name = form.name.data,
       location = form.location.data,
       type = form.type.data,
       price_range = form.price_range.data,
       description = form.description.data,
       photo_url = form.photo_url.data 
       db.session.add(restaurant)
       db.session.commit()
       flash('Restaurant updated succesfully')
       return redirect(url_for('main.restaurant_detail', restaurant_id=restaurant.id))

    restaurant = Restaurant.query.get(restaurant_id)
    return render_template('restaurant_detail.html', restaurant=restaurant, form=form)

