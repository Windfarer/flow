from flask import current_app, request

from . import api
from ..decorators import json
from ..auth import auth_token

#TODO: register validation
@api.route('/register', methods=['POST'])
@json
def user_register():
    data = request.json
    user = current_app.mongodb_conn.User()
    user.username = data.get('username')
    user.email = data.get('email')
    user.set_password(data.get('password'))
    user.save()
    return {'res': 'success'}

#TODO: login api
@api.route('/login', methods=['POST'])
@json
def user_login():

    return

#TODO: logout api
@auth_token.login_required
@api.route('/logout', methods=['POST'])
@json
def user_logout():
    return