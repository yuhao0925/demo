from flask import Flask

app = Flask(__name__)


@app.before_first_request
def head_before_first_request():
    print('before_first_request被调用')


@app.before_request
def before_request():
    print('before_request被调用')


@app.after_request
def after_request(response):
    print('after_request调用')
    return response

@app.teardown_request
def handle_teardown_request(e):
    print('handle_teardown_request调用')



@app.route('/')
def index():
    print('===index====')
    return 'index 被调用'


if __name__ == '__main__':
    app.run(debug=True)