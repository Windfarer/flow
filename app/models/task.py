from mongokit.document import Document
from bson import ObjectId
from datetime import datetime
from ..utils.validator import subtask_validator

class Task(Document):
    use_dot_notation = True
    __collection__ = 'tasks'
    structure = {
        'title': str,
        'description': str,
        'start_time': datetime,
        'end_time': datetime,
        'finish_time': datetime,
        'user_id': ObjectId,
        'assign_list': list,
        'groups': list,
        'finished': bool,
        'doing': bool,
        'sub_tasks': list,
        'deleted': bool
    }
    required_fields = ['title']
    default_values = {
        'finished': False,
        'doing': False,
        'start_time': datetime.utcnow,
        'end_time': datetime.utcnow,
        'deleted': False
    }

    def one_subtask(self, data):
        subtask_validator(data)
        subtask = {
            'title': data['title'],
            'finished': False,
            'deleted': False
        }
        pass

    def remove_subtask(self):
        pass

    def find_by_user_id(self, user_id):
        return self.find({'_id': ObjectId(user_id)})

    def find_by_task_id(self, task_id):
        return self.find({'_id': task_id})


    def remove(self, app_id):
        return self.collection.remove({'app_id': app_id})
