from mongokit.document import Document
from bson.objectid import ObjectId
from ..utils.validator import text_validator, object_id_validator

class Group(Document):
    use_dot_notation = True
    __collection__ = 'groups'
    structure = {
        'name': str,
        'owner_id': ObjectId,
        'user_list': list,
        'deleted': bool
    }
    required_fields = ['name', 'owner_id']
    default_values = {
        'deleted': False
    }
    validators = {
        'name': text_validator,
        'owner_id': object_id_validator
    }

    def find_one_by_id(self, group_id):
        return self.find_one({'_id': ObjectId(group_id)})

