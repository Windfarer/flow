from . import api
from ..models.group import Group
from ..decorators import json


@api.route('/groups', methods=['GET'])
@json
def get_groups(data):
    group = Group()
    return


@api.route('/groups', methods=['POST'])
@json
def create_group(data):
    group = Group()
    return


@api.route('/group/<group_alias>', methods=['PUT'])
@json
def delete_group():
    return


@api.route('/group/<group_alias>', methods=['DELETE'])
@json
def update_group():
    return