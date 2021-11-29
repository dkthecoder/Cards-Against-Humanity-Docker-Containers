from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class AddBlackCard(FlaskForm):
    card_body = TextAreaField('Card Content', validators=[DataRequired()])
    submit = SubmitField('Add')

class AddWhiteCard(FlaskForm):
    card_body = TextAreaField('Card Content', validators=[DataRequired()])
    submit = SubmitField('Add')

class LetsPlay(FlaskForm):
    word = StringField('Word', validators=[DataRequired()])
    submit = SubmitField('Play')