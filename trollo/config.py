import os
from . import app

config = dict(
    DEBUG=True,
    SECRET_KEY='dev',
    PONY = {
        'provider': 'sqlite',
        'filename': os.path.join(app.instance_path,'trollo.db'),
        'create_db': True
    }
)