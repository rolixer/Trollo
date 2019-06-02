from trollo.project import bp
# from trollo.project import

from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from trollo import db, models

@login_required
@bp.route('/project/<id>')
def project(id):
    return id