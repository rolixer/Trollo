import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    SECRET_KEY = 'dev'
    PONY = {
        'provider': 'sqlite',
        'filename': os.path.join(basedir, 'trollo.db'),
        'create_db': True
    }