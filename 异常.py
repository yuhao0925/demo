from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    abort(404)
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)