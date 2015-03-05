from models.task import Task


def create_task(data):
    task = Task()
    task.title = data.title
    task.description = data.description
    task.start_time = data.starttime
    task.end_time = data.endtime
    task.assign_list = data.assign_list
    return


def get_tasks(user):
    tasks = Task.find_by_user(user)
    return tasks


def update_task(id, data):
    task = Task.find
    return 'updated'


def delete_task(id):
    return 'deleted'