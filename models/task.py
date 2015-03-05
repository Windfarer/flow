from mongokit.document import Document
from datetime import datetime
from config import TaskStatus


class Task(Document):
    structure = {
        'title': str,
        'description': str,
        'start_time': datetime,
        'end_time': datetime,
        'finish_time': datetime,
        'assign_list': list,
        'status': TaskStatus
    }
    required_fields = ['title']
    default_values = {'status': TaskStatus.todo,
                      'start_time': datetime.utcnow,
                      'end_time': datetime.utcnow,
                      }

    def create_task(self, current_user):
        if not self.assign_list:
            self.assign_list.append(current_user)
            return 'add yourself'

    def find_by_user(self, user):
        self.find()
        return