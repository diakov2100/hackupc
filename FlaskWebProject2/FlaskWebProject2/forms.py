from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, IntegerField
from wtforms.validators import Required
class Messange(FlaskForm):
    msg = TextField('messange', validators = [Required()])