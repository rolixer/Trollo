from trollo.main import bp
from flask import render_template
from .forms import LoginForm, RegisterForm

@bp.route('/')
@bp.route('/index')
def index():
    login_form = LoginForm()
    register_form = RegisterForm()
    return render_template('main/index.html', loginform = login_form, \
        registerform = register_form)

# @bp.route('/home')
# @bp.route('/project/<int: id>')
# @bp.route('/add/<int: list_id>')
# @bp.route('/remove')
# @bp.route('/')