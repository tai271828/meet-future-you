from flask import Blueprint, render_template, request, session, redirect, url_for
import bcrypt
from user.models import User
from user.forms import RegistrationForm, LoginForm

user_page = Blueprint('user_page', __name__)

@user_page.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    error = None

    if request.method == 'POST' and form.validate():
        user = User.objects.filter(email=form.email.data).first()
        if user:
            if bcrypt.checkpw(form.password.data, user.password):
                session['email'] = user.email
                return '{} has succesfully logged in!'.format(session['email'])
            else:
                user = None
        if not user:
            error = 'Your email or password was entered incorrectly'


    return render_template('user/login.html', form=form, error=error)

@user_page.route('/logout')
def logout():
    session.pop('email')
    return redirect(url_for('user_page.login'))

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
