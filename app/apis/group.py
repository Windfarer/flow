from flask import request, g
from bson import ObjectId
from . import api
from flask import current_app, request
from ..models import Group
from ..decorators import json
from ..utils.validator import group_validator
from ..auth import auth_token
from ..exceptions import ValidationError
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

    group.manager_id = g.user['_id']

    group.member_list = []
    for item in data.get('member_list'):
        user_id = ObjectId(item)
        if current_app.mongodb_conn.User.find_one({'_id': user_id}):
            group.member_list.append(user_id)
        else:
            raise ValidationError('User not found')
    group.save()
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
    group.member_list = []
    for item in data.get('member_list'):
        user_id = ObjectId(item)
        if current_app.mongodb_conn.User.find_one({'_id': user_id}):
            group.member_list.append(user_id)
        else:
            raise ValidationError('User not found')
    group.save()
    return {'res': 'success update'}

#TODO: delete group api
@api.route('/group/<group_id>', methods=['DELETE'])
@json
def delete_group(group_id):
    group = current_app.mongodb_conn.Group.find_by_id(group_id)
    group.deleted = True
    group.save()
    return {'res': 'success delete'}