# from main import app
from flask import Blueprint


# @app.route('/good')
def good():
    return 'goods page'

# ===========

# 创建蓝图
# good = Blueprint('goods',__name__)


# @good.route('/get_goods')
# def good1():
#     return '===good===='
