from mongokit.document import Document
from bson.objectid import ObjectId
from ..utils.validator import text_validator, object_id_validator


class Project(Document):
    use_dot_notation = True
    __collection__ = "groups"
    structure = {
        "name": str,
        "manager_id": ObjectId,
        "menber_list": list,
        "deleted": int
    }
    required_fields = ["name", "manager_id"]
    default_values = {
        "deleted": 0
    }
    validators = {
        "name": text_validator,
        "manager_id": object_id_validator
    }

    def find_one_by_id(self, group_id):
        return self.find_one({"_id": ObjectId(group_id)})

