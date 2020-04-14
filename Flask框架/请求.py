from flask import Flask, request, render_template, redirect, jsonify

app = Flask(__name__)


@app.route('/aa')
def query():
    # a = request.args.get('a')
    return 'aaa'


@app.route('/post_data', methods=['POST'])
def post_data():
    print(request.form)
    print(request.form['a'])
    return request.form.get('b')


@app.route('/json_data', methods=['POST'])
def json_data():
    print(request.json)
    return '222'


if __name__ == '__main__':
    # app.__call__
    app.run(debug=True)
