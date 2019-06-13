from datetime import datetime
from flask import current_app
from flask_login import UserMixin
from pony.orm import Database, Set, Required, Optional, PrimaryKey, LongStr
from werkzeug.security import generate_password_hash, check_password_hash


from trollo import db



class User(db.Entity, UserMixin):
    id = PrimaryKey(int, auto=True)
    username = Required(str, unique = True)
    password = Required(str)
    email = Optional(str)
    project = Set('Project', reverse='owner')
    projects = Set('Project', reverse='users')
    task = Set('Task', reverse='creator')
    tasks = Set('Task', reverse='users')

    def set_password(self, password):
       self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Task(db.Entity):
    id = PrimaryKey(int, auto=True)
    creator = Required(User, reverse='task')
    task_text = Required(LongStr)
    users = Set(User, reverse='tasks')
    status = Required('Status')
    list = Required('List')
    add_date = Required(datetime)
    due_date = Optional(datetime)


class Project(db.Entity):
    _table_ = 'Projects'
    id = PrimaryKey(int, auto=True)
    name = Required(str, 25)
    description = Optional(LongStr)
    owner = Required(User, reverse='project')
    users = Set(User, reverse='projects')
    lists = Set('List')


class List(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 25)
    project = Required(Project)
    tasks = Set(Task)
    notes = Set('Note')


class Note(db.Entity):
    id = PrimaryKey(int, auto=True)
    note = Required(LongStr)
    list = Required(List)
    add_date = Required(datetime)


class Status(db.Entity):
    id = PrimaryKey(int, auto=True)
    status = Required(str)
    change_date = Optional(datetime)
    tasks = Set(Task)



db.generate_mapping(create_tables=True)
