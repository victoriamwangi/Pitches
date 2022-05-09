from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db
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

    return render_template("profile/profile.html", user=user)


@main.route('/pitches/new', methods = ['GET', 'POST'])
@login_required
def new_pitch(id):
    form = PitchForm
    if form.validate_on_submit():
        title = form.title.data
        pitch_content = form.pitch_content.data

        # Updated review instance
        new_pitch = Pitch(title = title, pitch=pitch_content,user=current_user)

        # save review method
        new_pitch.save_pitch()
        return redirect(url_for('.profile',id = id ))

    
    return render_template('new_pitch.html',title = title, pitch_form=form)




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