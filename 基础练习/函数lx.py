name = "小猿圈"
def change():
    name = "小猿圈，自学编程"
    def change2():
        # global name  如果声明了这句，下面的name改的是最外层的全局变层
        name = "小猿圈，自学编程不要钱" #这句注释掉的话，下面name打印的是哪个值？
        print("第3层打印", name)
    change2()  # 调用内层函数
    print("第2层打印", name)
change()
print("最外层打印", name)


def aa(n):
    n = int(n/2)
    print(n)
    if n > 0:
        aa(n)


aa(100)