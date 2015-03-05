from mongokit.document import Document
from bson.objectid import ObjectId

class Group(Document):
    structure = {
        'name': str,
        'owner': str,
        'owner_id': ObjectId
    }
    required_fields = ['name', 'owner', 'owner_id']