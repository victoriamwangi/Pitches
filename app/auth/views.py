from flask import render_template, redirect, url_for, flash, request
from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user, login_required, logout_user

@auth.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.profile'))
        flash('Invalid username or password')
        
        
    return render_template('auth/login.html', login_form = login_form)

@auth.route('register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    title = 'New Account'
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', registration_form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))