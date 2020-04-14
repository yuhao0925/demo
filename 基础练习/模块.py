"""
os：和操作系统相关的操作被封装到该模块中
"""

# 和文件操作相关，
import os
# os.remove('a.txt')      删除文件
# os.rename('a.txt','b.txt')   #重命名

# 删除目录必须是空目录   removedirs




# 序列化：将内存中的数据转换成字符串，用以保存在文件或通过网络传输。
# 反：从文件中、网络中获取数据，转换成内置中原来的数据类型。


"""
josn；将数据类型转换成字符串，用于存储或者网络传输
 - dumps 将指定的类型转换成json形式的字符串。   元组序列化后就变成了列表。
 - loads 反
pickle:
 - 将python所有数据类型转换成bytes类型，序列化过程
 - 将bytes转换为python类型，反序列化过程 
 
collections 模块
 - 

"""

import json,pickle
# s = json.dumps([1,2,3])
# print(s)

# s = json.dumps([1,2,3])
# ret = json.loads(s)
# print(ret)
# print(type(ret))

# a = pickle.dumps((1,23,3))
# print(type(a))
# print(a)
#
# c = pickle.loads(a)
# print(type(c))
# print(c)


# a = pickle.dumps(set("123"))
# res = pickle.loads(a)
# print(res)
# print(type(res))

import hashlib

# 获取加密对象
# m = hashlib.md5()
# # 使用加密对象update，进行加密
# m.update(b"abc")
# # 通过hexdigest 获取加密结果
# ret = m.hexdigest()
# print(ret)

# m = hashlib.md5(b'abb').hexdigest()
# print(m)

