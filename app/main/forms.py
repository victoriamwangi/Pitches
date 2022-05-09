from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PitchForm(FlaskForm):
    title = StringField("Pitch Title", validators=[DataRequired()])
    pitch_content = TextAreaField("Pitch Content", validators=[DataRequired()])
    submit = SubmitField('Submit')
    