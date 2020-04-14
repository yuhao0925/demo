class School(object):
    """总部，学校类"""
    def __init__(self,name,addr,website):
        self.name = name
        self.addr = addr
        self.website = website
        self.balance = 0
        print()

    def count_stu_num(self):
        pass
    def pay_salary(self):
        pass
    def staff_enrollment(self,staff_obj):
        pass
    def count_totla_revenue(self):
        pass

class BranchSchool(School):
    """分校"""
    pass

class Course(object):
    """分校"""
    def __init__(self,name,price,outline):
        self.name= name
        self.price = price
        self.outline= outline
        print()

class Class(object):
    """班级"""
    def __init__(self,course_obj,semester,school_obj):
        self.course_obj = course_obj
        self.semester = semester
        self.school_obj = school_obj
        print()

    def stu_transfer(self,sut_obj,sch_obj):
        """
        转学
        :param sut_obj:
        :param sch_obj:
        :return:
        """
        pass


class Staff(object):
    """员工"""
    def __init__(self,name,age,balance,salary,position):
        self.name=name
        self.age=age
        self.balance=balance
        self.salary = salary
        self.position = position

    def punch_obj(self):
        pass

class Teacher(Staff):
    def __init__(self,class_obj,day):
        self.class_obj = class_obj
        self.day = day

class Student():
    pass