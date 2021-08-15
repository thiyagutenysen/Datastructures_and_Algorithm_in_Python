from heapq import heappush, heappop, heapify

# create an empty array
heap = []

# heapify converts any list into MIN heap in linear time
heapify(heap)

# add elements to the heap (insert) - O(logn)
heappush(heap, 10)
heappush(heap, 30)
heappush(heap, 20)
heappush(heap, 400)

# get minimum value of the heap
print("Min element = ", heap[0])

# level order traversal
print("Min-Heap =", heap)

# extract_min - O(logn)
popped = heappop(heap)
print("Min popped element =", popped)

# level order traversal
print("Min-Heap =", heap)
