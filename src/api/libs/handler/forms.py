from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class CredentialsForm(FlaskForm):
    TWITTER_APP_KEY = StringField('TWITTER_APP_KEY', validators=[DataRequired(), Length(min=10)])
    TWITTER_APP_KEY_SECRET = StringField('TWITTER_APP_KEY_SECRET', validators=[DataRequired(), Length(min=10)])
    TWITTER_ACCESS_TOKEN = StringField('TWITTER_ACCESS_TOKEN', validators=[DataRequired(), Length(min=10)])
    TWITTER_ACCESS_TOKEN_SECRET = StringField('TWITTER_ACCESS_TOKEN_SECRET', validators=[DataRequired(), Length(min=10)])
    HASHTAGS = StringField('HASHTAGS', validators=[DataRequired(), Length(min=2)])
    REGISTRAR = SubmitField('Registrar')

