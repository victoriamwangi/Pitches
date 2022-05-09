from flask import render_template
from . import main
from ..models import User
from flask_login import login_required


@main.route('/')
def index():
    title = "Pitches"
    return render_template('index.html', title = title)

@main.route('/pitches/new', methods = ['GET', 'POST'])
@login_required
def new_pitch(id):
    return render_template('login.html')

