from flask import Flask, session, g, abort

app = Flask(__name__)
app.secret_key = 'fdsfsdf'

@app.errorhandler(401)
def error_handler(e):
    return '无法访问个人中心，请登录'

# 使用请求钩子，把用户信息保存在g变量中
@app.before_request
def get_user_info():
    """获取用户信息，其实就是获取认证信息"""
    g.name = session.get('name', None)

def login_required(func):
    def wrapper(*args, **kwargs):
        if g.name: # 已登录，允许执行视图函数
            return func(*args, **kwargs)
        else:
            # 400 语法/参数错误 401 未认证 403 已认证但权限不够
            # 404 资源不存在 405 请求方式不支持
            abort(401)
    return wrapper

@app.route('/user')
@login_required
def user(): # 需要已登录状态才能访问
    return '个人中心'

@app.route('/')
def index():
    if g.name: # 已经登录
        return '欢迎回来，%s' % g.name
    else: # 未登录
        return '首页'

@app.route('/login')
def login():
    # 模拟用户
    session['name'] = '' # 登录成功，记录认证信息
    return '用户登录'

if __name__ == '__main__':
    app.run(debug=True)