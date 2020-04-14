import json
import os
import math
import random


# data = { 'no' : 1,
#     'name' : 'Runoob'}
#
# json_str = json.dumps(data)
# print("json对象:",json_str)
# json_data = json.loads(json_str)
# print("解码:",json_data)


# a = math.cos(math.pi/4)
# print(a)
#
#
# print(random.choice(['apple','b','c']))


# 集合是无序的数据类型
# a = {'aa','bb'}
# a = set(('aa','bb','cc'))
# a.add('cc')
# print(a)
# a.update({1,3})
# a.update([1,2,3])
# a.remove('bb')
# a.pop()
# print(a)

# c = ['a','b','c','d','e','f','g']
# gec
# print(c[:1:-2])


# def aa(n):
#     return n % 2 ==1
#
# templist = filter(aa,[1,2,3,4,5,6,7])
# listtemp = list(templist)
# print(listtemp)


# 斐波那契数据
# lst = [1,1]
# for i in range(10):
#     lst.append(lst[-1]+lst[-2])
# print(lst)

# 6666
# def num():
#     return [lambda x:i*x for i in range(4)]
# print([m(2) for m in num()])

# def func(a,b=[]):
#     b.append(a)
#     return b
# v1 = func(1)
# v2 = func(2,[10,20])
# v3 = func(3)
# print(v1,v2,v3)  # [1, 3] [10, 20, 2] [1, 3]


class Node():
    def __init__(self, item):
        self.item = item
        self.next = None


class Link():
    def __init__(self):
        self._head = None

    def append(self, item):
        node = Node(item)
        if self._head == None:
            self._head = node
            return
        cur = self._head
        pre = None
        while cur:
            pre = cur
            cur = cur.next
        pre.next = node

    def travel(self):
        cur = self._head
        while cur:
            print(cur.item)
            cur = cur.next

    def remove(self, item):
        cur = self._head
        pre = None
        if cur.item == item:
            self._head = cur.next
            return
        while cur:
            pre = cur
            cur = cur.next
            if item == cur.item:
                pre.next = cur.next
                return
link = Link()
link.append(1)
link.append(2)
link.append(3)
link.append(4)
link.append(5)
# link.remove(4)
link.travel()