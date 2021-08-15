import queue

stack = queue.LifoQueue(maxsize=3)

# number of elements in the stack
print(stack.qsize())

# add elements to stack
stack.put(1)
stack.put(2)
stack.put(3)

# check if stack is full - ie., it reached it's max capacity
print(stack.full())

# check number of elements in the stack again
print(stack.qsize())

# pop elements from stack
print(stack.get())
print(stack.get())
print(stack.get())

# check if stack is empty
print(stack.empty())
