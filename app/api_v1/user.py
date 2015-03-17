from flask import current_app, request, g
from . import api
from ..decorators import json
from ..utils.validator import email_validator, username_validator


@api.route('/users')
def get_users():
    pass


@api.route('/test', methods=['GET'])
@json
def test():
    print(g.user)
    return {'res': 'res234234'}