from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
    email = StringField('Your email address', validators= [DataRequired(),Email() ])
    username = StringField('Enter your user name', validators= [DataRequired()])
    password = PasswordField('Password', validators =[ DataRequired(), EqualTo('password_confirm', message = 'Password does not match')])
    password_confirm = PasswordField('Password', validators =[DataRequired()])
    submit = SubmitField('Sign Up')
    
    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError(' Their is an account with that email')
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
  