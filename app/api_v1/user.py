from flask import current_app, request, g
from . import api
from ..decorators import json


@api.route("/users")
def get_users():
    pass
