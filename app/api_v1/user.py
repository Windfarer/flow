from flask import current_app, request, g
from . import api
from ..decorators import json


@api.route("/users")
def get_users():
    pass


@api.route("/test", methods=["GET"])
@json
def test():
    print(g.user)
    return {"res": "res234234"}