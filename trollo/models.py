from datetime import date
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
    lists = Set('List', reverse = 'user')
    card = Set('Card', reverse='creator')
    cards = Set('Card', reverse='users')

    def set_password(self, password):
       self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Card(db.Entity):
    id = PrimaryKey(int, auto=True)
    creator = Required(User, reverse='card')
    card_text = Required(LongStr)
    users = Set(User, reverse='cards')
    status = Optional('Status')
    list = Required('List')
    add_date = Required(date)
    due_date = Optional(date)


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
    cards = Set('Card')

class Status(db.Entity):
    id = PrimaryKey(int, auto=True)
    status = Required(str)
    change_date = Optional(date)
    card = Set('Card')



db.generate_mapping(create_tables=True)
