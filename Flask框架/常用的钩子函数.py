from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    print('===index====')
    return 'index 被调用'


# 第一次请求会执行
@app.before_first_request
def first_request():
    print('before_first_request.....')


# 每次请求前执行
@app.before_request
def before_request_demo():
    print('before_reqest........')


# 上下文处理器钩子context_processor使用
@app.route('/index')
def index1():
    return render_template('index.html')


@app.route('/list')
def list():
    return render_template('list.html')


# context_processor 钩子
@app.context_processor
def context_processor():
    return {'current_user': 'yuhao'}


# @app.errorhandler(500)
# def server_error(error):
#     return '你的服务器错误！！'


# 没有抛出异常，每次请求成功之后执行
@app.after_request
def after_request(error):
    print('after_request....')
    return error


if __name__ == '__main__':
    app.run(debug=True)
