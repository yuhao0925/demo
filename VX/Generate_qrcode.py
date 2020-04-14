import json
import time
import urllib
from urllib import request
from flask import Flask, request

WECHAT_APPID = "wx9d01fef2d8a4b870"
WECHAT_SECRET = "9f2be75572903f0b7565ca4ea0e997b1"


class AccessToken(object):
    """提供微信接口调用凭证"""
    # 类：1、数据  属性  2、函数  方法
    __access_token = {
        "token": "",  # 真实的token值
        "update_time": time.time(),  # 更新时间
        "expires_in": 7200  # token 有效期
    }

    @classmethod
    def get_access_token(cls):
        # 如果保存的access_token超过了有效期,重新从微信服务器获取，并保存，在返回
        if not cls.__access_token["token"] or (time.time() - cls.__access_token["update_time"]) > (
                cls.__access_token["expires_in"] - 600):
            # 调用微信接口，从新获取
            url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (
                WECHAT_APPID, WECHAT_SECRET)
            response = request.urlopen(url)
            resp_json = response.read()
            resp_dict = json.loads(resp_json)
            if "errcode" in resp_dict:
                # 微信处理失败
                raise Exception("get access token failed")
            else:
                cls.__access_token["token"] = resp_dict.get("access_token")
                cls.__access_token["expires_in"] = resp_dict.get("expires_in")
                cls.__access_token["update_time"] = time.time()
                return cls.__access_token["token"]
        else:
            # 如果没有过期，直接返回保存的access token
            return cls.__access_token["token"]


app = Flask(__name__)


@app.route("/get_grcode")
def get_grcode():
    scene_id = request.args.get("id")
    access_token = AccessToken.get_access_token()
    # 让微信生成临时二维码
    url = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s" % access_token
    req_data = {"expire_seconds": 604800,
                "action_name": "QR_SCENE",
                "action_info": {"scene": {"scene_id": scene_id}}
                }
    response = request.urlopen(url, data=json.dumps(req_data))
    resp_json = response.read()
    resp_dict = json.loads(resp_json)
    if "errcode" in resp_dict:
        return "generate grcode failed"
    else:
        ticket = req_data.get("ticket")
        # 指使微信生成成功
        return '<img src = "https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s">' % ticket


if __name__ == '__main__':
    app.run()
