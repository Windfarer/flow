from flask import Flask, g
from .decorators import json, rate_limit
from mongokit import Connection as MongoDBConn

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


    from .apis import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    @app.after_request
    def after_request(rv):
        headers = getattr(g, "headers", {})
        rv.headers.extend(headers)
        return rv

    #leave a auth entrance here
    #app.route('auth-token...')

    return app