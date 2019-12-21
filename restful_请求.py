import re
from flask import Flask, Blueprint
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser

# 自定义的参数，自定义参数的异常会被help覆盖掉
def mobile(mobile_str):
    if re.match(r'^1[3-9]\d{9}$', mobile_str):
        return mobile_str
    else:
        raise ValueError('{} is not a valid mobile'.format(mobile_str))


class UserProfile(Resource):

    def get(self):
        rp = RequestParser()
        # 1、参数名   type参数类型检验  loaction指明参数出现的位置，也可以指明多个
        rp = rp.add_argument('name',
                             # type=str,
                             type=mobile,
                             location='args',
                             help='套你猴子')

        args = rp.parse_args()
        # print(args['name'])
        name = args
        return {'msg': '{}'.format(name)}


app = Flask(__name__)
blue_bp = Blueprint('user', __name__)
user_api = Api(blue_bp)
user_api.add_resource(UserProfile, '/demo/aaa', endpoint='hahaha')
app.register_blueprint(blue_bp)

if __name__ == '__main__':
    app.run(debug=True)
