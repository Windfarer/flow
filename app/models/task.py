from mongokit.document import Document
from bson import ObjectId
from datetime import datetime
from ..utils.validator import subtask_validator, text_validator, datetime_validator, object_id_validator

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
    required_fields = ['title', 'user_id']
    default_values = {
        'finished': False,
        'doing': False,
        'start_time': datetime.utcnow,
        'end_time': datetime.utcnow,
        'deleted': False
    }
    validators = {
        'title': text_validator,
        # 'description': text_validator,
        # 'start_time': datetime_validator,
        # 'end_time': datetime_validator,
        # 'owner_id': object_id_validator
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
        return self.find({'user_id': ObjectId(user_id)})

    def find_by_id(self, task_id):
        return self.find({'_id': ObjectId(task_id)})

    def find_one_by_id(self, task_id):
        return self.find_one({'_id': ObjectId(task_id)})

    def remove(self, app_id):
        return self.remove({'app_id': app_id})
