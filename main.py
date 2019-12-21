from flask import Flask
from goods import good
from users import get_longin
from orders import order
from cart import app_cart

# 循环引用，解决方法，推迟一方的导入，让一方先完成

app = Flask(__name__)

app.route('/good')(good)
app.route('/login')(get_longin)

# 注册蓝图
# app.register_blueprint(order)
# app.register_blueprint(good,url_prefix='/goods')
app.register_blueprint(order, url_prefix="/orders")
app.register_blueprint(app_cart, url_prefix="/cart")


@app.route('/')
def index():
    return 'index page'


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
