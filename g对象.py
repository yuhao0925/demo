from flask import Flask,g,request

app = Flask(__name__)


def db_query():
    print(g.user_id,g.user_name)

@app.route('/')
def index():
    g.user_id = request.args['user_id']
    g.user_name = request.args['user_name']
    db_query()
    return '{}{}'.format(g.user_id,g.user_name)



if __name__ == '__main__':
    app.run(debug=True)