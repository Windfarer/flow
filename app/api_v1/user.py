from flask import current_app, request, g
from . import api
from ..decorators import json
from ..exceptions import ValidationError


@api.route("/users/<user_id>", methods=["GET"])
@json
def get_user(user_id):
    user = g.user

    return {
        "user_id": user._id,
        "nickname": user.nickname,
        "email": user.email,
        "avatar": "/images/default-avatar.png"
    }

@api.route("/users/<user_id>", methods=["PUT"])
@json
def update_user(user_id):
    data = request.get_json()
    user = g.user
    user = current_app.mongodb_conn.User.find_one({"_id": user._id})
    user.nickname = data.get("nickname")
    user.email = data.get("email")
    if user.verify_password(data.get("original_password")):
        user.set_password(data.get("new_password"))
    else:
        ValidationError("Password not Equal")
    user.save()
    return {
        'user_id': user._id,
        'nickname': user.nickname,
        'email': user.email
    }

@api.route("/users/<user_id>", methods=["DELETE"])
@json
def delete_user(user_id):
    data = request.get_json()
    user = g.user
    user = current_app.mongodb_conn.User.find_one({"_id": user._id})
    user.deleted = 1
    user.save()
    return {
        'user_id': user._id,
        'nickname': user.nickname,
        'email': user.email,
        'deleted': user.deleted
    }