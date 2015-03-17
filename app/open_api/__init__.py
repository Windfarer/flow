from flask import Blueprint, request, current_app

from ..decorators import json
from ..exceptions import ValidationError

open_api = Blueprint('open_api', __name__)


@open_api.route('/register', methods=['POST'])
@json
def create_user():
    data = request.get_json()
    data['email'] = data['email'].lower()

    if current_app.mongodb_conn.User.find_one_by_email(data['email']):
        raise ValidationError('user is exists')
    else:
        user = current_app.mongodb_conn.User()
        user.username = data.get('username')
        user.email = data.get('email')
        user.set_password(data.get('password'))
        user.save()
    return {'res': 'success'}


@open_api.route('/get_token', methods=['POST'])
@json
def login():
    data = request.get_json()
    data['email'] = data['email'].lower()

    user = current_app.mongodb_conn.User.find_one_by_email(data.get('email'))
    if user:
        user.verify_password(data.get('password'))
    else:
        raise ValidationError('user not exists')
    return {'res': 'login success', 'token': user.generate_auth_token()}