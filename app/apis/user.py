from flask import current_app, request, g
from . import api
from ..decorators import json
from ..auth import auth_token

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




#TODO: login api --move to app layer
@api.route('/login', methods=['POST'])
@json
def login():
    data = request.get_json()
    user = current_app.mongodb_conn.User.find_one_by_username(data.get('username'))
    if user:
        user.verify_password(data.get('password'))
    else:
        raise ValueError('user not exists')
    return {'res': 'login success', 'token': user.generate_auth_token()}
    #return login result, tell front end save token to cookie

@auth_token.auth_required
@api.route('/test', methods=['GET'])
@json
def test():
    print(g.user)
    return {'res': 'res234234'}