from datetime import date
from flask import current_app
from pony.orm import Database, Set, Required, Optional, PrimaryKey, LongStr


db = Database()


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Required(str)
    password = Required(str)
    salt = Required(str)
    email = Optional(str)
    project = Set('Project', reverse='owner')
    projects = Set('Project', reverse='users')
    task = Set('Task', reverse='creator')
    tasks = Set('Task', reverse='users')


class Task(db.Entity):
    id = PrimaryKey(int, auto=True)
    creator = Required(User, reverse='task')
    task_text = Optional(LongStr)
    users = Set(User, reverse='tasks')
    status = Required('Status')
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
    tasks = Set(Task)
    notes = Set('Note')


class Note(db.Entity):
    id = PrimaryKey(int, auto=True)
    note = Required(LongStr)
    list = Required(List)
    add_date = Required(date)


class Status(db.Entity):
    id = PrimaryKey(int, auto=True)
    status = Required(str)
    change_date = Optional(date)
    tasks = Set(Task)


