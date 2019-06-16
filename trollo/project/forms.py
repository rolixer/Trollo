from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Optional

from trollo import models, db

class NewListForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Add new list')

    def validate_name(self, name):
        list = db.List.get(name = name.data)
        if list is not None:
            raise ValidationError('List already exists')

class NewCardForm(FlaskForm):
    card = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField('Add new card')

class EditCardForm(FlaskForm):
    card = TextAreaField('', validators=[DataRequired()])
    status = StringField('Status', validators=[Optional()])
    due_date = DateField('Due date', validators=[Optional()])

    submit = SubmitField("Save")
