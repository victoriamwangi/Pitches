from flask import render_template
from . import main, login_manager
from models import User
from flask_login import login_required


@main.route('/')
def index():
    title = "Pitches"
    return render_template('index.html', title = title)

@main.route('/login', methods = ['GET', 'POST'])
@login_required
def new_pitch(id):
    return render_template('login.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))