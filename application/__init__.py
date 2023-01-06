import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

Login_manager = LoginManager()
appy = Flask(__name__,template_folder='templates')
appy.config['SECRET_KEY'] = 'secretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
appy.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir,"data.sqliteTest")
appy.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(appy)
Migrate(appy,db)

Login_manager.init_app(appy)
Login_manager.login_view = "login"
