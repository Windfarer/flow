from flask import Flask, g
from .decorators import json, rate_limit
from mongokit import Connection as MongoDBConn
from .exceptions import ValidationError


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    mongodb_database = MongoDBConn(host=app.config.get("MONGODB_HOST"),
                                   port=app.config.get("MONGODB_PORT"))

    mongodb_conn = mongodb_database[app.config.get("MONGODB_DATABASE")]

    from .models import User, Task, Group

    mongodb_database.register([User, Task, Group])

    app.mongodb_database = mongodb_database
    app.mongodb_conn = mongodb_conn

    from .api_v1 import api as api_blueprint
    from .open_api import open_api as open_api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api/v1")
    app.register_blueprint(open_api_blueprint, url_prefix="/open_api")


    @app.after_request
    def after_request(rv):
        headers = getattr(g, "headers", {})
        rv.headers.extend(headers)
        return rv

    return app