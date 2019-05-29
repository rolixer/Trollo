import os

from .models import db
from .app import app


db.bind(app.config['PONY'])
db.generate_mapping(create_tables=True)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass


@app.route('/')
@app.route('/index')
@app.route('/hello')
def hello():
    return 'Hello, World!'
