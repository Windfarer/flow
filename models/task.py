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
    required_fields = ['title', 'assign_list']
    default_values = {'status': TaskStatus.todo,
                      'start_time': datetime.utcnow,
                      'end_time': datetime.utcnow,
                      }
