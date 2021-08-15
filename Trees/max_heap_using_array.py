# A Max Heap is a Complete Binary Tree. A Max heap is typically represented as an array.
# The root element will be at Arr[0].
# Below table shows indexes of other nodes for the ith node, i.e., Arr[i]:
# Arr[(i-1)/2] Returns the parent node.
# Arr[(2*i)+1] Returns the left child node.
# Arr[(2*i)+2] Returns the right child node.

import sys


class max_heap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [-1*sys.maxsize]*(self.maxsize+1)
        # this line of code is to not give error when parent of root is called
        self.heap[0] = sys.maxsize

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

    def max_heapify(self, pos):
        '''Bubble down algorithm, helpful only in extract_max operation'''
        if not self.is_leaf(pos):
            if ((self.heap[pos] < self.heap[self.left_child(pos)]) or (
                    self.heap[pos] < self.heap[self.right_child(pos)])):
                if self.heap[self.left_child(pos)] > self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.max_heapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.max_heapify(self.right_child(pos))

    def insert(self, data):
        if self.size >= self.maxsize:
            return

        self.heap[self.size+1] = data

        '''Bubble up algorithm'''
        current = self.size+1
        while(self.heap[current] > self.heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

        self.size += 1

    def extract_max(self):
        if self.size >= 1:
            popped = self.heap[1]
            self.swap(1, self.size)
            self.heap[self.size] = -1*sys.maxsize
            self.size -= 1
            self.max_heapify(1)
            return popped
        else:
            return

    def maxHeap(self):
        '''Function to build the max heap using the maxHeapify function'''
        for i in range(self.size//2, 0, -1):
            self.max_heapify(i)

    def levelorder(self):
        print(self.heap)

    def heap_print(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : " + str(self.heap[i])+" LEFT CHILD : " +
                  str(self.heap[2 * i])+" RIGHT CHILD : " +
                  str(self.heap[2 * i + 1]))


# output
print('The maxHeap is ')
maxHeap = max_heap(15)
maxHeap.insert(5)
maxHeap.insert(3)
maxHeap.insert(17)
maxHeap.insert(10)
maxHeap.insert(84)
maxHeap.insert(19)
maxHeap.insert(6)
maxHeap.insert(22)
maxHeap.insert(9)
print("max-heap =")
maxHeap.levelorder()
maxHeap.maxHeap()
print("max-heap =")
maxHeap.levelorder()
print("max-heap =")
maxHeap.heap_print()
print("The Max val is " + str(maxHeap.extract_max()))
print("max-heap =")
maxHeap.levelorder()
