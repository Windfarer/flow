from flask import jsonify, g, current_app
from flask.ext.httpauth import HTTPBasicAuth
from .models.user import User


auth = HTTPBasicAuth()
auth_token = HTTPBasicAuth

@auth.verify_password
def verify_password(user_alias, password):
    g.user = User.find_one()