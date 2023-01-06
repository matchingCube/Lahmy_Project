from application import db,Login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@Login_manager.user_loader
def load_user(user_id):
    return user.query.get(user_id)


class user(db.Model,UserMixin):

    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(64), unique=True, index = True)
    username = db.Column(db.String(64), unique = True, index = True)
    password_hash = db.Column(db.String(128))
    riskeProfile = db.Column(db.String(128))

    def __init__(self,Email,username,password,riskeProfile):
        self.email = Email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.riskeProfile = riskeProfile

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

# class preset(db.Model,UserMixin):
#
#     __tablename__='presets'
#
#     id = db.Column(db.Integer, forign_key=True, autoincrement=True)
#     email = db.Column(db.String(64), unique=True, index = True)
#     username = db.Column(db.String(64), unique = True, index = True)
#     password_hash = db.Column(db.String(128))
#
#     def __init__(self,Email,username,password):
#         self.email = Email
#         self.username = username
#         self.password_hash = generate_password_hash(password)
#
#     def check_password(self,password):
#         return check_password_hash(self.password_hash, password)
