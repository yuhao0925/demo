# 在init方法之前执行new方法


class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('init heheh')

    def __new__(cls, *args, **kwargs):
        print(cls,args,kwargs)

        object.__new__(cls)
        return object.__new__(cls)

a = Student("yuhao",20)
a.name
