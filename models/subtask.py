from mongokit.document import Document
from bson.objectid import ObjectId
from config import TaskStatus


class SubTask(Document):
    structure = {
        'title': str,
        'parent_task': ObjectId,
        'status': TaskStatus
    }
    required_fields = ['title', 'parent_task']
    default_values = {'status': TaskStatus.todo}
