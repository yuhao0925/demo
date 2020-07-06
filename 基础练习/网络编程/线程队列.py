import queue

# 队列  先进先出
q = queue.Queue()
q.put('1')
q.put('2')
q.put('3')

print(q.get())
print(q.get())
print(q.get())

print("=" * 10)

# 栈stack
q1 = queue.LifoQueue()
q1.put('1')
q1.put('2')
q1.put('3')

print(q1.get())
print(q1.get())
print(q1.get())

print("=" * 10)

# 优先级队列：存储数据时可设置优先级的队列
q2 = queue.PriorityQueue()
# put进入一个元组,元组的第一个元素是优先级(通常是数字,
# 也可以是非数字之间的比较),数字越小优先级越高
q2.put((20, 'a'))
q2.put((10, 'b'))
q2.put((5, 'c'))

print(q2.get())
print(q2.get())
print(q2.get())
