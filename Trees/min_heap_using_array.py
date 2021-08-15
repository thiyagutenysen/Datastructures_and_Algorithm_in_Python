# A Min Heap is a Complete Binary Tree. A Min heap is typically represented as an array.
# The root element will be at Arr[0]. For any ith node, i.e., Arr[i]:

# Arr[(i -1) / 2] returns its parent node.
# Arr[(2 * i) + 1] returns its left child node.
# Arr[(2 * i) + 2] returns its right child node.

import sys


class min_heap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [sys.maxsize]*(self.maxsize+1)
        # this line of code is to not give error when parent of root is called
        self.heap[0] = -1*sys.maxsize

    def parent(self, pos):
        return (pos)//2

    def left_child(self, pos):
        return (2*pos)

    def right_child(self, pos):
        return (2*pos)+1

    def is_leaf(self, pos):
        leaf_start = self.size//2
        if pos > leaf_start:
            return True
        return False

    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def min_heapify(self, pos):
        '''Bubble down algorithm, helpful only in extract_min operation'''
        if not self.is_leaf(pos):
            if ((self.heap[pos] > self.heap[self.left_child(pos)]) or (
                    self.heap[pos] > self.heap[self.right_child(pos)])):
                if self.heap[self.left_child(pos)] < self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.min_heapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.min_heapify(self.right_child(pos))

    def insert(self, data):
        if self.size >= self.maxsize:
            return

        self.heap[self.size+1] = data

        '''Bubble up algorithm'''
        current = self.size+1
        while(self.heap[current] < self.heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

        self.size += 1

    def extract_min(self):
        if self.size >= 1:
            popped = self.heap[1]
            self.swap(1, self.size)
            self.heap[self.size] = sys.maxsize
            self.size -= 1
            self.min_heapify(1)
            return popped
        else:
            return

    def minHeap(self):
        '''Function to build the min heap using the minHeapify function'''
        for i in range(self.size//2, 0, -1):
            self.min_heapify(i)

    def levelorder(self):
        print(self.heap)

    def heap_print(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : " + str(self.heap[i])+" LEFT CHILD : " +
                  str(self.heap[2 * i])+" RIGHT CHILD : " +
                  str(self.heap[2 * i + 1]))


# output
print('The minHeap is ')
minHeap = min_heap(15)
minHeap.insert(5)
minHeap.insert(3)
minHeap.insert(17)
minHeap.insert(10)
minHeap.insert(84)
minHeap.insert(19)
minHeap.insert(6)
minHeap.insert(22)
minHeap.insert(9)
print("min-heap =")
minHeap.levelorder()
minHeap.minHeap()
print("min-heap =")
minHeap.levelorder()
print("min-heap =")
minHeap.heap_print()
print("The Min val is " + str(minHeap.extract_min()))
print("min-heap =")
minHeap.levelorder()
