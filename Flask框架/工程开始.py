from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def aa():
#     return 'hello'
#
#
# if __name__ == '__main__':
#     app.run()


# class Deafult(object):
#     KEY = 'dsadasdsadsada'
#
# app.config.from_object(Deafult)
#
# @app.route('/')
# def index():
#     print(app.config['KEY'])
#     return app.config['KEY']


# class DefaultConfig(object):
#     KEY = '这是配置1'
#
# class DefaultConmentfig(DefaultConfig):
#     KEY_2 = '这是配置2'
#
# app.config.from_object(DefaultConmentfig)
#
# @app.route('/')
# def index():
#     print(app.config['KEY'])
#     print(app.config['KEY_2'])
#     return app.config['KEY_2']


# app.config.from_pyfile('settings.py')
#
# @app.route('/1')
# def index():
#     print(app.config['KEY'])
#     return app.config['KEY']

# if __name__ == '__main__':
#     app.run(debug=True)


# 工厂模式
class DefaultConfig(object):
    KEY = 'aaaaaaaaaa'
class DevelopmentConfig(DefaultConfig):
    DEBUG = True

def flask_app(aa):
    app = Flask(__name__)
    app.config.from_object(aa)
    return app

app = flask_app(DevelopmentConfig)
@app.route('/')
def index():
    print(app.config['KEY'])
    return 'hello world'

if __name__ == '__main__':
    app.run()

