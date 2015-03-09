from app.models.task import Task


def create_task(user_alias, data):
    task = Task()
    task.title = data.title
    task.description = data.description
    task.start_time = data.starttime
    task.end_time = data.endtime
    task.assign_list = data.assign_list
    return


def get_tasks(user_alias):
    tasks = Task.find_by_user(user_alias)
    resp = filter(tasks, lambda x: x.deleted)
    return resp


def update_task(task_id, data):
    task = Task.find
    return 'updated'


def delete_task(task_id):
    return 'deleted'