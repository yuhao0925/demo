import threading


# __new__方法
class Singlenton(object):
    isinstance = None
    lock = threading.RLock()

    def __init__(self, name):
        # 初始化对象
        self.name = name

    def __new__(cls, *args, **kwargs):  # new 返回空对象
        """创建对象"""
        if cls.isinstance:
            return cls.isinstance
        with cls.lock:
            if not cls.isinstance:
                cls.isinstance = object.__new__(cls)
            return object.__new__(cls)


# obj1 = Singlenton('yuhao')
# obj2 = Singlenton('yuhao')
# print(obj1,obj2)
def func():
    obj = Singlenton('xx')
    print(obj)


for i in range(10):
    t = threading.Thread(target=func)
    t.start()
