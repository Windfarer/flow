from flask import Blueprint, current_app, g

from ..auth import auth_token


api = Blueprint("api", __name__)


@api.before_request
@auth_token.auth_required
def before_request():
    if current_app.config.get("IGNORE_AUTH"):
        g.user = current_app.mongodb_conn.User.find_one()
    pass


@api.after_request
def after_request(rv):
    return rv

from . import project, task, user
from .. import error_handlers
