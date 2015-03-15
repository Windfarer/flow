from flask import current_app, request, g
from . import api
from ..decorators import json
from ..utils.validator import email_validator, username_validator

#TODO: register validation
@api.route('/user', methods=['POST'])
@json
def create_user():
    data = request.get_json()

    email_validator(data.get('email'))
    username_validator(data.get('username'))

    user = current_app.mongodb_conn.User()
    user.username = data.get('username')
    user.email = data.get('email')
    user.set_password(data.get('password'))
    user.save()
    return {'res': 'success'}


@api.route('/test', methods=['GET'])
@json
def test():
    print(g.user)
    return {'res': 'res234234'}