from mongokit.document import Document
from datetime import datetime
from config import TaskStatus


class Task(Document):
    use_dot_notation = True
    __collection__ = "users"
    structure = {
        'title': str,
        'description': str,
        'start_time': datetime,
        'end_time': datetime,
        'finish_time': datetime,
        'assign_list': list,
        'status': TaskStatus,
        'deleted': bool
    }
    required_fields = ['title']
    default_values = {'status': TaskStatus.todo,
                      'start_time': datetime.utcnow,
                      'end_time': datetime.utcnow,
                      'deleted': False
                      }

    def create_task(self, current_user):
        if not self.assign_list:
            self.assign_list.append(current_user)
            return 'add yourself'

    def find_by_user(self, user):
        return

    def find_by_task_id(self, task_id):
        return self.find({'_id': task_id})

    def remove(self, app_id):
        return self.collection.remove({'app_id': app_id})
