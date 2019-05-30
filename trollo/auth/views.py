from trollo.auth import bp
from trollo.main.forms import LoginForm
from trollo import db, models

from flask import request, flash, redirect, url_for, render_template
from flask_login import login_user


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.User.get(username = form.username.data )
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('auth.login'))

        login_user(user, remember=form.rememberme.data)
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', loginform = form)