from flask import Flask, render_template, jsonify, redirect, make_response

app = Flask(__name__)


# 返回模板
@app.route('/moban')
def index():
    my_dict = {
        "a": 100
        # ......
    }
    my_list = [1, 2, 3, 4, 5, 6]
    my_int = 0
    context = {
        "name": "python",
        "age": 20,
        "my_dict": my_dict,
        "my_list": my_list,
        "my_int": my_int,
        'bread': "yuhao"
    }
    # return render_template('1.html',name = 'python',age = 18...)
    return render_template('1.html', **context)


# 重定向
@app.route('/aa')
def aa():
    return redirect('http://www.baidu.com')


# JSON
@app.route('/bb')
def bb():
    aa = {
        "id": 10,
        "name": '老王',
        'names': 'yuhao'
    }
    return jsonify(aa)


# 自定义状态码、请求头
@app.route('/demo')
def demo():
    return '状态码 666', 666, {'yuhao': 'python'}


@app.route('/demo2')
def demo2():
    aa = make_response('make_response测试')
    aa.headers['yuhao'] = 'python'
    aa.status = '404'
    return aa




if __name__ == '__main__':
    app.run(debug=True)
