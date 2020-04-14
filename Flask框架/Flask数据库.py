from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 连接mysql 数据库                       用户名:密码@主机ip:端口/数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/bd_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 在flask中是否追踪数据库修改
app.config['SQLALCHEMY_ECHO'] = True  # 显示生成的SQL语句

# 创建SQLAlchemy的数据库连接对象
db = SQLAlchemy(app)


# step 3. 建立映射模型  类->表  类属性->字段  对象->记录
# 此时数据库里一个表都没有
class User(db.Model):
    __tablename__ = 't_user'  # 设置表名
    id = db.Column(db.Integer, primary_key=True)  # 主键  默认主键自增
    name = db.Column(db.String(20), unique=True)  # 设置唯一
    age = db.Column(db.Integer, doc='年龄int')  # doc字段说明，和数据表没有关联性
    gender = db.Column(db.SmallInteger, default=0, doc='性别，默认0')


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
