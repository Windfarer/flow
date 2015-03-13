from flask import g, current_app, request
from . import api
from ..decorators import json
from ..auth import auth_token

#TODO: register validation
@api.route('/register', methods=['POST'])
@json
def user_register():
    data = request.get_json()
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
    data = request.get_json()
    user = current_app.mongodb_conn.User.find_one(data.get('username'))
    if user:
        user.verify_password(data.get('password'))
    else:
        raise ValueError('user not exists')
    return {'res': 'login success'}
    #return login result, tell front end save token to cookie


#TODO: logout api
@auth_token.login_required
@api.route('/logout', methods=['POST'])
@json
def user_logout():
    return {'res': 'logout success'}
    #return logout result, tell front end remove token from cookie