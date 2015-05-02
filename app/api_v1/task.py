from flask import current_app, request, g
from bson import ObjectId
from . import api
from ..decorators import json, validate_and_preprocess_payload

from ..exceptions import ValidationError


@api.route("/tasks", methods=["GET"])
@json
def get_tasks():

    user_id = g.user["_id"]
    print(user_id)
    tasks = current_app.mongodb_conn.Task.find_by_user_id(user_id)
    resp = [make_response_task(x) for x in tasks if not x.deleted]
    return resp


@api.route("/tasks", methods=["POST"])
@json
def create_task():
    user_id = g.user["_id"]

    data = request.get_json()
    print(data)
    task = current_app.mongodb_conn.Task()

    task.title = data.get("title")
    task.user_id = user_id
    task.save()

    return make_response_task(task)


@api.route("/tasks/<task_id>", methods=["PUT"])
@json
def update_task(task_id):

    data = request.get_json()
    print(data)
    task = current_app.mongodb_conn.Task.find_one_by_id(task_id)
    task.title = data.get("title")
    task.description = data.get("description")
    task.status = data.get("status")
    task.deadline = data.get("deadline")
    task.start_time = data.get("start_time")
    task.finish_time = data.get("finish_time")
    task.project = data.get("project")
    task.assignees = data.get("assignees")
    task.sub_tasks = data.get("sub_tasks")

    task.save()
    return make_response_task(task)


@api.route("/tasks/<task_id>", methods=["DELETE"])
@json
def delete_task(task_id):
    task = current_app.mongodb_conn.Task.find_one_by_id(task_id)
    task.deleted = 1
    task.save()
    return {"_id": task._id}


def make_response_task(data):
    return {
        "id": data.get("_id"),
        "title": data.get("title"),
        "description": data.get("description"),
        "status": data.get("status"),
        "deadline": data.get("deadline"),
        "start_time": data.get("start_time"),
        "finish_time": data.get("finish_time"),
        "assignees": data.get("assignees"),
        "sub_tasks": data.get("sub_tasks"),
        "project": data.get("project"),
    }


def helper_load_task_assgin_list(data, task):
    task.menber_list = []
    for item in data.get("assign_list"):
        user_id = ObjectId(item)
        if current_app.mongodb_conn.User.find_one({"_id": user_id}):
            task.assign_list.append(user_id)
        else:
            raise ValidationError("User not found")
    if g.user["_id"] not in task.assign_list:
        task.assign.list = g.user["_id"]
    return