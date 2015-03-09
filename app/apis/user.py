from flask import request

from . import api
from ..models import User
from ..decorators import json


@api.route('/register', methods=['POST'])
@json
def user_register():
    data = request.json
    user = User()
    user.username = data.username
    user.email = data.email
    user.set_password(data.password)
    user.save()
    return


@api.route('/login', methods=['POST'])
@json
def user_login(data):

    return


@api.route('/logout', methods=['POST'])
@json
def user_logout(data):
    return