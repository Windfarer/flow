from datetime import datetime
from bson import ObjectId
import re

class ValidationError(ValueError):
    pass

class Structure(object):
    structure = {}
    def __init__(self, data):
        current = None
        try:
            for k, v in self.structure.items():
                current = k
                if isinstance(v, str):
                    assert re.match(v, data[k])
                elif isinstance(v, datetime):
                    assert isinstance(datetime.fromtimestamp(data[k]), datetime)
                elif isinstance(v, ObjectId):
                    assert ObjectId(data[k])
        except Exception as e:
            raise ValidationError('validate failed: '+current)


class TaskStructure(Structure):
    structure = {
        'title': r'^.{1,255}$',
        'description': r'^[\s\S]{1,200}$',
        'start_time': datetime,
        'end_time': datetime,
        'owner_id': ObjectId
    }
    def __init__(self, data):
        super().__init__(data)



class GroupStructure(Structure):
    structure = {
        'name': str,
        'manager_id': ObjectId,
    }
    def __init__(self, data):
        super().__init__(data)
