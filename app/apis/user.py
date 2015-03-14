from flask import current_app, request, g
from . import api
from ..decorators import json


#TODO: register validation
@api.route('/user', methods=['POST'])
@json
def create_user():
    data = request.get_json()
    print(data)
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