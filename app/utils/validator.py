import re
from ..exceptions import ValidationError


def username_validator(username):
    if not re.match(r"^.{1,10}$", username):
        raise ValidationError
    return True


def email_validator(email):
    if not re.match(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", email):
        raise ValidationError
    return True


#TODO: task validator
def task_validator(task):

    return True

def subtask_validator(subtask):
    return True


#TODO: group validator
def group_validator(group):
    return True