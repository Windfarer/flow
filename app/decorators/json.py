import functools
from flask import make_response
from json import JSONEncoder, dumps
from bson import ObjectId
from datetime import date, datetime


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, ObjectId):
            return str(obj)
        else:
            return JSONEncoder.default(self, obj)


def json(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        rv = f(*args, **kwargs)

        status = None
        headers = []
        if isinstance(rv, tuple):
            rv, status, headers = rv + (None,) * (3 - len(rv))
        if isinstance(status, (dict, list)):
            headers, status = status, None

        # if not isinstance(rv, dict):
        #     rv = rv.export_data()
        status_code = 200

        if status:
            status_code = status
        rv = make_response(dumps(rv, cls=CustomJSONEncoder), status_code, {"Content-Type": "application/json"})

        if headers is not None:
            rv.headers.extend(headers)
        rv.headers.extend(make_cors_headers())

        return rv
    return wrapped


def make_cors_headers():
    cors_headers = {
        "Access-Control-Allow-Headers": "Origin, Accept, Content-Type, Authorization",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS, HEAD",
        "Access-Control-Allow-Origin": "*"
    }
    return cors_headers