from flask import current_app, request

from . import api
from ..decorators import json


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


@api.route('/login', methods=['POST'])
@json
def user_login(data):
    return


@api.route('/logout', methods=['POST'])
@json
def user_logout(data):
    return