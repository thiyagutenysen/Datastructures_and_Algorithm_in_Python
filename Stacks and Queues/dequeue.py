# Dequeues of collection module is an implementation of doubly linked list
# adding and deleting at both ends are much faster
# Indexing is very slow

from collections import deque

# Primary operations - O(1)
dqueue = deque()
# append() :- This function is used to insert the value in its argument to the right end of deque.
dqueue.append('last')
# appendleft() :- This function is used to insert the value in its argument to the left end of deque.
dqueue.appendleft('start')
# access the first element
print(dqueue[0])
# access the last element
print(dqueue[-1])
# pop() :- This function is used to delete an argument from the right end of deque.
print(dqueue.pop())
# popleft() :- This function is used to delete an argument from the left end of deque.
print(dqueue.popleft())


# Secondary operations - O(N)
