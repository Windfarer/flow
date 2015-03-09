from . import api
from ..models.task import Task
from ..decorators import json


@api.route('/<user_alias>/tasks', methods=['GET'])
@json
def get_tasks(user_alias):
    tasks = Task.find_by_user(user_alias)
    resp = filter(tasks, lambda x: x.deleted)
    return resp


@api.route('/<user_alias>/tasks', methods=['POST'])
@json
def create_task(user_alias, data):
    task = Task()
    task.title = data.title
    task.description = data.description
    task.start_time = data.starttime
    task.end_time = data.endtime
    task.assign_list = data.assign_list
    return


@api.route('/<user_alias>/task/<task_id>', methods=['PUT'])
@json
def update_task(user_alias, task_id, data):
    task = Task.find
    return 'updated'


@api.route('/<user_alias>/task/<task_id>', methods=['DELETE'])
@json
def delete_task(user_alias, task_id):
    return 'deleted'