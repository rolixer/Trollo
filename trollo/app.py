from flask import Flask
from flask_login import LoginManager
from pony.flask import Pony
from .config import config

app = Flask(__name__)

app.config.from_object(config)

Pony(app)
