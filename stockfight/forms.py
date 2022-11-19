from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import (
    BooleanField,
    PasswordField,
    StringField,
    SubmitField,
    SelectMultipleField
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Regexp,
    ValidationError
)

from stockfight import models


VALID_USERNAME = [DataRequired(), Length(min=1, max=32), Regexp(r'^[\w.@+-]+$')]
VALID_EMAIL = [DataRequired(), Email(), Length(min=5, max=320)]
VALID_PASSWORD = [DataRequired(), Length(min=1, max=32)]


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=VALID_USERNAME)
    email = StringField('Email', validators=VALID_EMAIL)
    password = PasswordField('Password', validators=VALID_PASSWORD)
    confirm_password = PasswordField('Confirm', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = models.User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists.')

    def validate_email(self, email):
        user = models.User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists.')


class SignInForm(FlaskForm):
    email = StringField('Email', validators=VALID_EMAIL)
    password = PasswordField('Password', validators=VALID_PASSWORD)
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
