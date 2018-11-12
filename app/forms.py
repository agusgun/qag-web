from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class PassageForm(FlaskForm):
    passage = TextAreaField('Write me a passage!', validators=[DataRequired()])
    submit = SubmitField('I\'m done!')


class CrawlForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Crawl')
