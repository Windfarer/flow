from app.controllers.task import *


task_api = [
    ('/<user_alias>/tasks', get_tasks, 'GET'),
    ('/<user_alias>/tasks', create_task, 'POST'),
    ('/<user_alias>/task/<task_id>', update_task, 'PUT'),
    ('/<user_alias>/task/<task_id>', delete_task, 'DELETE')
]