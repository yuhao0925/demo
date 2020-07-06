"""
序列化:
1.用于存储数据=>用于存档   一般使用pickle
2.传输给其他平台=>跨平台交互    json类型
"""

import json

# ret = json.dumps(True)
# print(ret, type(ret))
#
# print(json.loads(ret))


list = [1, 'aa', True, False]
json_ret = json.dumps(list)
print(json_ret, type(json_ret))  # [1, "aa", true, false] <class 'str'>

a = json.loads(json_ret)
print(a, type(a))  # [1, 'aa', True, False] <class 'list'>

import pickle

pick = pickle.dumps({1, 2, 3, 4, 5, 6})
print(pick, type(pick))  # b'\x80\x03cbuiltins\nset\nq\x00]q\x01(K\x01K\x02K\x03K\x04K\x05K\x06e\x85q\x02Rq\x03.' <class 'bytes'>

print(pickle.loads(pick))  # {1, 2, 3, 4, 5, 6}
