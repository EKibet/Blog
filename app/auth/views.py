from flask import render_template,flash
from flask_login import current_user, login_user, logout_user, login_required
from . import auth
from .forms import RegistrationForm,LoginForm
from app.models import User
from werkzeug.urls import url_parse
from . import auth
from app import db


@auth.route('/')
def index():
    registration_form = RegistrationForm()
    login_form = LoginForm()
    return render_template('index.html',registration_form=registration_form, login_form=login_form)

##################Registration route section#############
@auth.route('/register', methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    registration_form = RegistrationForm()
    login_form = LoginForm()
    if registration_form.validate_on_submit():
        user = User(username=registration_form.username.data, email=registration_form.email.data)
        user.set_password(registration_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successfull!')
        # mail_message("Welcome to RestMe blog","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register',registration_form=registration_form, login_form=login_form)


    '''
    first I ensure that the user that invokes this route is
    not logged in. Logic inside if validate_on_submit() creates a 
    new user with the username, email and password provide, writes it to the db
    and then redirects to the login prompt so that the user can ogin


    '''
##################End Registration route section#############

