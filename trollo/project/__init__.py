from flask import Blueprint

bp = Blueprint('project', __name__)

from trollo.project import views