from functools import wraps
from flask import request


def validate_and_preprocess_payload(payload_structrue):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            payload = request.get_json()
            payload['test'] = 'success'

            #TODO: validate
            #TODO: prerpocess

            for k, v in payload.items():
                request.json[k] = v

            return f(*args, **kwargs)
        return wrapper
    return decorator