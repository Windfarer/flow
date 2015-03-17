from flask import current_app, request, g
from . import api
from ..decorators import json, validate_and_preprocess_payload
from ..helpers import helper_load_task_assgin_list
from ..utils.validator import task_validator

@api.route('/tasks', methods=['GET'])
@json
def get_tasks():

    user_id = g.user['_id']
    tasks = current_app.mongodb_conn.Task.find_by_user_id(user_id)
    resp = [x for x in tasks if x.deleted is False]
    return {'results': resp}


@api.route('/tasks', methods=['POST'])
@validate_and_preprocess_payload('task')
@json
def create_task():
    data = request.get_json()
    print(data)
    task = current_app.mongodb_conn.Task()

    task.title = data['title']
    task.description = data['description']
    task.start_time = data['starttime']
    task.end_time = data['endtime']

    helper_load_task_assgin_list(data, task)

    task.save()
    return {'res': "success"}


@api.route('/task/<task_id>', methods=['PUT'])
@validate_and_preprocess_payload('task')
@json
def update_task(task_id):

    data = request.get_json()

    task = current_app.mongodb_conn.Task.find_one_by_id(task_id)
    task.title = data.get('title')
    task.description = data.get('description')
    task.start_time = data.get('starttime')
    task.end_time = data.get('endtime')

    helper_load_task_assgin_list(data, task)

    task.save()
    return {'res': 'updated'}


@api.route('/task/<task_id>', methods=['DELETE'])
@json
def delete_task(task_id):
    task = current_app.mongodb_conn.Task.find_one_by_id(task_id)
    task.deleted = True
    task.save()
    return {'res': 'deleted'}