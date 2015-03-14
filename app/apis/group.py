from flask import request, g

from . import api
from flask import current_app, request
from ..models import Group
from ..decorators import json


#TODO: get groups api
@api.route('/groups', methods=['GET'])
@json
def get_groups():
    data = request.get_json()
    group = current_app.mongodb_conn.Group()
    group.name = data['name']
    return

#TODO: create groups api
@api.route('/groups', methods=['POST'])
@json
def create_group():
    data = request.get_json()
    group = current_app.mongodb_conn.Group()
    group.name = data['name']
    group.owner_name = g.user.username
    group.owner_id = g.user._id
    return

#TODO: get one group api
@api.route('/group/<group_alias>', methods=['GET'])
@json
def get_group(group_alias):
    data = request.get_json()
    return


#TODO: delete a group api
@api.route('/group/<group_alias>', methods=['PUT'])
@json
def delete_group(group_alias):
    data = request.get_json()
    return

#TODO: update group api
@api.route('/group/<group_alias>', methods=['DELETE'])
@json
def update_group(group_alias):
    data = request.get_json()
    return