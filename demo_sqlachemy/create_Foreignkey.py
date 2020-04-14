from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.engine import create_engine

# ORM精髓
from sqlalchemy.orm import relationship

engin = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/sql1?charset=utf8")
BaseMode = declarative_base()


# 一对多
class School(BaseMode):
    __tablename__ = "school"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)


class Student(BaseMode):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    school_id = Column(Integer, ForeignKey("school.id"))

    # 关系映射
    stu2sch = relationship("School", backref="stu2sch")


BaseMode.metadata.create_all(engin)
