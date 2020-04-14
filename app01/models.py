from app01 import db


class Users(db.Model):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),nullable=False)  #nullable=False 不允许为空
    mobile = db.Column(db.String(64),nullable=False,unique=True)

if __name__ == '__main__':
    from app01 import create_app
    app = create_app()
    db.create_all(app=app)