import functools
from flask import jsonify


import functools
from flask import jsonify


def json(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        rv = f(*args, **kwargs)

        status = None
        headers = None
        if isinstance(rv, tuple):
            rv, status, headers = rv + (None,) * (3 - len(rv))
        if isinstance(status, (dict, list)):
            headers, status = status, None

        if not isinstance(rv, dict):
            rv = rv.export_data()

        rv = jsonify(rv)
        if status is not None:
            rv.status_code = status
        if headers is not None:
            rv.headers.extend(headers)
        rv.headers.extend(make_cors_headers())
        return rv
    return wrapped


def make_cors_headers():
    cors_headers = {
        "Access-Control-Allow-Headers": "Origin, Accept, Content-Type, Authorization",
        "Access-Control-Allow-Methods": "OPTIONS",
        "Access-Control-Allow-Origin": "*"
    }
    return cors_headers