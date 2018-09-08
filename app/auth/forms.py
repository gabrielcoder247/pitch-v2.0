from flask_wtf import FlaskForm
from wtforms import StringField, passwordField,SubmitField
from wtforms.validators import Required, Email, EqualTo
from  ..models import User
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('password',validators = [Required(),EqualTo('password_confirm',message = 'passwords must match')])
    password_confirm = passwordField('Confirm passwords' validators = [Required()])
    submit = SubmitField('Sign Up')