from flask import request

from . import api
from flask import request
from ..models import Group
from ..decorators import json


@api.route('/groups', methods=['GET'])
@json
def get_groups():
    data = request.json
    group = Group()
    return


@api.route('/groups', methods=['POST'])
@json
def create_group():
    data = request.json
    group = Group()
    return


@api.route('/group/<group_alias>', methods=['GET'])
@json
def get_group():
    data = request.json
    return


@api.route('/group/<group_alias>', methods=['PUT'])
@json
def delete_group():
    data = request.json
    return


@api.route('/group/<group_alias>', methods=['DELETE'])
@json
def update_group():
    data = request.json
    return