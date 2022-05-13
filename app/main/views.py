from unicodedata import category
from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db, photos
from ..models import User, Pitch
from flask_login import login_required, current_user
from .forms import PitchForm, UpdateProfile



@main.route('/')
def index():
    pitches = Pitch.query.all()    
    title = "Pitches"
    pitches = Pitch.query.all()
    science = Pitch.query.filter_by(category_name='science').all()
    computing = Pitch.query.filter_by(category_name='computing').all()
    business = Pitch.query.filter_by(category_name='business').all()
    fashion = Pitch.query.filter_by(category_name='fashion').all()
    
  
    return render_template('index.html',science = science,computing= computing,  business=business, fashion = fashion,pitches = pitches, title= title)


@main.route('/categories/<categoryeach>')
def categories(categoryeach):
    category = Pitch.get_pitches(categoryeach)
    title = f'{categoryeach}'
    
    return render_template('categories.html', title= title, category=category)


@main.route('/add/<uname>/pitches/new')
@login_required
def add(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        return redirect(url_for('auth/login.html', uname=user.username))
            
    return render_template('new_pitch.html')

@main.route('/user/<uname>')
def profile(uname):
    user = current_user
    pitches = Pitch.query.filter_by(user_id = current_user.id).all()
    
    
 
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=uname, pitches= pitches)
@main.route('/pitches')
@login_required
def profpitch():
    # user = User.query.filter_by(username=id).first()
    # pitches = Pitch.get_mypitches(pitches)  
    pitches = Pitch.query(user_id = current_user.id).all()
    message = "lets see"
    if current_user is None:
        abort(404)

    return render_template("profile/pitchCats.html",  pitches= pitches, message= message, userName = current_user.username)


@main.route('/user/<uname>/pitches/new', methods = ['GET', 'POST'])
@login_required
def new_pitch(uname):
    user = User.query.filter_by(username=uname).first()
    
    if user is None:
        abort(404)
  
    form = PitchForm()
  

    if form.validate_on_submit():      
        new_pitch = Pitch(pitch_title = form.pitch_title.data, pitch_content = form.pitch_content.data, user_id=user.id, category_name= form.category_name.data) #, category_id =Category.category_name
        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))
    return render_template('new_pitch.html', pitch_form=form, user=uname )

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


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))


