from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, url, Email, Length
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField

class HatData(FlaskForm):
    firstName = StringField()
    lastName = StringField()
    job = StringField()
    submit = SubmitField()