from flask import current_app, request

from . import api
from ..decorators import json
from ..auth import auth_token

#TODO: get tasks api
@auth_token.login_required
@api.route('/<user_alias>/tasks', methods=['GET'])
@json
def get_tasks(user_alias):
    tasks = current_app.mongodb_conn.Task.find_by_user(user_alias)
    resp = filter(tasks, lambda x: x.deleted)
    return resp

#TODO: create task api
@auth_token.login_required
@api.route('/<user_alias>/tasks', methods=['POST'])
@json
def create_task(user_alias):
    data = request.get_json()
    task = current_app.mongodb_conn.Task()
    task.title = data.title
    task.description = data.description
    task.start_time = data.starttime
    task.end_time = data.endtime
    task.assign_list = data.assign_list
    task.save()
    return

#TODO: update task api
@auth_token.login_required
@api.route('/<user_alias>/task/<task_id>', methods=['PUT'])
@json
def update_task(user_alias, task_id):
    data = request.get_json()
    task = current_app.mongodb_conn.Task.find_one()
    task.title = data.title
    task.description = data.description
    task.start_time = data.starttime
    task.end_time = data.endtime
    task.assign_list = data.assign_list
    task.save()
    return {'res': 'updated'}

#TODO: delete task api
@auth_token.login_required
@api.route('/<user_alias>/task/<task_id>', methods=['DELETE'])
@json
def delete_task(user_alias, task_id):
    task = current_app.mongodb_conn.Task.find_one()
    task.deleted = True
    task.save()
    return {'res': 'deleted'}