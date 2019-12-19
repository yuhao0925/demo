from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    aa = make_response('===set_cookie===')
    # k  V  过期时间
    aa.set_cookie('username','python',max_age=3600)
    return aa

@app.route('/get_cookie')
def get_cookie():
    resp = request.cookies.get('username')
    return resp

@app.route('/delete_cookie')
def delete_cookie():
    response = make_response('===delete_cooke===')
    response.delete_cookie('username')
    return response



if __name__ == '__main__':
    app.run(debug=True)