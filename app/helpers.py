from flask import current_app, g
from bson import ObjectId
from .exceptions import ValidationError


def helper_load_group_member_list(data, group):
    group.member_list = []
    for item in data.get('member_list'):
        user_id = ObjectId(item)
        if current_app.mongodb_conn.User.find_one({'_id': user_id}):
            group.member_list.append(user_id)
        else:
            raise ValidationError('User not found')
    if g.user['_id'] not in group.member_list:
        group.member_list = g.user['_id']
    return


def helper_load_task_assgin_list(data, task):
    task.menber_list = []
    for item in data.get('assign_list'):
        user_id = ObjectId(item)
        if current_app.mongodb_conn.User.find_one({'_id': user_id}):
            task.assign_list.append(user_id)
        else:
            raise ValidationError('User not found')
    if g.user['_id'] not in task.assign_list:
        task.assign.list = g.user['_id']
    return