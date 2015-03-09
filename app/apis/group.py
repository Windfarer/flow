from app.controllers.group import *


group_api = [
    ('/groups', get_groups, 'GET'),
    ('/groups', create_group, 'POST'),
    ('/group/<task_id>', update_group, 'PUT'),
    ('/group/<task_id>', delete_group, 'DELETE')
]