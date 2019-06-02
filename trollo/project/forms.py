from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class NewListForm(FlaskForm):
    name = StringField('Name')

class NewNoteForm(FlaskForm):

class NewTaskForm(FlaskForm):