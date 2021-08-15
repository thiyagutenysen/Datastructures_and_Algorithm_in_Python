from heapq import heappush, heappop, heapify

# create an empty array
heap = []

# heapify converts any list into MIN heap in linear time
heapify(heap)

# add elements to the heap (insert) - O(logn)
heappush(heap, -1*10)
heappush(heap, -1*30)
heappush(heap, -1*20)
heappush(heap, -1*400)

# get maximum value of the heap
print("Max element = ", -1*heap[0])

# level order traversal
print("Max-Heap =", [-1*i for i in heap])

# extract_max - O(logn)
popped = -1*heappop(heap)
print("Max popped element =", popped)

# level order traversal
print("Max-Heap =", [-1*i for i in heap])
