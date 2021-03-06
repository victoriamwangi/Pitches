from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash 
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(85), nullable= False)
    email = db.Column(db.String(255), unique=True, index= True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch', backref = 'users', lazy= 'dynamic')
    
    
    @classmethod
    def get_mypitches(cls, pitch):
        pitches = User.query.filter_by(pitches= pitch ).all()
        return pitches

    @property
    def password(self): 
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User{self.username}'
    
class Pitch( db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    pitch_title = db.Column(db.String(255), nullable=False)
    pitch_content = db.Column(db.String(255))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_name = db.Column(db.String, nullable= False)
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    comments = db.Column(db.String(255))
    

    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()    
    
    
    @classmethod
    def get_pitches(cls, categoryEach):
        pitch = Pitch.query.filter_by(category_name = categoryEach).all()
        return pitch
    

 


