# 深浅拷贝
# import copy
# l1 = [1,2,3,[22,44]]
# l2 = copy.deepcopy(l1)
# l1[-1].append(66)
# print(l1)
# print(l2)

#
# def aa(a, b):
#     c = a if a > b else b
#     return c
# print(aa(100, 20))

#
# def aa(name, hige, size,age=18):
#     print("呵呵呵%s %s %s %s" % (name, age, hige, size))
#
# aa('于浩', hige=20, size=66)


# def func(args):
#     return args[::2]
# print(func([1,2,3,4,5]))

# def func(x):
#     if len(x) >5:
#         return True
#     else:
#         return False
# print(func([1,2,3,4,5,6,6]))

# def func(x):
#     return True if len(x) >5 else False
# print(func([1,2,3,4,5,6,6]))

# def aa(x):
#     if len(x) > 2:
#         return x[:2]
# print(aa([1,2,3,4,5]))


# def aa(a,bb,cc):
#     return len(a),len(bb),len(cc)
#
# print(aa(a='123',bb='于浩',cc= [1,1,3,2,3]))


# def aa(a,b):
# if a > b:
#     return a
# else:
#     return b
# return a if a >b else b
# print(aa(10,20))


# def aa(*args):
#     count = 0
#     for i in args:
#         count += i
#     return count
# print(aa(1,2,3,4))

# def aa(*args,**kwargs):
#     print(args)
#     print(kwargs)
# # aa(*[1,2,3,4],*[2,3,4,5])
# # aa(*'sadsad',*[2,3,4,5])
# aa(**{"name":"yuhao"},**{"Age":18})


# 迭代器
# s1 = 'asdasfas'
# print(dir(s1))

# l1 = [11,22,33,44,55]
# obj = iter(l1)
# # print(obj)
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))


# 生成器
# def func():
# #     print("111111")
# #     yield 3
# #     yield 4
# #     yield 5
# #
# # ret = func()
# # print(next(ret))
# # print(next(ret))
# # print(next(ret))


# 列表推导式(生成器表达式吧[]改成（）)
# l1 = [i ** 2 for i in range(1, 10)]
# print(l1)
#
# l2 = [i for i in range(1, 101) if i % 2 == 0]
# print(l2)
#
# li = [i for i in range(2, 101, 2)]
# print(li)
#
# l3 = ['tom', 'barry', 'a', 'bbb', 'yuhao']
# print([i.upper() for i in l3 if len(i) >= 3])

name = [['tom', 'bil', 'jyere', 'abce', 'gedg'], ['aaa', 'bbbb', 'ccc', 'aefgbd']]
# li = []
# for i in name:
#     for name in i:
#         if name.count("e") == 2:
#             li.append(name)
# print(li)

# print([name for i in name for name in i if name.count("e") ==2 ])


"""
内置函数 
eval剥去字符串的外衣运算里面的代码
lambda匿名函数 
callable 判断一个对象是否可否被调用 ***
round 保留浮点数的小数位数
reversed  将一个可迭代对象转换为迭代器
"""


# ret = lambda a,b: a + b
# print(ret(1,2))


# ret = lambda a:(a[0],a[2])
# print(ret('asdfg'))

# def aa(a, b):
#     if a > b:
#         return a
# ret = aa(5, 2)
# print(ret)
#
# ret = lambda a, b: a if a > b else b
# print(ret(5,2))

