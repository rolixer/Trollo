from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from trollo import models, db

class NewListForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Add new list')

    def validate_name(self, name):
        list = db.List.get(name = name.data)
        if list is not None:
            raise ValidationError('List already exists')

class NewNoteForm(FlaskForm):
    note = TextAreaField('Note')
    submit = SubmitField('Add new note')

class NewTaskForm(FlaskForm):
    task = TextAreaField('Task')
    due_date = DateField('Due date')
    submit = SubmitField('Add new task')