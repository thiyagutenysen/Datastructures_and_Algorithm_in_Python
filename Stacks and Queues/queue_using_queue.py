from queue import Queue

# methods
# 0. Queue(maxsize=N)
# 1. put(76)
# 2. get()
# 3. empty()
# 4. qsize()
# 5. full()

# initialize a queue
q = Queue(maxsize=3)

# number of items in the queue
print("number of items in the queue", q.qsize())

# enqueue
q.put(1)
q.put(2)
q.put(3)

# show queue
# we cannot print the whole queue
# print("print whole queue =", q)

# check if queue is filled fully
print("check if queue is filled fully", q.full())

# dequeue
print("dequeue", q.get())
print("dequeue", q.get())
print("dequeue", q.get())

# check if queue is empty
print("check if queue is empty", q.empty())
