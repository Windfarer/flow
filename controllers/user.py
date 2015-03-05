from models.user import User


def create_user(data):
    user = User()
    user.username = data.username
    user.email = data.email
    user.set_password(data.password)
    user.save()
    return 'success'


def delete_user(user):
    return