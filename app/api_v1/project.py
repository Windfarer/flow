from flask import current_app, request, g

from . import api

from ..decorators import json
from ..utils.validator import project_validator

from ..helpers import helper_load_project_member_list


@api.route("/projects", methods=["GET"])
@json
def get_projects():
    resp = current_app.mongodb_conn.Project.find_by_user_id(g.user["_id"])
    return {"results": resp}


@api.route("/projects", methods=["POST"])
@json
def create_project():
    data = request.get_json()
    project_validator(data)

    project = current_app.mongodb_conn.Group()
    project.name = data["name"]

    project.manager_id = g.user["_id"]

    helper_load_project_member_list(data, project)

    project.save()
    return {"res": "success"}


@api.route("/projects/<project_id>", methods=["GET"])
@json
def get_one_project(project_id):
    project = current_app.mongodb_conn.Project.find_by_id(project_id)
    return project


@api.route("/projects/<project_id>", methods=["PUT"])
@json
def update_project(project_id):

    data = request.get_json()
    project_validator(data)

    project = current_app.mongodb_conn.Group()
    project.name = data["name"]
    project.owner_id = g.user["_id"]

    helper_load_project_member_list(data, project)

    project.save()
    return {"res": "success update"}


@api.route("/projects/<project_id>", methods=["DELETE"])
@json
def delete_project(project_id):
    project = current_app.mongodb_conn.Project.find_by_id(project_id)
    project.deleted = True
    project.save()
    return {"res": "success delete"}