from flask import current_app
from bson import ObjectId
from mongokit import Document
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from ..utils.validator import username_validator, email_validator


class User(Document):
    use_dot_notation = True
    __collection__ = 'users'
    structure = {
        'username': str,
        'email': str,
        'password_hash': str,
        'groups': list,
        'deleted': bool
    }
    required_fields = ['username', 'email', 'password_hash']
    default_values = {
        'deleted': False
    }
    indexes = [
        {
            'fields': 'email',
            'unique': True
        },
    ]
    validators = {
        'username': username_validator,
        'email': email_validator
    }

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({'id': str(self._id)}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return current_app.mongodb_conn.User.find_one({'_id': ObjectId(data['id'])})

    def find_one_by_email(self, email):
        return self.find_one({'email':email})