from flask import Blueprint, jsonify
from app01.models import db, Users

user = Blueprint("user", __name__)


@user.route("/reg/<username>")
def reg(username):
    u = Users(name=username)
    db.session.add(u)
    db.session.commit()
    return "ok 200"


@user.route("/user_list")
def user_list():
    ret = Users.query.filter().all()[1]
    print(ret)
    return "ok"


@user.route("/aa")
def add():
    user2 = Users(name="浩浩", mobile="15174471511")
    user3 = Users(name=123, mobile="15174471522")
    db.session.add_all([user2, user3])
    db.session.commit()
    return "ok"


@user.route("/get_all")
def get_all():
    users = Users.query.all()
    ret_dict = {}
    for user in users:
        print(user.name,user.mobile)
        ret_dict[user.mobile]=user.name
    return jsonify(ret_dict)

@user.route("/first")
def first():
    user = Users.query.first()
    print(user)
    # return "OK"
    return jsonify({user.mobile:user.name})


@user.route("/filter_by")
def filter_by():
    ret = Users.query.filter_by(mobile="15174471558").first()
    return ret.name