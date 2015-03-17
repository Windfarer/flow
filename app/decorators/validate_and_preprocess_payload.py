from functools import wraps
from flask import request


def validate_and_preprocess_payload(payload_structrue):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            payload = request.get_json()
            #validate
            #prerpocess
            request.json['title']='lalalla'
            return f(*args, **kwargs)
        return wrapper
    return decorator