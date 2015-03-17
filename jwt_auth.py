from functools import wraps
from flask import request, make_response


class HTTPJWTAuth(object):

    def __init__(self):
        def default_get_token(token):
            return None

        def default_auth_error():
            return "Unauthorized Access"

        self.token = "Authorization Required"
        self.get_token(default_get_token)
        self.error_handler(default_auth_error)

    def get_token(self, auth):
        data = str(auth).split()  # first one is method, second one is token
        return data[1]

    def generate_token(self, f):
        self.generate_token_callback = f
        return f

    def verify_token(self, f):
        self.verify_token_callback = f
        return f

    def authenticate_header(self):
        return 'Bearer {}'.format(self.token)

    def authenticate_token(self, token):
        if self.verify_token_callback(token):
            return True
        return False

    def auth_required(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            auth = request.headers.get('Authorization')
            if request.method != 'OPTIONS':   # avoid 401 when request method is OPTIONS
                if auth:
                    token = self.get_token(auth)
                else:
                    token = None
                if not self.authenticate_token(token):
                    return self.auth_error_callback()
            return f(*args, **kwargs)
        return wrapper


    def error_handler(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            res = f(*args, **kwargs)
            if type(res) is str:
                res = make_response(res)
                res.status_code = 401
            if 'Authorization' not in res.headers.keys():
                res.headers['Authorization'] = self.authenticate_header()
            return res
        self.auth_error_callback = wrapper
        return wrapper