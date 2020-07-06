# class Person(object):
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def shangshan(self):
#         print('%s,%s岁，%s上山去砍柴' % (self.name, self.age, self.sex))
#
#     def drive(self):
#         print('%s,%s岁,%s,开车去东北' % (self.name, self.age, self.sex))
#
#     def favor(self):
#         print('%s,%s岁,%s,最爱大保健' % (self.name, self.age, self.sex))
#
#
# a = Person('小明', '10', '男')
# a.shangshan()
# a.drive()
# a.favor()
# zhang = Person('老张', '90', '男')
# zhang.shangshan()
# zhang.drive()
# zhang.favor()


class Person:
    role = 'person'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.life_val = 100
        # self.attack_val = attack_val


class Police(Person):
    def __init__(self, name, age, sex, attack_val):
        Person.__init__(self, name, age, sex)
        self.attack_val = attack_val
        self.weapon = Weapon()

    def attack(self, terrorist_obj):
        terrorist_obj.life_val -= self.attack_val
        print("警察[%s]攻击了恐怖分子[%s],掉血[%s],还剩血量[%s]..." % (
        self.name, terrorist_obj.name, self.attack_val, terrorist_obj.life_val))


class Terrorist(Person):
    def __init__(self, name, age, sex, attack_val):
        Person.__init__(self, name, age, sex)
        self.attack_val = attack_val
        self.weapon = Weapon()

    def t_attack(self, police_obj):
        police_obj.life_val -= self.attack_val
        print("恐怖分子[%s]攻击了警察[%s],掉血[%s],还剩血量[%s]...")


class Weapon:
    def gun(self, obj):
        self.name = '打狗棒'
        self.attack_val = 40
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def print_log(self, obj):
        print("[%s]被[%s]攻击了，掉血[%s],还剩血量[%s]..." % (obj.name, self.name, self.attack_val, obj.life_val))

        # 警察不能使用，恐怖分子可以


p1 = Police('王华', 25, '男', 30)
t1 = Terrorist('毛开枪', '28', '男', 25)
p1.attack(t1)
t1.t_attack(p1)
p1.weapon.gun(t1)
