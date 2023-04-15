"""
The secrets Blueprint handles secrets.
"""
from flask import Blueprint

secrets_blueprint = Blueprint('secrets', __name__, template_folder='templates')

from . import routes
