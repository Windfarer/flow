from flask import current_app, request, g
from bson import ObjectId
from datetime import datetime
from . import api
from ..decorators import json, validate_and_preprocess_payload

from ..exceptions import ValidationError


@api.route("/tasks", methods=["GET"])
@json
def get_tasks():

    user_id = g.user["_id"]

    project = request.args.get("project")
    status = int(request.args.get("status")) if request.args.get("status") else None
    # if not status:
    #     tasks = current_app.mongodb_conn.Task.find({"project": ObjectId(project),
    #                                                 "deleted": 0
    #                                                 })
    if project:
        tasks = current_app.mongodb_conn.Task.find({"project": ObjectId(project),
                                                    "deleted": 0
                                                    })
    else:
        tasks = current_app.mongodb_conn.Task.find({"project": None,
                                                    "user_id": ObjectId(user_id),
                                                    "deleted": 0
                                                    })
    resp = [make_response_task(x) for x in tasks]
    return resp


@api.route("/tasks", methods=["POST"])
@json
def create_task():
    data = request.get_json()
    user_id = g.user["_id"]
    project = request.args.get("project")

    task = current_app.mongodb_conn.Task()
    task.title = data.get("title")
    task.user_id = user_id
    if project:
        task.project = ObjectId(project)

    task.save()

    return make_response_task(task)


@api.route("/tasks/<task_id>", methods=["PUT"])
@json
def update_task(task_id):

    data = request.get_json()
    task = current_app.mongodb_conn.Task.find_one_by_id(task_id)
    task.title = data.get("title")
    task.description = data.get("description")
    task.status = data.get("status")
    if data.get("deadline"):
        # task.deadline = datetime.strptime(data.get("deadline"), "%Y-%m-%dT%H:%M:%S.%fZ")
        task.deadline = datetime.strptime(data.get("deadline"), "%Y-%m-%d")

    if data.get("assignees"):
        task.assignees = []
        for item in data.get("assignees"):
            task.assignees.append(ObjectId(item.get("id")))

    task.sub_tasks = data.get("sub_tasks")

    if task.status == 0 and task.deadline:
        task.status = 1

    task.save()
    return make_response_task(task)


@api.route("/tasks/<task_id>", methods=["DELETE"])
@json
def delete_task(task_id):
    task = current_app.mongodb_conn.Task.find_one_by_id(task_id)
    task.deleted = 1
    task.save()
    return {"deleted": task.deleted}


def make_response_task(data):
    assignees = []
    for item in data.get("assignees"):
        user = current_app.mongodb_conn.User.find_one({'_id': item})
        assignees.append({
            'id': user._id,
            'nickname': user.nickname,
            'email': user.email
        })
    return {
        "id": data.get("_id"),
        "title": data.get("title"),
        "description": data.get("description"),
        "status": data.get("status"),
        "deadline": data.get("deadline"),
        "start_time": data.get("start_time"),
        "finish_time": data.get("finish_time"),
        "assignees": assignees,
        "sub_tasks": data.get("sub_tasks"),
        "project": data.get("project"),
    }


def helper_load_task_assgin_list(data, task):
    task.menber_list = []
    for item in data.get("assignees"):
        user_id = ObjectId(item)
        if current_app.mongodb_conn.User.find_one({"_id": user_id}):
            task.assign_list.append(user_id)
        else:
            raise ValidationError("User not found")
    if g.user["_id"] not in task.assign_list:
        task.assign.list = g.user["_id"]
    return