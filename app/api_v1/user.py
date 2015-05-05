from flask import current_app, request, g
from . import api
from ..decorators import json


@api.route("/users/:user_id")
@json
def get_users(user_id):
    user = g.user.get("_id")

    return {
        'user_id': user._id,
        'nickname': user.nickname,
        'email': user.email
    }