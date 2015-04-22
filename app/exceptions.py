from datetime import datetime
from bson import ObjectId
import re

class ValidationError(ValueError):
    def __init__(self, msg):
        print(msg)

class Structure(object):
    structure = {}
    def __init__(self, data):
        for k, v in self.structure.items():
            try:
                if v is str:
                    assert re.match(v, data[k])
                elif v is datetime:
                    assert isinstance(datetime.fromtimestamp(data[k]), datetime)
                elif v is ObjectId:
                    assert ObjectId(data[k])
            except Exception:

                raise ValidationError('validation failed: '+k)
            # except Exception as e:
            #     if e.args:
            #         raise ValidationError('validate failed: '+e.args[0])
            #     else:
            #         raise  ValidationError('validate failed: '+k)




class TaskStructure(Structure):
    structure = {
        'title': r'^.{1,255}$',
        'description': r'^[\s\S]{1,200}$',
        'start_time': datetime,
        'end_time': datetime,
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
