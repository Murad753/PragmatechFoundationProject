from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField, SubmitField

class ServicesForm(FlaskForm):
    title = StringField('title')
    icon = StringField('icon')
    submit = SubmitField()

class WorksForm(FlaskForm):
    w_title = StringField('w_title')
    w_content = TextAreaField('w_content')
    w_url = StringField('w_url')
    w_img = FileField('file')
    w_submit = SubmitField()

class ClientForm(FlaskForm):
    c_img = FileField('file')
    c_submit = SubmitField()

class LatestForm(FlaskForm):
    l_title = StringField('l_title')
    l_url = StringField('l_url')
    l_content = TextAreaField('l_content')
    l_img = FileField('file')
    l_submit = SubmitField()