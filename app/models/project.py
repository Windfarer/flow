from mongokit.document import Document
from bson.objectid import ObjectId
from ..utils.validator import text_validator, object_id_validator


class Project(Document):
    use_dot_notation = True
    __collection__ = "projects"
    structure = {
        "name": str,
        "owner_id": ObjectId,
        "managers": [ObjectId],
        "members": [ObjectId],
        "deleted": int
    }
    required_fields = ["name", "owner_id"]
    default_values = {
        "deleted": 0
    }
    validators = {
        "name": text_validator,
        # "manager_id": object_id_validator
    }

    def find_one_by_id(self, project_id):
        return self.find_one({"_id": ObjectId(project_id)})

    def find_by_user_id(self, user_id):
        return self.find({"members": ObjectId(user_id)})
