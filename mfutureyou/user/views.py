from flask import Blueprint, render_template, request
from user.models import User
from user.forms import RegistrationForm

user_page = Blueprint('user_page', __name__)

@user_page.route('/login')
def login():
    return render_template('base.html')

@user_page.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        return '{} Signed up!'.format(form.name.data)
    return render_template('user/signup.html')
