from bson import ObjectId
from mongokit import Document
import uuid


class FileRecord(Document):
    use_dot_notation = True
    __collection__ = "files"
    structure = {
        "file_name": str,
        "file_ext": str,
        "task_id": ObjectId,
        # "file_uuid": str,
        "deleted": int
    }
    required_fields = ["filename"]
    default_values = {
        # "file_uuid": uuid.uuid4(),
        "deleted": 0
    }