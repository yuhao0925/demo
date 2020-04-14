from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine

BaseModel = declarative_base()

from sqlalchemy import Column, Integer, String


class User(BaseModel):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False, index=True)


engin = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/sql1?charset=utf8")  # 数据库连接驱动语句

BaseModel.metadata.create_all(engin)
