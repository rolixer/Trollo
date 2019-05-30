from flask import Blueprint

bp = Blueprint('main', __name__)

from trollo.main import views