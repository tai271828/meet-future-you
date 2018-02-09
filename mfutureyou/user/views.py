from flask import Blueprint, render_template
from user.models import User

user_page = Blueprint('user_page', __name__)

@user_page.route('/login')
def login():
    return render_template('base.html')

@user_page.route('/signup')
def signup():
    return render_template('user/signup.html')
