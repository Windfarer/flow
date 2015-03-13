from flask import Blueprint

api = Blueprint('api', __name__)


@api.before_request
def before_request():
    pass


@api.after_request
def after_request(rv):
    return rv

from . import group, task, user
