from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, RadioField, TextAreaField, TimeField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from .models import User, Event
from . import db
from wtforms.fields.html5 import DateTimeLocalField, DateField
import email_validator

# Function that prompts the user to create an account
class RegistrationForm(FlaskForm):
    '''
    This class is used when the user wants to create an account
    '''
    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please enter a different username.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please enter a different email.')

# Function that prompts the user to login
class LoginForm(FlaskForm):
    '''
    This class is used whenever the user already has an account and wants to log in with it.
    '''
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class DeleteAccountForm(FlaskForm):
    submit = SubmitField('Delete Account')

class SettingsForm(FlaskForm):
    availability_start = SelectField("Availability start:",choices=[('9:00 AM','9:00 AM'),('10:00 AM','10:00 AM'),('11:00 AM','11:00 AM'),('12:00 PM','12:00 PM'),('1:00 PM','1:00 PM'),('2:00 PM','2:00 PM'),('3:00 PM','3:00 PM'),('4:00 PM','4:00 PM'),('5:00 PM','5:00 PM'),('6:00 PM','6:00 PM'),
                                                                   ('7:00 PM','7:00 PM'),('8:00 PM','8:00 PM'),('9:00 PM','9:00 PM'),('10:00 PM','10:00 PM')])
    availability_end = SelectField("Availability end:",choices=[('9:00 AM','9:00 AM'),('10:00 AM','10:00 AM'),('11:00 AM','11:00 AM'),('12:00 PM','12:00 PM'),('1:00 PM','1:00 PM'),('2:00 PM','2:00 PM'),('3:00 PM','3:00 PM'),('4:00 PM','4:00 PM'),('5:00 PM','5:00 PM'),('6:00 PM','6:00 PM'),
                                                                   ('7:00 PM','7:00 PM'),('8:00 PM','8:00 PM'),('9:00 PM','9:00 PM'),('10:00 PM','10:00 PM')])
    length = SelectField("Length:",choices=[("15",'15 min'), ('30','30 min'), ('60','60 min')])
    submit = SubmitField('Save Changes')
    email_confirmation = BooleanField('Yes')
    email_rejection = BooleanField('No')


# Function that prompts the user to logout
class LogoutForm(FlaskForm):
    '''
    This class is used when the user wants to log off from their account.
    '''
    submit = SubmitField('Logout')

class CreateEventForm(FlaskForm):
    name = StringField('Full name:', validators=[DataRequired()])
    title = StringField('Event Title:', validators=[DataRequired()])
    description = TextAreaField('Description:', validators=[DataRequired()])
    date = DateField('Date:', validators=[DataRequired()])
    startTime = SelectField('Start Time:', choices=[('9:00 AM','9:00 AM'), ('9:15 AM', '9:15 AM'), ('9:30 AM', '9:30 AM'), ('9:45 AM', '9:45 AM'),('10:00 AM','10:00 AM'),  ('10:15 AM', '10:15 AM'), ('10:30 AM', '10:30 AM'), ('10:45 AM', '10:45 AM'), 
                                                    ('11:00 AM','11:00 AM'), ('11:15 AM', '11:15 AM'), ('11:30 AM', '11:30 AM'), ('11:45 AM', '11:45 AM'),('12:00 PM','12:00 PM'), ('12:15 PM', '12:15 PM'), ('12:30 PM', '12:30 PM'), ('12:45 PM', '12:45 PM'),('1:00 PM','1:00 PM'), ('1:15 PM', '1:15 PM'), ('1:30 PM', '1:30 PM'), ('1:45 PM', '1:45 PM'),
                                                    ('2:00 PM','2:00 PM'),  ('2:15 PM', '2:15 PM'), ('2:30 PM', '2:30 PM'), ('2:45 PM', '2:45 PM'),('3:00 PM','3:00 PM'), ('3:15 PM', '3:15 PM'), ('3:30 PM', '3:30 PM'), ('3:45 PM', '3:45 PM'),('4:00 PM','4:00 PM'), ('4:15 PM', '4:15 PM'), ('4:30 PM', '4:30 PM'), ('4:45 PM', '4:45 PM'), 
                                                    ('5:00 PM','5:00 PM'), ('5:15 PM', '5:15 PM'), ('5:30 PM', '5:30 PM'), ('5:45 PM', '5:45 PM'),('6:00 PM','6:00 PM'),('6:15 PM', '6:15 PM'), ('6:30 PM', '6:30 PM'), ('6:45 PM', '6:45 PM'), ('7:00 PM','7:00 PM'), ('7:15 PM', '7:15 PM'), ('7:30 PM', '7:30 PM'), ('7:45 PM', '7:45 PM'),
                                                    ('8:00 PM','8:00 PM'), ('8:15 PM', '8:15 PM'), ('8:30 PM', '8:30 PM'), ('8:45 PM', '8:45 PM'),('9:00 PM','9:00 PM'), ('9:15 PM', '9:15 PM'), ('9:30 PM', '9:30 PM'), ('9:45 PM', '9:45 PM'),('10:00 PM','10:00 PM')])
    endTime = SelectField('End Time:',  choices=[('9:00 AM','9:00 AM'), ('9:15 AM', '9:15 AM'), ('9:30 AM', '9:30 AM'), ('9:45 AM', '9:45 AM'),('10:00 AM','10:00 AM'),  ('10:15 AM', '10:15 AM'), ('10:30 AM', '10:30 AM'), ('10:45 AM', '10:45 AM'), 
                                                    ('11:00 AM','11:00 AM'), ('11:15 AM', '11:15 AM'), ('11:30 AM', '11:30 AM'), ('11:45 AM', '11:45 AM'),('12:00 PM','12:00 PM'), ('12:15 PM', '12:15 PM'), ('12:30 PM', '12:30 PM'), ('12:45 PM', '12:45 PM'),('1:00 PM','1:00 PM'), ('1:15 PM', '1:15 PM'), ('1:30 PM', '1:30 PM'), ('1:45 PM', '1:45 PM'),
                                                    ('2:00 PM','2:00 PM'),  ('2:15 PM', '2:15 PM'), ('2:30 PM', '2:30 PM'), ('2:45 PM', '2:45 PM'),('3:00 PM','3:00 PM'), ('3:15 PM', '3:15 PM'), ('3:30 PM', '3:30 PM'), ('3:45 PM', '3:45 PM'),('4:00 PM','4:00 PM'), ('4:15 PM', '4:15 PM'), ('4:30 PM', '4:30 PM'), ('4:45 PM', '4:45 PM'), 
                                                    ('5:00 PM','5:00 PM'), ('5:15 PM', '5:15 PM'), ('5:30 PM', '5:30 PM'), ('5:45 PM', '5:45 PM'),('6:00 PM','6:00 PM'),('6:15 PM', '6:15 PM'), ('6:30 PM', '6:30 PM'), ('6:45 PM', '6:45 PM'), ('7:00 PM','7:00 PM'), ('7:15 PM', '7:15 PM'), ('7:30 PM', '7:30 PM'), ('7:45 PM', '7:45 PM'),
                                                    ('8:00 PM','8:00 PM'), ('8:15 PM', '8:15 PM'), ('8:30 PM', '8:30 PM'), ('8:45 PM', '8:45 PM'),('9:00 PM','9:00 PM'), ('9:15 PM', '9:15 PM'), ('9:30 PM', '9:30 PM'), ('9:45 PM', '9:45 PM'),('10:00 PM','10:00 PM')])
    submit = SubmitField('Create Event')