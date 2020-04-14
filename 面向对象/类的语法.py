class Dog:
    d_type = "二哈"  # 类属性，类变量  公共属性   所有实例共享
    sss = "sss"  # 类属性，类变量

    def __init__(self, name, age):  # 初始化方法，实例化时会自动执行，进行一些初始化工作
        print("呵呵", name, age)
        self.name = name   # 实例属性，每个实例独享
        self.age = age

    def sayhi(self):
        print("hello", self.d_type,self.name,self.age)


# d = Dog("yyy", 20)  # 生成了一个实例
# d.sayhi()
# print(d.d_type, d.sss)
# print(Dog.d_type)
# print(d.d_type)
# print(d.name)
# d.name = '于浩'
# print(d.name)