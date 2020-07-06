import multiprocessing
from multiprocessing import Process
import time


# import random
# import os
#
#
# def task():
#     print('%s is piaoing' % os.getpid())
#     time.sleep(random.randrange(1, 3))
#     print('%s is piao end' % os.getpid())
#
#
# if __name__ == '__main__':
#     p = Process(target=task)
#     p.start()
#     p.join()  # 等待p停止,才执行下一行代码
#     print('主')


# from multiprocessing import Process
# import time
# import random
#
#
# def task(name):
#     print('%s is piaoing' % name)
#     time.sleep(random.randrange(1, 5))
#     print('%s is piao end' % name)
#
#
# if __name__ == '__main__':
#     p1 = Process(target=task, args=('egon',))
#     p1.start()
#     p1.terminate()  # 关闭进程,不会立即关闭,所以is_alive立刻查看的结果可能还是存活
#     print(p1.is_alive())  # 结果为True
#     print('主')
#     print(p1.is_alive())  # 结果为False


# from multiprocessing import Process
# import time
# import random
#
#
# def task(name):
#     print('%s is piaoing' % name)
#     time.sleep(random.randrange(1, 5))
#     print('%s is piao end' % name)
#
#
# if __name__ == '__main__':
#     p1 = Process(target=task, args=('egon',), name='子进程1')  # 可以用关键参数来指定进程名   name关键字给当前进程起个别名
#     p1.start()
#     print(p1.name, p1.pid,)


# from multiprocessing import Process
# import time
# import random
#
#
# def task(n):
#     time.sleep(random.randint(1, 3))
#     print('-------->%s' % n)
#
#
# if __name__ == '__main__':
#     p1 = Process(target=task, args=(1,))
#     p2 = Process(target=task, args=(2,))
#     p3 = Process(target=task, args=(3,))
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     p3.start()
#     p3.join()
#     print('-------->4')


# 带有参数的任务
# def task(count):
#     for i in range(count):
#         print("任务执行中..")
#         time.sleep(0.2)
#     else:
#         print("任务执行完成")
#
#
# def sing(singer):
#     for i in range(singer):
#         print("唱歌")
#         time.sleep(0.2)
#     else:
#         print("不唱了！！")
#
#
# if __name__ == '__main__':
#     # 创建子进程
#     # args: 以元组的方式给任务传入参数
#     sub_process = multiprocessing.Process(target=task, args=(5,))
#     sing_process = multiprocessing.Process(target=sing, kwargs={"singer": 3})
#     sub_process.start()
#     sing_process.start()


def task():
    for i in range(10):
        print("任务执行中...")
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子进程
    sub_process = multiprocessing.Process(target=task)
    # 设置守护主进程，主进程退出子进程直接销毁，子进程的生命周期依赖与主进程
    sub_process.daemon = True
    sub_process.start()

    time.sleep(0.5)
    print("over")
    # 让子进程销毁
    sub_process.terminate()
    exit()
