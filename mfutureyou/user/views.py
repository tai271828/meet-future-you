from flask import Blueprint

user_page = Blueprint('user_page', __name__)

@user_page.route('/login')
def login():
    return "This is the login page"

