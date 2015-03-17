from flask import jsonify
from . import api
from ..exceptions import ValidationError


@api.app_errorhandler(ValidationError)
def bad_request(e):
    response = jsonify({'status': 400,
                        'error': 'bad request',
                        'message': e.args[0]})
    response.status_code = 400
    return response


@api.app_errorhandler(400)
def bad_request(e):
    response = jsonify({'status': 400,
                        'error': 'bad request',
                        'message': e.args[0]})
    response.status_code = 400
    return response


@api.app_errorhandler(404)
def not_found(e):
    response = jsonify({
        'status': 404,
        'error': 'not found',
        'message': 'invalid resource URI'
    })
    response.status_code = 404
    return response


@api.errorhandler(405)
def method_not_supported(e):
    response = jsonify({
        'status': 405,
        'error': 'method not supported',
        'message': 'the method is not supported'
    })
    response.status_code = 405
    return response


@api.app_errorhandler(500)
def internal_server_error(e):
    response = jsonify({
        'status': 500,
        'error': 'internal server error',
        'message': e.args[0]
    })
    response.status_code = 500
    return response