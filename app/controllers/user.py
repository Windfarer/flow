from app.models.user import User


def user_register(data):
    user = User()
    user.username = data.username
    user.email = data.email
    user.set_password(data.password)
    user.save()
    return 'success'


def user_login(data):

    return


def user_logout(data):

    return