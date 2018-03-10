from flask import Blueprint, render_template, request
import bcrypt
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
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        user = User(
            name=form.name.data,
            email=form.email.data,
            password=hashed_password
        )
        user.save()

        return '{} Signed up!'.format(form.name.data)
    return render_template('user/signup.html', form=form)
