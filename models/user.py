from mongokit import Document
from werkzeug.security import generate_password_hash, check_password_hash

class User(Document):
    structure = {
        'username': str,
        'email': str,
        'password_hash': str,
        'groups': list
    }
    required_fields = ['username', 'email', 'password_hash']

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)