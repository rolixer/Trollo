from trollo.auth import bp
from trollo.main.forms import LoginForm, RegisterForm
from trollo import db, models

from flask import request, flash, redirect, url_for, render_template
from flask_login import login_user, current_user, logout_user

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse



@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if not current_user.is_anonymous:
        return redirect(url_for('main.home'))
    if form.validate_on_submit():
        user = db.User.get(username = form.username.data )
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('auth.login'))

        login_user(user, remember=form.rememberme.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth/login.html', loginform = form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if current_user is not None:
        return redirect(url_for('main.home'))
    if form.validate_on_submit():
        user = db.User(username = form.username.data, email = form.email.data, password=generate_password_hash(form.password.data))
        flash("Registration success, u can log in now")
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', registerform = form)

@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('main.index'))
