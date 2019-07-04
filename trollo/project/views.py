from datetime import datetime

from trollo.project import bp
from trollo.project.forms import NewListForm, NewCardForm, EditCardForm, AddUserForm

from flask import flash, render_template, redirect, url_for
from flask_login import login_required, current_user

from trollo import db, models

@login_required
@bp.route('/project/<id>')
def project(id):
    project = db.Project.get(id = id)
    form = NewListForm()

    cardForm = NewCardForm()

    if project is not None:
        return render_template('project/main.html', project = project, \
            current_user = current_user, \
            title = project.name, form = form, \
            cardForm = cardForm)
    else:
        return redirect(url_for('main.home'))

@login_required
@bp.route('/remove_project/<id>')
def remove_project(id):
    db.Project.get(id = id).delete()

    return redirect(url_for('main.home'))


@login_required
@bp.route('/add_list/<p_id>', methods=['GET', 'POST'])
def add_list(p_id):
    form = NewListForm()

    if form.validate_on_submit():
        db.List(name = form.name.data, project = p_id)
    else:
        flash('List already exists')

    return redirect(url_for('project.project', id = p_id))

@login_required
@bp.route('/remove_list/<l_id>')
def remove_list(l_id):
    project = db.List.get(id = l_id).project
    db.List.get(id = l_id).delete()

    return redirect(url_for('project.project', id = project.id))


@login_required
@bp.route('/add_card/<l_id>', methods=['GET', 'POST'])
def add_card(l_id):
    form = NewCardForm()
    project = db.List.get(id = l_id).project
    if form.validate_on_submit():
        db.Card(card_text = form.card.data, list = l_id, creator = current_user, \
             add_date = datetime.now())

    return redirect(url_for('project.project', id = project.id))

@login_required
@bp.route('/remove_card/<c_id>')
def remove_card(c_id):
    project = db.Card.get(id = c_id).list.project
    db.Card.get(id = c_id).delete()

    return redirect(url_for('project.project', id = project.id))

@login_required
@bp.route('/edit_card/<c_id>', methods=['GET', 'POST'])
def edit_card(c_id):
    project = db.Card.get(id = c_id).list.project
    form = EditCardForm()
    card = db.Card.get(id = c_id)

    if form.validate_on_submit():
        if form.status.data is not "":
            if card.status is None:
                status = db.Status(status = form.status.data, change_date = datetime.now().date())
            else:
                if card.status.status == form.status.data:
                    status = card.status
                else:
                    status = db.Status(status = form.status.data, change_date = datetime.now().date())
            card.set(card_text = form.card.data, due_date = form.due_date.data, status = status)

        card.set(card_text = form.card.data, due_date = form.due_date.data)

        return redirect(url_for('project.project', id = project.id))

    form.card.data = card.card_text
    if card.status is not None:
        form.status.data = card.status.status
    form.due_date.data = card.due_date
    form.submit.label.text = "Save"


    return render_template('project/edit_card.html' \
        , project = project, form = form, id = c_id)

@login_required
@bp.route('/project/<p_id>/users', methods=['GET', 'POST'])
def users(p_id):
    project = db.Project.get(id = p_id)

    form = AddUserForm()

    if form.validate_on_submit():
        project.users += db.User.get(username = form.user.data)
    return render_template('project/users.html', project = project, \
        current_user = current_user, form = form)

@login_required
@bp.route('/project/<p_id>/remove_user/<u_id>')
def remove_user(p_id, u_id):
    project = db.Project.get(id = p_id)
    user = db.User.get(id = u_id)

    project.users -= user

    return redirect(url_for('project.project', id = project.id))


@login_required
@bp.route('/quit_project/<p_id>')
def quit_project(p_id):
    project = db.Project.get(id = p_id)
    user = db.User.get(id = current_user.id)

    project.users -= user

    return redirect(url_for('main.home'))