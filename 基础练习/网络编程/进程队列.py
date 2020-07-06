from multiprocessing import process, Queue

q = Queue(3)
q.put(1)
q.put(2)
q.put(3)
print(q.full())
# q.put(4)  # 放不进去阻塞住了

print(q.get())
print(q.get())
print(q.get())
print(q.empty())
# print(q.get())   # 在取就阻塞主了
