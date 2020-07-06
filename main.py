from threading import Thread
from werkzeug.local import Local
# 只要绑定loacl对象上的属性,每个线程中都是隔离的.

local = Local()
local.request = '123'


class Mytest(Thread):
    def run(self):
        # global request
        local.request = 'abc'
        print('子线程', local.request)


mytest = Mytest()
mytest.start()
mytest.join()
print('主线程', local.request)
