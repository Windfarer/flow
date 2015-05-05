from flask import current_app, request, g
from bson import ObjectId

from . import api
from ..exceptions import ValidationError
from ..decorators import json
from ..utils.validator import project_validator


@api.route("/projects", methods=["GET"])
@json
def get_projects():
    projects = current_app.mongodb_conn.Project.find_by_user_id(g.user["_id"])
    resp = [make_response_project(project) for project in projects]
    return resp


@api.route("/projects", methods=["POST"])
@json
def create_project():
    data = request.get_json()
    # project_validator(data)

    project = current_app.mongodb_conn.Project()
    project.name = data["name"]
    project.owner_id = g.user["_id"]
    project.manager_id = g.user["_id"]

    helper_load_project_member_list(data, project)
    print(project)
    project.save()
    return make_response_project(project)


@api.route("/projects/<project_id>", methods=["GET"])
@json
def get_one_project(project_id):
    project = current_app.mongodb_conn.Project.find_one_by_id(project_id)
    return make_response_project(project)


@api.route("/projects/<project_id>", methods=["PUT"])
@json
def update_project(project_id):

    data = request.get_json()
    project_validator(data)

    project = current_app.mongodb_conn.Project.find_one({'_id': ObjectId(project_id)})
    project.name = data.get("name")

    helper_load_project_member_list(data, project)

    project.save()
    return make_response_project(project)


@api.route("/projects/<project_id>", methods=["DELETE"])
@json
def delete_project(project_id):
    project = current_app.mongodb_conn.Project.find_by_id(project_id)
    project.deleted = 1
    project.save()
    return {"_id": project._id}


def make_response_project(data):
    members = []
    for member in data.get("members"):
        user = current_app.mongodb_conn.User.find_one({'_id': member})
        members.append({
            'id': user._id,
            'nickname': user.nickname,
            'email': user.email
        })
    return {
        "id": data.get("_id"),
        "name": data.get("name"),
        "owner_id": data.get("owner_id"),
        "managers": data.get("managers"),
        "members": members,
        "deleted": data.get("deleted"),
    }


def helper_load_project_member_list(data, project):
    project.members = []
    if data.get("members"):
        for user in data.get("members"):
            user = current_app.mongodb_conn.User.find_one_by_email(user.get("email"))
            if user:
                project.members.append(user._id)
            else:
                raise ValidationError("User not found")
    if g.user["_id"] not in project.members:
        project.members.append(g.user["_id"])
    return


