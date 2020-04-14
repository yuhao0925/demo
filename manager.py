# 启动flask
from app01 import create_app,db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = create_app()
mig = Migrate(app,db)
manage = Manager(app)
manage.add_command("db",MigrateCommand)

@manage.command
def old(args):
    print(args)
    return args

@manage.option("-w","--who",dest="who")
@manage.option("-s","--sss",dest="ss")
def func(who,ss):
    print(f"{who},你好{ss}")


if __name__ == '__main__':
    manage.run()
