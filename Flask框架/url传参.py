from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world"


# http://127.0.0.1:5000/p/1/  <class 'str'> 默认类型
# string类型
@app.route("/p/<id>/")
def arcile_deailt(id):
    print(type(id))
    return "你访问的文章%s" % id


# http://127.0.0.1:5000/user/123  <class 'int'>
# int:接受整形
@app.route("/user/<int:user_id>/")
def user_id(user_id):
    print(type(user_id))
    return "user你好%s" % user_id


# http://127.0.0.1:5000/paths/flask/python/22/abc/   <class 'str'>
# path:和string类似,接受斜杠
@app.route("/paths/<path:test>/")
def path_demo(test):
    print(type(test))
    return "hello path {}".format(test)


# http://127.0.0.1:5000/bolg/123  <class 'str'>
# http://127.0.0.1:5000/users/1111  <class 'str'>
# any:可以指定多个路径
@app.route("/<any(bolg,users):url_path>/<id>")
def detail(url_path, id):
    if url_path == "bolg":
        print(type(url_path))
        return '博客详情%s' % id
    else:
        print(type(id))
        return '用户详情%s' % id


# http://127.0.0.1:5000/demo/1.52   <class 'float'>
# float:浮点型
@app.route("/demo/<float:number>")
def detail_float(number):
    print(type(number))
    return "您输入的小数伪%s" % number


@app.route('/d/')
def index():
    aa = request.args.get('aa')
    return '你的查询字符串方式为%s' % aa


@app.route("/login/", methods=['GET', 'POST'])
def login():
    return "login page"


@app.route("/profile/", methods=['GET', 'POST'])
def profile():
    name = request.args.get('name')
    if not name:
        return redirect(url_for('login'))
    else:
        return name


if __name__ == '__main__':
    app.run(debug=True)
