from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class NewProjectForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    decription = TextAreaField('Description')
    submit = SubmitField('Add new Project')
