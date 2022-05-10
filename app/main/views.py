from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db, photos
from ..models import User, Pitch
from flask_login import login_required, current_user
from .forms import PitchForm, UpdateProfile



@main.route('/')
def index():
    title = "Pitches"
    return render_template('index.html', title = title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=uname)


@main.route('/user/<uname>/pitches/new', methods = ['GET', 'POST'])
@login_required
def new_pitch(uname):
    user = User.query.filter_by(username=uname).first()
  
    
    # id_user = User.query.filter_by(i).first()
    
    if user is None:
        abort(404)
  
    form = PitchForm()
    if form.validate_on_submit():
       
        
        new_pitch = Pitch(pitch_title = form.pitch_title.data, pitch_content = form.pitch_content.data, user_id=user.id)
        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username ))

    
    return render_template('new_pitch.html', pitch_form=form, user=uname)

@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)