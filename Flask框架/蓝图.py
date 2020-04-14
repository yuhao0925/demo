from flask import Flask,Blueprint

app = Flask(__name__)

bp = Blueprint('bp',__name__)

@bp.route('/1')
def func():
    return 'lantu11'

app.register_blueprint(bp)

@app.route('/')
def func2():
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)