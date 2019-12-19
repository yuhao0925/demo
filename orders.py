from flask import Blueprint

order = Blueprint('orders',__name__)

@order.route('/get_order')
def get_order():
    return 'get order page'

@order.route('/post_order')
def post_order():
    return 'post order page'

