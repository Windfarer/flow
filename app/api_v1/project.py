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
    project_validator(data)

    project = current_app.mongodb_conn.Project()
    project.name = data["name"]
    project.manager_id = g.user["_id"]

    helper_load_project_member_list(data, project)

    project.save()
    return make_response_project(project)


@api.route("/projects/<project_id>", methods=["GET"])
@json
def get_one_project(project_id):
    project = current_app.mongodb_conn.Project.find_by_id(project_id)
    return make_response_project(project)


@api.route("/projects/<project_id>", methods=["PUT"])
@json
def update_project(project_id):

    data = request.get_json()
    project_validator(data)

    project = current_app.mongodb_conn.Project()
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
    return {
        "id": data.get("_id"),
        "name": data.get("name"),
        "owner_id": data.get("owner_id"),
        "managers": data.get("managers"),
        "menbers": data.get("members"),
        "deleted": data.get("deleted"),
    }


def helper_load_project_member_list(data, project):
    project.member_list = []
    for user_id in data.get("member_list"):

        if current_app.mongodb_conn.User.find_one({"_id": ObjectId(user_id)}):
            project.member_list.append(user_id)
        else:
            raise ValidationError("User not found")
    if g.user["_id"] not in project.member_list:
        project.member_list = g.user["_id"]
    return


