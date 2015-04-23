from flask import current_app, request, g
from . import api
from ..decorators import json, validate_and_preprocess_payload
from ..helpers import helper_load_task_assgin_list
from ..utils.validator import task_validator

@api.route('/tasks', methods=['GET'])
@json
def get_tasks():

    user_id = g.user['_id']
    print(user_id)
    tasks = current_app.mongodb_conn.Task.find_by_user_id(user_id)
    resp = [x for x in tasks if x.deleted is False]
    return resp


@api.route('/tasks', methods=['POST'])
@json
def create_task():
    user_id = g.user['_id']

    data = request.get_json()
    print(data)
    task = current_app.mongodb_conn.Task()

    task.title = data['title']
    task.user_id = user_id
    # task.description = data['description']
    # task.start_time = data['starttime']
    # task.end_time = data['endtime']
    #
    # helper_load_task_assgin_list(data, task)

    task.save()
    return task


@api.route('/tasks/<task_id>', methods=['PUT'])
@json
def update_task(task_id):

    data = request.get_json()
    print(data)
    task = current_app.mongodb_conn.Task.find_one_by_id(task_id)
    task.title = data.get('title')
    task.done = data.get('done')
    # task.description = data.get('description')
    # task.start_time = data.get('starttime')
    # task.end_time = data.get('endtime')

    # helper_load_task_assgin_list(data, task)

    task.save()
    return task


@api.route('/tasks/<task_id>', methods=['DELETE'])
@json
def delete_task(task_id):
    task = current_app.mongodb_conn.Task.find_one_by_id(task_id)
    task.deleted = True
    task.save()
    return {'res': 'deleted'}