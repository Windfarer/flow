from flask import jsonify, g, current_app
from flask.ext.httpauth import HTTPBasicAuth
from .models.user import User


auth = HTTPBasicAuth()
auth_token = HTTPBasicAuth()


@auth.verify_password
def verify_password(user_alias, password):
    g.user = User.find_one({'user_alias': user_alias})
    if g.user is None:
        return False
    return g.user.verify_password(password)


@auth.error_handler
def unauthorized():
    response = jsonify({'status': 401,
                        'error': 'unauthorized',
                        'message': 'please authenticate'})
    response.status_code = 401
    return response


@auth_token.verify_password
def verify_auth_token(token, unused):
    if current_app.config.get('IGNORE_AUTH') is True:
        g.user = User.find_one()
    else:
        g.user = User.verify_auth_token(token)
    return g.user is not None

@auth_token.error_handler
def unauthorized_token():
    response = jsonify({'status': 401,
                        'error': 'unauthorized',
                        'message': 'please send your authentication token'})
    response.status_code = 401
    return response