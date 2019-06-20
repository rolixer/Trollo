from datetime import datetime
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

    def validate_due_date(self, date):
        if date.data < datetime.now().date():
            raise ValidationError('Due date can\'t be in past')

    submit = SubmitField("Save")

class AddUserForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Add new user')

    def validate_user(self, user):
        user = db.User.get(username = user.data)

        if user is None:
            raise ValidationError('User don\'t exists')
