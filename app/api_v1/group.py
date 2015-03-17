from flask import current_app, request, g

from . import api

from ..decorators import json, validate_and_preprocess_payload
from ..utils.validator import group_validator

from ..helpers import helper_load_group_member_list


@api.route('/groups', methods=['GET'])
@json
def get_groups():
    resp = current_app.mongodb_conn.Group.find_by_user_id(g.user['_id'])
    return {'results': resp}


@api.route('/groups', methods=['POST'])
@validate_and_preprocess_payload('group')
@json
def create_group():
    data = request.get_json()
    group_validator(data)

    group = current_app.mongodb_conn.Group()
    group.name = data['name']

    group.manager_id = g.user['_id']

    helper_load_group_member_list(data, group)

    group.save()
    return {'res': 'success'}


@api.route('/group/<group_id>', methods=['GET'])
@json
def get_one_group(group_id):
    group = current_app.mongodb_conn.Group.find_by_id(group_id)
    return group


@api.route('/group/<group_id>', methods=['PUT'])
@validate_and_preprocess_payload('group')
@json
def update_group(group_id):

    data = request.get_json()
    group_validator(data)

    group = current_app.mongodb_conn.Group()
    group.name = data['name']
    group.owner_id = g.user['_id']

    helper_load_group_member_list(data, group)

    group.save()
    return {'res': 'success update'}


@api.route('/group/<group_id>', methods=['DELETE'])
@json
def delete_group(group_id):
    group = current_app.mongodb_conn.Group.find_by_id(group_id)
    group.deleted = True
    group.save()
    return {'res': 'success delete'}