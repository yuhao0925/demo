from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 创建db时候一定要主要导入蓝图的顺序
from app01.views import user


def create_app():
    app = Flask(__name__)

    # app.config["DEBUG"] = True
    app.config["SESSION_COOKIE_NAME"] = "I am Not Session"
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123@127.0.0.1:3306/sql1?charset=utf8"
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3306/sql1'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(user.user)

    db.init_app(app=app)
    return app
