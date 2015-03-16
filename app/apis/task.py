from flask import current_app, request, g
from bson import ObjectId
from . import api
from ..decorators import json
from ..helpers import helper_load_task_assgin_list
from ..exceptions import ValidationError
from ..auth import auth_token

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

    task = current_app.mongodb_conn.Task()
    task.title = data.get('title')
    task.description = data.get('description')
    task.start_time = data.get('starttime')
    task.end_time = data.get('endtime')

    helper_load_task_assgin_list(data, task)

    task.save()
    return {'res': "success"}


#TODO: update task api
@api.route('/task/<task_id>', methods=['PUT'])
@json
def update_task(task_id):

    #TODO: auth task manager

    data = request.get_json()

    task = current_app.mongodb_conn.Task.find_one_by_id(task_id)
    task.title = data.get('title')
    task.description = data.get('description')
    task.start_time = data.get('starttime')
    task.end_time = data.get('endtime')

    helper_load_task_assgin_list(data, task)

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