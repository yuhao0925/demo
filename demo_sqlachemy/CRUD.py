from demo_sqlachemy.create_sqlalchemy import User  # 选择表

# 选择数据库
from sqlalchemy.engine import create_engine

engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/sql1?charset=utf8")

from sqlalchemy.orm import sessionmaker

select_db = sessionmaker(engine)  # 选择数据库
db_session = select_db()  # 已经打开查询窗口
# 写人SQL
# user = User(name="yuhao.hao")
# user_list = [User(name="于浩"),User(name="浩浩")]
# 放入查询窗口
# db_session.add(user)
# db_session.add_all(user_list)
# 提交sql
# db_session.commit()
# 关闭sql
# db_session.close()


# 简单无条件/条件查询
# ret = db_session.query(User).all()
# ret = db_session.query(User).first()
# print(ret.id,ret.name)

# ret = db_session.query(User).filter(User.id==3).all()
# print(ret[0].id,ret[0].name)
# ret = db_session.query(User).filter_by(id=3).all()

# 修改数据 update
# ret = db_session.query(User).filter(User.id == 1).update({'name':'绝地求生'})
# db_session.commit()
# db_session.close()
# print(ret)

# 删除数据
ret = db_session.query(User).filter(User.id==2).delete()
db_session.commit()
db_session.close()