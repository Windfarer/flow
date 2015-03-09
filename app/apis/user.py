from app.controllers.user import *

user_api = [
    ('/register', user_register, 'POST'),
    ('/login', user_login, 'POST'),
    ('/logout', user_logout, 'POST')
]