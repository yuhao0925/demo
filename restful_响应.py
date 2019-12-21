from json import dumps
from six import PY3
from flask import Flask, current_app, make_response
from flask_restful import Api, fields, Resource, marshal_with, marshal


# from flask_restful.representations import json


class Uesr(object):
    def __init__(self, user_id, name, age):
        self.user_id = user_id
        self.name = name
        self.age = age


#  定义返回的数据
resoure_fields = {
    'user_id': fields.Integer,
    'name': fields.String
}


# class DemoResource(Resource):
#     # 方法1：envelope 参数规定了返回数据的外层包裹字段
#     @marshal_with(resoure_fields, envelope='data1')
#     def get(self):
#         return Uesr(1, 'yuhao', 22)


class DemoResource(Resource):
    # 方法1：envelope 参数规定了返回数据的外层包裹字段
    @marshal_with(resoure_fields, envelope='data1')
    def get(self):
        return Uesr(1, 'yuhao', 22)


'''
{
    "data1": {
        "user_id": 1,
        "name": "yuhao"
    }
}
'''


class Demo2Resourse(Resource):
    # 方法2
    def get(self):
        user = Uesr(2, 'haohao', 11)
        return marshal(user, resoure_fields)


class Demo3Resourse(Resource):
    def get(self):
        my_file = {
            'uesr_id': fields.Integer,
            'info': {
                'name': fields.String,
                'age': fields.Integer}
        }
        user = Uesr(2, 'HHHH', 33)
        return marshal(user, my_file)


app = Flask(__name__)

api = Api(app)
api.add_resource(DemoResource, '/1')
api.add_resource(Demo2Resourse, '/2')
api.add_resource(Demo3Resourse, '/3')


# json模式
@api.representations('application/json')
def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""

    # 自定义返回数据的格式
    if 'message' not in data:
        data = {
            'message': 'OK',
            'data': data
        }

    settings = current_app.config.get('RESTFUL_JSON', {})
    if current_app.debug:
        settings.setdefault('indent', 4)
        settings.setdefault('sort_keys', not PY3)

    dumped = dumps(data, **settings) + "\n"

    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp


if __name__ == '__main__':
    app.run(debug=True)
