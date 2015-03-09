from mongokit.document import Document
from bson.objectid import ObjectId


class Group(Document):
    use_dot_notation = True
    __collection__ = "groups"
    structure = {
        'name': str,
        'owner': str,
        'owner_id': ObjectId,
        'user_list': list
    }
    required_fields = ['name', 'owner', 'owner_id']
