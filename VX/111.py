from urllib import request

url = "http://www.baidu.com"
reqponse = request.urlopen(url)
print(reqponse.read().decode())