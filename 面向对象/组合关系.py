class Dog:  # 狗类
    def __init__(self, name, age, beed, attack_val):
        self.name = name
        self.age = age
        self.beed = beed  # 品种
        self.attack_val = attack_val  # 每条狗的攻击力
        self.left_val = 100  # 每条狗的血量

    def bite(self, people):
        people.val_sex -= self.attack_val
        print("人%s打了狗%s,狗掉血%s,还剩%s..." % (self.name, people.name, self.attack_val, people.life_val))


class People:
    def __init__(self, name, sex, attack_val):
        self.name = name
        self.sex = sex
        self.attack_val = attack_val
        self.life_val = 100

    def attack(self, dog):
        dog.life_val -= self.attack_val
        print("人%s打了狗%s,狗掉血%s,还剩%s..." % (self.name, dog.name,self.attack_val,dog.life_val))


class Weapon:
    def dog_stick(self, obj):
        """打狗棒"""
        self.name = "打狗棒"
        self.attack_avl = 40
        obj.life_val -= self.attack_avl
        self.print_log(obj)

    def AK(self, obj):
        """打狗棒"""
        self.name = "AK47"
        self.attack_avl = 60
        obj.life_val -= self.attack_avl
        self.print_log(obj)

    def print_log(self, obj):
        print("%s 被 %s 攻击力，掉线%s,还剩血%s..." % (obj.name, self.name, self.attack_avl, obj.life_val))
