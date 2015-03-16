import re
from bson import ObjectId
from datetime import datetime
from ..exceptions import ValidationError


def username_validator(username):
    if not re.match(r"^.{1,10}$", username):
        raise ValidationError('Invalid username')
    return True


def email_validator(email):
    if not re.match(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", email):
        raise ValidationError('Invalid Email address')
    return True


def text_validator(text):
    if not isinstance(text, str) or not text:
        raise ValidationError
    return True


def object_id_validator(object_id):
    if not isinstance(object_id, ObjectId):
        raise ValidationError('Invalid ObjectId')
    return True

def datetime_validator(d):
    if not isinstance(d, datetime):
        raise ValidationError('Invalid datetime')


def subtask_validator(subtask):
    return True


#TODO: group validator
def group_validator(group):
    return True