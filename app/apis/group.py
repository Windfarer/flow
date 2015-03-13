from flask import request

from . import api
from flask import current_app, request
from ..models import Group
from ..decorators import json
from ..auth import auth_token

#TODO: get groups api
@auth_token.login_required
@api.route('/groups', methods=['GET'])
@json
def get_groups():
    data = request.get_json()
    group = current_app.mongodb_conn.Group()
    group.name = data['name']
    return

#TODO: create groups api
@auth_token.login_required
@api.route('/groups', methods=['POST'])
@json
def create_group():
    data = request.get_json()
    group = current_app.mongodb_conn.Group()

    return

#TODO: get one group api
@auth_token.login_required
@api.route('/group/<group_alias>', methods=['GET'])
@json
def get_group(group_alias):
    data = request.get_json()
    return


#TODO: delete a group api
@auth_token.login_required
@api.route('/group/<group_alias>', methods=['PUT'])
@json
def delete_group(group_alias):
    data = request.get_json()
    return

#TODO: update group api
@auth_token.login_required
@api.route('/group/<group_alias>', methods=['DELETE'])
@json
def update_group(group_alias):
    data = request.get_json()
    return