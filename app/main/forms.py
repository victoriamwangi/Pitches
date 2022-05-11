
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class PitchForm(FlaskForm):
    pitch_title = StringField("Pitch Title", validators=[DataRequired()])
    pitch_content = TextAreaField("Pitch Content", validators=[DataRequired()])
    category_name = SelectField('Category', choices=[('science','science'), ('computing','computing'), ('business','business'), ('fashion','fashion')],  validators=[DataRequired()]) 
    submit = SubmitField('Submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[DataRequired()])
    submit = SubmitField('Submit')