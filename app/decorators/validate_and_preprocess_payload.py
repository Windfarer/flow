from functools import wraps
from flask import request
from ..exceptions import TaskStructure, GroupStructure


def validate_and_preprocess_payload(payload_structrue):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            validator = {
            'task': lambda x: TaskStructure(x),
            'group': lambda x: GroupStructure(x)
            }
            payload = request.get_json()

            validator[payload_structrue](payload)

            for k, v in payload.items():
                request.json[k] = v

            return f(*args, **kwargs)
        return wrapper
    return decorator