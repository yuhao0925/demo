from sqlalchemy.orm import sessionmaker
from demo_sqlachemy.createM2M import engine,Girl,Boy

select_db = sessionmaker(engine)
db_session = select_db()

# 增加数据   正向添加
# g = Girl(name="赵丽颖",gyb=[Boy(name="Drang"),Boy(name="冯绍峰")])
# db_session.add(g)
# db_session.commit()
# db_session.close()

# 反向添加
# b = Boy(name="浩浩")
# b.byg=[
#     Girl(name="热巴"),
#     Girl(name="杨幂"),
#     Girl(name="乔碧罗")
# ]
# db_session.add(b)
# db_session.commit()
# db_session.close()

# 查询  正向
# ret = db_session.query(Girl).all()
# for g in ret:
#     print(g.name,len(g.gyb))

# 反向
# ret = db_session.query(Boy).all()
# for b in ret:
#     print(b.name,len(b.byg))