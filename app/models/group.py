from mongokit.document import Document
from bson.objectid import ObjectId


class Group(Document):
    use_dot_notation = True
    __collection__ = "users"
    structure = {
        'name': str,
        'owner': str,
        'owner_id': ObjectId,
        'user_list': list
    }
    required_fields = ['name', 'owner', 'owner_id']

    def add_user(self, user):
        if user not in self.user_list:
            self.user_list.append()
            self.save()
            return 'success'
        else:
            return 'already exists'

    def remove_user(self, user):
        if user not in self.user_list:
            self.user_list.remove(user)
            self.save()
            return 'success'
        else:
            return 'not exists'