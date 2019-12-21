from . import app_cart
from flask import render_template


@app_cart.route("get_cart")
def get_cart():
    return 'get_cart'


@app_cart.route("render_cart")
def render_cart():
    return render_template('cart.html')
