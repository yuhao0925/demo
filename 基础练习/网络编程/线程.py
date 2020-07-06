import threading
from multiprocessing import Queue

# def user(q):
#     while True:
#         inp_str = input(">>>>").strip()
#         q.put(inp_str)
#         if inp_str == "exit":
#             break
#
#
# def str_up(q):
#     while True:
#         msg = q.get().upper()
#         if msg == 'EXIT':
#             break
#
#
# if __name__ == '__main__':
#     q = Queue()
#     t1 = threading.Thread(target=user, args=(q,))
#     t2 = threading.Thread(target=str_up, args=(q,))
#
#     t1.start()
#     t2.start()

# from threading import Thread
# import os
#
#
# def work():
#     print('hello', os.getpid())
#     print('hello', os.getpid())
#
#
# if __name__ == '__main__':
#     t1 = Thread(target=work)
#     t2 = Thread(target=work)
#     t1.start()
#     t2.start()
#     print('主线程', os.getpid())
#
# from multiprocessing import Process
#
# print("=====================")
#
#
# def work1():
#     print('word', os.getpid())
#
#
# if __name__ == '__main__':
#     t2 = Process(target=work1)
#     t3 = Process(target=work1)
#     t2.start()
#     t3.start()
#     print("主进程", os.getpid())


