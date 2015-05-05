from flask import jsonify, g, current_app, request
from flask.ext.httpauth import HTTPBasicAuth

from .models.user import User
from .decorators import json
from jwt_auth import HTTPJWTAuth


auth = HTTPBasicAuth()
auth_token = HTTPJWTAuth()


@auth.verify_password
def verify_password(username, password):
    g.user = current_app.mongodb_conn.User.find_one({"username": username})
    if g.user is None:
        return False
    return g.user.verify_password(password)


@auth.error_handler
@json
def unauthorized():
    response = {
        "status": 401,
        "error": "unauthorized",
        "message": "please authenticate"
    }
    return response, 401


@auth_token.verify_token
def verify_auth_token(token):
    if current_app.config.get("IGNORE_AUTH") is True:
        g.user = current_app.mongodb_conn.User.find_one()
    else:
        g.user = User.verify_auth_token(token)
    return g.user is not None


@auth_token.error_handler
@json
def unauthorized_token():
    response = {
        "status": 401,
        "error": "unauthorized",
        "message": "please send your authentication token"
    }
    return response, 401

