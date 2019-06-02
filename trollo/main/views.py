from trollo.main import bp
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from trollo.auth.forms import LoginForm, RegisterForm

@bp.route('/')
@bp.route('/index')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    login_form = LoginForm()
    register_form = RegisterForm()
    return render_template('main/index.html', loginform = login_form, \
        registerform = register_form)

@bp.route('/home')
@login_required
def home():
    return render_template('main/home.html')



# @bp.route('/project/<int: id>')
# @bp.route('/add/<int: list_id>')
# @bp.route('/remove')
# @bp.route('/')