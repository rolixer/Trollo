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
    form = NewListForm()

    noteForm = NewNoteForm()
    taskForm = NewTaskForm()

    return render_template('project/main.html', project = project, \
        current_user = current_user, \
        title = project.name, form = form, \
        noteForm = noteForm, taskForm = taskForm)

@login_required
@bp.route('/add_list/<p_id>', methods=['GET', 'POST'])
def add_list(p_id):
    form = NewListForm()

    if form.validate_on_submit():
        db.List(name = form.name.data, project = p_id, user = current_user )
    else:
        flash('List already exists')

    return redirect(url_for('project.project', id = p_id))

@login_required
@bp.route('/add_note/<l_id>', methods=['GET', 'POST'])
def add_note(l_id):
    form = NewNoteForm()
    project = db.List.get(id = l_id).project
    if form.validate_on_submit():
        db.Note(note = form.note.data, list = l_id, user = current_user, \
             add_date = datetime.now())

    return redirect(url_for('project.project', id = project.id))

@login_required
@bp.route('/remove_note/<n_id>')
def remove_note(n_id):
    project = db.Note.get(id = n_id).list.project
    db.Note.get(id = n_id).delete()

    return redirect(url_for('project.project', id = project.id))

@login_required
@bp.route('/edit_note/<n_id>', methods=['GET', 'POST'])
def edit_note(n_id):
    project = db.Note.get(id = n_id).list.project
    form = NewNoteForm()
    note = db.Note.get(id = n_id)

    if form.validate_on_submit():
        note.set(note = form.note.data)

        return redirect(url_for('project.project', id = project.id))

    form.note.data = note.note
    form.submit.label.text = "Save"


    return render_template('project/edit_note.html' \
        , project = project, form = form, id = n_id)

@login_required
@bp.route('/add_task/<l_id>', methods=['GET', 'POST'])
def add_task(l_id):
    return "zadanko"