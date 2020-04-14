class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


a = Person("yuhao", 23)
print(type(a))
print(type(Person))


def __init__(self, name, age):
    self.name = name
    self.age = age


dog_class = type("Dog", (object,), {"role": 22, "__init__": __init__})  # 动态生成一个类
print(dog_class)

# d  = dog_class
# a = d.role
# print(a)
print(dog_class)
c = dog_class("mjj", 22)
print(c.role, c.name, c.age)

