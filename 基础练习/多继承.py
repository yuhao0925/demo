class shenxian:
    def fly(self):
        print("我会飞")

    # 如果出现了重名方法,会执行第一个父类的方法,如果继承的父类又继承了爷爷类并且重名了,会执行最高者的方法
    def fight(self):
        print("神仙在打架...")


class Monkey:
    def dump(self):
        print("我会跳")

    def fight(self):
        print("猴子在打架...")


class people(shenxian, Monkey):
    def play(self):
        print("我会玩")


a = people()
# a.fly()
# a.dump()
# a.play()
a.fight()


class People(object):
    couny = "china"

    @classmethod
    def get_couny(cls):
        return cls.couny


class aa(People):
    couny = 'usa'

    @classmethod
    def get_cony(cls):
        return cls.couny


a = aa()
print(a.get_cony())  # 可以用过实例对象访问
print(aa.get_cony())  # 可以通过类访问




# ==============================

class People(object):
    eat = 'aa'

    @staticmethod
    def get_aa(self):
        return People.eat

class bbb(People):
    eat = 'banana'

    @staticmethod
    def get_Bb(self):
        return bbb.eat

b = bbb()
print(b.eat)
# print(bbb.get_Bb())
print(People.get_aa('brink'))
