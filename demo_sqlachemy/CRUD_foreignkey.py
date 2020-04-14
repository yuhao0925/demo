from sqlalchemy.orm import sessionmaker
from demo_sqlachemy.create_Foreignkey import engin, Student, School

select_db = sessionmaker(engin)
db_session = select_db()

# 增加数据  stu qsl语句
# relationship 正向添加
# stu = Student(name="DragonFire", stu2sch=School(name="oldboy"))
# db_session.add(stu)
# db_session.commit()
# db_session.close()

# relationship 反向添加
# sch = School(name="Oldboyaaa")
# sch.stu2sch = [
#     Student(name="迪丽热巴"),
#     Student(name="于浩")
# ]
# db_session.add(sch)
# db_session.commit()
# db_session.close()


# 查询  relationship正向
# res = db_session.query(Student).all()
# for stu in res:
#     # print(stu.name, stu.school_id)
#     print(stu.name, stu.stu2sch.name)


 # 查询  relationship 反向
ret = db_session.query(School).all()
for stu in ret:
    # print(stu.name,len(stu.stu2sch))
    for sch in stu.stu2sch:
        print(stu.name,sch.name)