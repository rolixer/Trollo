from trollo.main import bp
from flask import render_template

@bp.route('/')
def index():
    return render_template('main/index.html')

# @bp.route('/home')
# @bp.route('/project/<int: id>')
# @bp.route('/add/<int: list_id>')
# @bp.route('/remove')
# @bp.route('/')