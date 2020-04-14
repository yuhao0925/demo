import time

from flask import Flask, request, abort
import hashlib
import xmltodict

app = Flask(__name__)

WECHAT_TOKEN = 'yuhao'


@app.route("/watch8000", methods=["GET", "POST"])
def wechat():
    """对接微信服务器"""
    # 获取参数
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    echostr = request.args.get("echostr")
    # 进行参数计算
    # 1、进行排序
    list = [WECHAT_TOKEN, timestamp, nonce]
    list.sort()
    # 2、拼接成字符串
    tmp_str = "".join(list)
    # 3、进行sha1加密
    sgin = hashlib.sha1(tmp_str).hexdigest()
    if signature != sgin:
        # 表示不是微信发送过来的请求，报错 拒绝
        abort(403)
    else:
        # 如果与微信传过来的参数相匹配，则返回echostr
        if request.method == "GET":
            # 表示微信初始接入时发的GET请求
            return echostr
        else:
            # post请求方式，表示微信用户的消息转发过来
            # 接收消息
            req_xml = request.data
            req_dict = xmltodict.parse(req_xml)["xml"]
            # req_dict = req_xml["xml"]
            # 获取消息类型
            msq_type = req_dict.get("MsgType")
            if msq_type == "text":
                # 表示文本类型数据
                res_dict = {
                    "ToUserName": req_dict.get("FromUserName"),
                    "FromUserName": req_dict.get("ToUserName"),
                    'CreateTime': int(time.time()),
                    'MsgType': 'text',
                    'Content': req_dict.get("Content")}
            elif msq_type == "voice":
                # 语音类型
                res_dict = {
                    "ToUserName": req_dict.get("FromUserName"),
                    "FromUserName": req_dict.get("ToUserName"),
                    'CreateTime': int(time.time()),
                    'MsgType': 'text',
                    'Content': req_dict.get("Recognition")}

            elif msq_type == "event":
                if "subscribe" == req_dict.get("Event"):  # subscribe 代表用户关注
                    res_dict = {
                        "ToUserName": req_dict.get("FromUserName"),
                        "FromUserName": req_dict.get("ToUserName"),
                        'CreateTime': int(time.time()),
                        'MsgType': 'text',
                        'Content': "感谢关注!!!"}
                    if req_dict.get("EventKey") != None:
                        res_dict["Content"] += "场景值:"
                        res_dict["Content"] += req_dict.get("EventKey")[8:]
                elif req_dict.get("EVent") == "SCAN":
                    res_dict = {
                        "ToUserName": req_dict.get("FromUserName"),
                        "FromUserName": req_dict.get("ToUserName"),
                        'CreateTime': int(time.time()),
                        'MsgType': 'text',
                        'Content': "您扫描的场景值为：%s" % req_dict.get("EventKey")}
                else:
                    res_dict = None
            else:
                res_dict = {
                    "ToUserName": req_dict.get("FromUserName"),
                    "FromUserName": req_dict.get("ToUserName"),
                    'CreateTime': int(time.time()),
                    'MsgType': 'text',
                    'Content': "I love you"}
            req_dict = {"xml": req_dict}
            return xmltodict.unparse(req_dict)


if __name__ == '__main__':
    app.run(port=8000)
