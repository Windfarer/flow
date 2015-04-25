from flask import Blueprint, request, current_app
import uuid

from ..decorators import json
from ..exceptions import ValidationError, NotFound

open_api = Blueprint("open_api", __name__)


@open_api.route("/register", methods=["POST"])
@json
def create_user():
    data = request.get_json()
    print(data)
    data["email"] = data["email"].lower()

    if current_app.mongodb_conn.User.find_one_by_email(data["email"]):
        raise ValidationError("user is exists")
    else:
        user = current_app.mongodb_conn.User()
        user.nickname = data.get("nickname")
        user.alias = str(uuid.uuid5(uuid.NAMESPACE_DNS, data.get("email")))
        user.email = data.get("email")
        user.set_password(data.get("password"))
        user.save()
    return {
        "email": user.email,
        "nickname": user.nickname,
        "password": "fakepassword"
    }


@open_api.route("/login", methods=["POST"])
@json
def login():
    data = request.get_json()
    data["email"] = data["email"].lower()
    user = current_app.mongodb_conn.User.find_one_by_email(data.get("email"))
    if user:
        user.verify_password(data.get("password"))
    else:
        raise NotFound("user not exists")
    return {
        "_id": user._id,
        "email": user.email,
        "alias": user.alias,
        "token": user.generate_auth_token(),
        "role": user.role
    }