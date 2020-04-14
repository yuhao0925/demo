from flask_restful import Api, Resource
from flask import Flask


app = Flask(__name__)

rest_api = Api(app)

class Demo(Resource):
    def get(self):
        return 'get'

    def post(self):
        return 'post'

rest_api.add_resource(Demo, '/')  # 第一个参数视图类 第二个路由url

if __name__ == '__main__':
    app.run(debug=True)