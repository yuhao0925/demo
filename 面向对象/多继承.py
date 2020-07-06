class Master(object):
    def __init__(self):
        self.kongfu = "古法煎饼果子配方"  # 实例变量，属性

    def make_cake(self):  # 实例方法，方法
        print("[古法] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)

    def dayandai(self):
        print("师傅的大烟袋..")


class School(object):
    def __init__(self):
        self.kongfu = "现代煎饼果子配方"

    def make_cake(self):
        print("[现代] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)

    def xiaoyandai(self):
        print("学校的小烟袋..")


class Prentice(Master, School):  # 多继承，继承了多个父类（Master在前）
    def paly(self):
        print("我喜欢自己玩")


damao = Prentice()
print(damao.kongfu)  # 执行Master的属性
damao.make_cake()  # 执行Master的实例方法

# 子类的魔法属性__mro__决定了属性和方法的查找顺序
print(Prentice.__mro__)

damao.dayandai()  # 不重名不受影响
damao.xiaoyandai()
damao.paly()
