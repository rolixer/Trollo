from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from pony.flask import Pony
from pony import orm
from config import Config

login = LoginManager()
db = orm.Database()
pony = Pony()
login.login_view = 'auth.login'
login.login_message = "Please log in"
bootstrap = Bootstrap()

def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)


    db.bind(app.config['PONY'])

    pony.init_app(app)
    login.init_app(app)
    bootstrap.init_app(app)


    from trollo.main import bp as main_bp
    app.register_blueprint(main_bp)

    from trollo.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from trollo.project import bp as project_bp
    app.register_blueprint(project_bp)


    return app

from trollo import db

@login.user_loader
def load_user(user_id):
    return db.User.get(id=user_id)