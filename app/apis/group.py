from flask import request, g

from . import api
from flask import current_app, request
from ..models import Group
from ..decorators import json
from ..utils.validator import group_validator


#TODO: get groups api
@api.route('/groups', methods=['GET'])
@json
def get_groups():
    resp = current_app.mongodb_conn.Group.find_by_user_id(g.user['_id'])
    return {'results': resp}

#TODO: create groups api
@api.route('/groups', methods=['POST'])
@json
def create_group():
    data = request.get_json()
    group_validator(data)

    group = current_app.mongodb_conn.Group()
    group.name = data['name']
    group.owner_id = g.user['_id']
    group.user_list = [x for x in data['user_list']]
    return {'res': 'success'}

#TODO: get one group api
@api.route('/group/<group_id>', methods=['GET'])
@json
def get_one_group(group_id):
    group = current_app.mongodb_conn.Group.find_by_id(group_id)
    return group


#TODO: update a group api
@api.route('/group/<group_id>', methods=['PUT'])
@json
def update_group(group_id):
    data = request.get_json()
    group_validator(data)

    group = current_app.mongodb_conn.Group()
    group.name = data['name']
    group.owner_id = g.user['_id']
    group.user_list = [x for x in data['user_list']]
    return {'res': 'success update'}

#TODO: delete group api
@api.route('/group/<group_id>', methods=['DELETE'])
@json
def delete_group(group_id):
    group = current_app.mongodb_conn.Group.find_by_id(group_id)
    group.deleted = True
    return {'res': 'success delete'}