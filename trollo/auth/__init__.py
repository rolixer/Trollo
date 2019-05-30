from flask import Blueprint

bp = Blueprint('auth', __name__)

from trollo.auth import views