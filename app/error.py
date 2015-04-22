from flask import jsonify
from .api_v1 import api
from .exceptions import ValidationError
from .decorators import json

@api.app_errorhandler(ValidationError)
@json
def bad_request(e):
    response = {
        'status': 400,
        'error': 'bad request',
        'message': e.args[0]
    }
    return response, 400


@api.app_errorhandler(400)
@json
def bad_request(e):
    response = {
        'status': 400,
        'error': 'bad request',
        'message': "invalid request"
    }
    return response, 400


@api.app_errorhandler(404)
@json
def not_found(e):
    response = {
        'status': 404,
        'error': 'not found',
        'message': 'invalid resource URI'
    }
    return response, 404


@api.app_errorhandler(405)
@json
def method_not_supported(e):
    response = {
        'status': 405,
        'error': 'method not supported',
        'message': 'the method is not supported'
    }
    return response, 405


@api.app_errorhandler(500)
@json
def internal_server_error(e):
    response = {
        'status': 500,
        'error': 'internal server error',
        'message': e.args[0]
    }
    return response, 500