from flask import Blueprint

# 创建了一个蓝图
app_cart = Blueprint("carts",__name__,template_folder="templates")

from .views import get_cart

