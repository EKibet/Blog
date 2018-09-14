from flask import render_template
from . import main
from .forms import RegistrationForm

@main.route('/')
def index():
    registration_form = RegistrationForm()
    return render_template('index.html',registration_form=registration_form)
