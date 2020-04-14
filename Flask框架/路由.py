from flask import Flask, request, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world 1'

@app.route('/')
def index1():
    return 'hello world 2'

@app.route('/yu',methods=['POST'])
def yu():
    return 'hello world 1'
@app.route('/yu1',methods=['GET','POST'])
def yu1():
    if request.method == 'GET':
        return 'hehehe'
    if request.method == 'POST':
        return 'xixixixi'

@app.route('/hello')
@app.route('/hi')
def index3():
    return '---index-----'

@app.route('/python',methods=['GET','POST'])
def index4():
    return '----post-----'

@app.route('/redict')
def redrect():
    return '<a href="%s">red_iect</a>' %url_for('index4')

# http://127.0.0.1:5000/users/11
@app.route("/users/<int:user_id>")
def index6(user_id):
    print(type(user_id))
    return "hello user{}".format(user_id)

# http://127.0.0.1:5000/user/a/b/c
@app.route("/user/<path:user_id>")
def index7(user_id):
    print(type(user_id))
    return "hello user{}".format(user_id)


class MobileConverter(BaseConverter):
    '''自定义'''
    regex = r'\d{5}'

    def to_python(self, value):
        '''经过to_python的调用，将调用的结果返回,在传给视图函数'''
        print("to_python调用 value=%s" %value)
        # return value
        return '666'

app.url_map.converters['mobile'] = MobileConverter

@app.route('/mobile/<mobile:mob_num>')
def index8(mob_num):
    return 'mobile is {}'.format(mob_num)




if __name__ == '__main__':
    # print(app.url_map)
    app.run(debug=True)