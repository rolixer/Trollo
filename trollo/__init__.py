from flask import Flask
from flask_login import LoginManager
from pony.flask import Pony
from config import Config
from .models import db

login = LoginManager()
login.login_view = 'auth.login'
login.login_message = "Please log in"

def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)


    db.bind(app.config['PONY'])
    db.generate_mapping(create_tables=True)

    Pony(app)
    login.init_app(app)

    from .main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

from trollo import models, db

@login.user_loader
def load_user(user_id):
    return db.User.get(id=user_id)