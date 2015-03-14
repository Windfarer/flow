from flask import Blueprint, current_app, g

api = Blueprint('api', __name__)


@api.before_request
def before_request():
    if current_app.config.get('IGNORE_AUTH'):
        g.user = current_app.mongodb_conn.User.find_one()
    pass


@api.after_request
def after_request(rv):
    return rv

from . import group, task, user, error
