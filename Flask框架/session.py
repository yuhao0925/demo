from flask import Flask, session
import os
import datetime

app = Flask(__name__)

# 方式2
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(hours=2)


# 方式1
# 使用session需要设置secret_key
# class Myconfig(object):
#     SECRET_KEY = 'nb2m13bmn14bmn214b21mn'
# app.config.from_object(Myconfig)
# app.config['SECRET_KEY'] = "nb2m13bmn14bmn214b21mn"

# 设置
@app.route('/set_session')
def set_session():
    session['username'] = 'yuhao'
    session['age'] = 18
    # permanent持久化  存储31天
    session.permanent = True
    return '==set_session=='


# eyJ1c2VybmFtZSI6Inl1aGFvIn0.XexdGg.SUv9lxUaR-hWHl8kLwGgHf9fO30
# 获取
@app.route('/get_session')
def get_session():
    username = session.get('username')
    return 'get_session {}'.format(username)


# 删除
@app.route('/delete_session')
def delete_session():
    session.pop('username', None)
    session.clear()
    return 'delete session'


@app.route('/check_session')
def check_session():
    # pop 取出原有的就不存在了
    return session.pop('username', 'aaaabbbccc')


if __name__ == '__main__':
    app.run(debug=True)
