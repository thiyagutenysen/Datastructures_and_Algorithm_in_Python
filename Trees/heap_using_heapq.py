# https://www.geeksforgeeks.org/binary-heap/

# By simply calling heap we mean array implementation of min-heap
# We are gonna implement only 2 extra methods than minheap_using_heapq.py

# Method 1 - decreaseKey(): Decreases value of key.
# The time complexity of this operation is O(Logn).
# If the decreases key value of a node is greater than the parent of the node,
# then we don’t need to do anything. Otherwise,
# we need to traverse up to fix the violated heap property.

# Method 2 - delete(): Deleting a key also takes O(Logn) time.
# We replace the key to be deleted with minum infinite by calling decreaseKey().
# After decreaseKey(), the minus infinite value must reach root,
# so we call extractMin() to remove the key.

from heapq import heappush, heappop, heapify


class min_heap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)//2

    def get_min(self):
        return self.heap[0]

    def insert(self, data):
        heappush(self.heap, data)
    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]

    def decrease_data(self, i, new_data):
        self.heap[i] = new_data
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            self.heap[self.parent(
                i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]

    def extract_min(self):
        return heappop(self.heap)
    # This functon deletes key at index i. It first reduces
    # value to minus infinite and then calls extractMin()

    def delete_data(self, i):
        self.decrease_data(i, float("-inf"))
        self.extract_min()


# output
heapObj = min_heap()
heapObj.insert(3)
heapObj.insert(2)
heapObj.delete_data(1)
heapObj.insert(15)
heapObj.insert(5)
heapObj.insert(4)
heapObj.insert(45)

print(heapObj.extract_min())
print(heapObj.get_min())
heapObj.decrease_data(2, 1)
print(heapObj.get_min())
