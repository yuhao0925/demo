class Animal:
    a_type = "哺乳动物"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print("%s is eating..." % self.name)


class Person(Animal):

    def __init__(self, name, age, sex, hobble):
        # Animal.__init__(self,name,age,sex) # 方法1
        # super(Person,self).__init__(name,age,sex) # 方法2
        super().__init__(name, age, sex)
        self.hobble = hobble

    a_type = "高等动物"

    def talk(self):
        print("person %s is talking ...." % self.name)

    def eat(self):
        # Animal.eat(self)  # 保留父类的方法
        super().eat()
        print("人在优雅的吃。。。。")  # 重写父类的方法  先执行父类的方法


a = Person('于浩', 18, 'M', "男人")
a.eat()
a.talk()
# print(a.a_type)
print(a.name, a.sex, a.hobble)
