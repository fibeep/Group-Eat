from re import L
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError, URL
from wtforms.fields.core import FloatField
from app import bcrypt
from app.models import Group, Restaurant
# Import Models

#TODO:

# Join Group Form

class JoinGroupForm(FlaskForm):
    """ Form for joining a group """
    code = StringField("Code", validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField('Submit!')
    def validate_code(self, code):
        group = Group.query.filter_by(code=code.data).first()
        if not group:
            raise ValidationError(
                'That code is incorrect. Please try again.')

# Create Group Form

class GroupForm(FlaskForm):
    """ Form for creating a group"""
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=80)])
    code = StringField("Code", validators=[DataRequired(), Length(min=3, max=80)])
    max_atendees = FloatField("Max Atendees")
    location = StringField("Location", validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField('Submit!')

    def validate_code(self, code):
        group = Group.query.filter_by(code=code.data).first()
        if group:
            raise ValidationError(
                'That code is taken. Please choose a different one.')

# Create Restaurant

class RestaurantForm(FlaskForm):
    """ Form for creating a Restaurant"""
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=80)])
    location = StringField("Location", validators=[DataRequired(), Length(min=3, max=80)])
    type = StringField("Type", validators=[DataRequired(), Length(min=3, max=80)])
    price_range = StringField("Title", validators=[DataRequired(), Length(min=3, max=80)])
    description = TextAreaField("Description", validators=[DataRequired(), Length(min=3, max=10000)])
    photo_url = StringField("Photo Url", validators=[URL()])
    submit = SubmitField('Submit!')
