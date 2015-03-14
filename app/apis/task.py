from flask import current_app, request, g

from . import api
from ..decorators import json
from ..utils.validator import task_validator

#TODO: get tasks api
@api.route('/tasks', methods=['GET'])
@json
def get_tasks():
    user_id = g.user['_id']
    tasks = current_app.mongodb_conn.Task.find_by_user_id(user_id)
    resp = [x for x in tasks if x.deleted is False]
    return {'results': resp}


#TODO: create task api
@api.route('/tasks', methods=['POST'])
@json
def create_task():
    data = request.get_json()
    task_validator(data)

    task = current_app.mongodb_conn.Task()
    task.title = data.get['title']
    task.description = data.get['description']
    task.start_time = data.get['starttime']
    task.end_time = data.get['endtime']
    task.assign_list = data.get['assign_list']
    #TODO: assign_list?
    task.save()
    return {'res': "success"}

# #TODO: create subtask?
# @api.route('/task/<task_id>/subtasks', methods=['POST'])
# @json
# def create_subtask(task_id):
#     task = current_app.mongodb_conn.Task.find_one_by_id(task_id)
#     pass
#
# #TODO: remove subtask?
# @api.route('/task/<task_id>/subtask/<subtask_id>', methods=['POST'])
# @json
# def remove_subtask(task_id,subtask_id):
#     pass
#
# #TODO: update subtask?
# @api.route('/task/<task_id>/subtask/<subtask_id>', methods=['POST'])
# @json
# def update_subtask(task_id, subtask_id):
#     pass


#TODO: update task api
@api.route('/task/<task_id>', methods=['PUT'])
@json
def update_task(task_id):
    data = request.get_json()
    task_validator(data)

    task = current_app.mongodb_conn.Task.find_one_by_id(task_id)
    task.title = data['title']
    task.description = data['description']
    task.start_time = data['starttime']
    task.end_time = data['endtime']
    task.assign_list = data['assign_list']
    task.save()
    return {'res': 'updated'}


#TODO: delete task api
@api.route('/task/<task_id>', methods=['DELETE'])
@json
def delete_task(task_id):
    task = current_app.mongodb_conn.Task.find_one_by_id(task_id)
    task.deleted = True
    task.save()
    return {'res': 'deleted'}