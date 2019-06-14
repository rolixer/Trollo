from datetime import datetime

from trollo.project import bp
from trollo.project.forms import NewListForm, NewNoteForm, NewTaskForm

from flask import flash, render_template, redirect, url_for
from flask_login import login_required, current_user

from trollo import db, models

@login_required
@bp.route('/project/<id>')
def project(id):
    project = db.Project.get(id = id)
    lists = db.List.select(lambda l: l.project == project)
    form = NewListForm()

    noteForm = NewNoteForm()
    taskForm = NewTaskForm()

    return render_template('project/main.html', project = project, \
         lists = lists, \
         title = project.name, form = form, \
         noteForm = noteForm, taskForm = taskForm)

@login_required
@bp.route('/add_list/<p_id>', methods=['GET', 'POST'])
def add_list(p_id):
    form = NewListForm()

    if form.validate_on_submit():
        db.List(name = form.name.data, project = p_id )
    else:
        flash('List already exists')

    return redirect(url_for('project.project', id = p_id))

@login_required
@bp.route('/add_note/<l_id>', methods=['GET', 'POST'])
def add_note(l_id):
    form = NewNoteForm()
    project = db.List.get(id = l_id).project
    if form.validate_on_submit():
        db.Note(note = form.note.data, list = l_id, add_date = datetime.now())

    return redirect(url_for('project.project', id = project.id))

@login_required
@bp.route('/add_task/<l_id>', methods=['GET', 'POST'])
def add_task(l_id):
    return "zadanko"