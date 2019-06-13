from trollo.main import bp
from trollo.main.forms import NewProjectForm

from trollo.auth.forms import LoginForm, RegisterForm

from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from trollo import db, models


@bp.route('/')
@bp.route('/index')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    login_form = LoginForm()
    register_form = RegisterForm()
    return render_template('main/index.html', loginform = login_form, \
        registerform = register_form)

@bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    projects = db.Project.select(lambda p: p.owner == current_user)
    form = NewProjectForm()
    if form.validate_on_submit():
        project = db.Project(name = form.name.data, description = form.decription.data, \
            owner = current_user.id)
        project.users += db.User.get(id = current_user.id)
        return redirect(url_for('main.home'))

    return render_template('main/home.html', form = form, projects = projects)
