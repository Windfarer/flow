from flask import jsonify, g, current_app, request

from .models.user import User
from .decorators import json
from jwt_auth import HTTPJWTAuth

auth_token = HTTPJWTAuth()


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

