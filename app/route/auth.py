from flask import Blueprint, render_template

auth_bp = Blueprint('login', __name__)

@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')