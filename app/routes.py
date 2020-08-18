from flask import render_template, url_for, flash, redirect, request
from flask import current_app as apps
from .forms import RegistrationForm, LoginForm, LogoutForm, DeleteAccountForm, SettingsForm, CreateEventForm
from .models import User, Event
from . import db
from flask_login import login_required, current_user, logout_user, login_user, UserMixin



@apps.route("/")
@apps.route("/welcome")
def welcome():
    """
    What is seen on the welcomepage.
    All this is for like testing purposes for display on the main page.
    This all probably won't show when the welcome page is done for real.
    Fitting main page description to be added in later.
    title = header
    author + date posted ==> By author on date posted
    content = Descriptions under all that
    """
    welcomewagon={'title':'Who are we?', 'content1':'Slay the Python is an event organizer for students.',
                 'content2': 'As new students transition into college life, it can be difficult to juggle the struggles of you new life such as doing classes, making friends, and paying tuition and rent. You will find your life exploded with heavy workloads. Slay the Python offers itself as a place for students to plan out and resolve scheduling issues.'}
    return render_template('welcome.html', intro = welcomewagon)


@apps.route("/register", methods=['GET', 'POST'])
def register():
    """
    Goes to Registration form in forms.py.
    Takes all methods and validators to register.html and waits for input.
    Then it waits for validation from the submit button.
    """
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You can now log in.")
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register')


@apps.route("/login", methods=['GET', 'POST'])
def login():
    """
    Login page
    Realistically, if you have registered already, you go here.
    Takes all methods and validators to login.html and waits for input.
    Then it waits for validation from the submit button.
    """
    if current_user.is_authenticated:
        return redirect(url_for('meetings'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('meetings'))
    return render_template('login.html', title='Login', form=form)


@apps.route('/meetings')
@login_required
def meetings():
    events = Event.query.all()
    return render_template('meetings.html', events=events)


@apps.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    time = ['9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM', '9 PM',
            '10 PM']
    length = ['15 min', '30 min', '60 min']
    delete_account_form = DeleteAccountForm()
    settings_form = SettingsForm()
    email_confirmation = False
    user = User.query.filter_by(username=current_user.username).first()
    if request.method == 'POST':
        user.availability_start = settings_form.availability_start.data
        user.availability_end = settings_form.availability_end.data
        user.length = int(settings_form.length.data)
        db.session.commit()
        flash("Your changes has been saved!")
    if user.availability_start:
        settings_form.availability_start.data = user.availability_start
    if user.availability_end:
        settings_form.availability_end.data = user.availability_end
    if user.length:
        settings_form.length.data = str(user.length)
    else:
        settings_form.length.data = '15'
    return render_template('settings.html', delete_account_form=delete_account_form, settings_form=settings_form,
                           email_confirmation=email_confirmation)


@apps.route('/deleteaccount', methods=['POST'])
def deleteaccount():
    User.query.filter_by(username=current_user.username).delete()
    db.session.commit()
    logout_user()
    return redirect(url_for("welcome"))


@apps.route('/logout')
@login_required
def logout():
    """
    Logout form
    Clicking logs out account
    Its here for the future
    """
    logout_user()
    return redirect(url_for('login'))


@apps.route('/createEvent', methods=['GET', 'POST'])
def createEvent():
    form = CreateEventForm()
    if form.validate_on_submit():
        event = Event(name=form.name.data, title=form.title.data, description=form.description.data, date=form.date.data, startTime=form.startTime.data, endTime=form.endTime.data)
        db.session.add(event)
        db.session.commit()
        flash('Congratulations, you have created an event!')
        return redirect(url_for('createEvent'))
    return render_template('createEvent.html', title='Create Event', form=form)
