from flask import Blueprint

colleges = Blueprint("colleges", __name__)

from . import controller