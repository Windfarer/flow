from flask import send_from_directory, current_app, request
from werkzeug.exceptions import NotFound
from bson import ObjectId
from . import api
from ..decorators import json

from ..exceptions import ValidationError


@api.route("tasks/<task_id>/files/", methods=["GET"])
@json
def get_file_list(task_id):
    files = current_app.mongodb_conn.FileRecord.find({"task_id": ObjectId(task_id)})
    file_list = []
    for file_record in files:
        item = {
            "filename": "{}.{}".format(file_record.file_name, file_record.file_ext),
            "file_id": file_record._id
        }
        file_list.append(item)
    return file_list


@api.route("/tasks/<task_id>/files", methods=["POST"])
@json
def add_file(task_id):
    file_record = current_app.mongodb_conn.FileRecord()
    file_record.file_name = "test"
    file_record.file_ext = "txt"
    file_record.save()

    file = request.files
    file.save()
    return file_record


@api.route("tasks/<task_id>/files/<file_id>", methods=["DELETE"])
@json
def remove_file(task_id, file_id):
    file_record = current_app.mongodb_conn.FileRecord.find_one({"_id": ObjectId(file_id)})
    if not file_record:
        raise NotFound
    file_record.deleted = 1
    file_record.save()
    return file_record


def send_file(file_id):
    file_record = current_app.mongodb_conn.FileRecord.find_one({"_id": ObjectId(file_id)})
    if not file_record or file_record.deleted == 1:
        raise NotFound
    filename = "{}.{}".format(file_record.file_name, file_record.file_ext)
    return send_from_directory(current_app.config.get("UPLOAD_FOLDER"),
                               file_id,
                               as_attachment=True,
                               attachment_filename=filename)


