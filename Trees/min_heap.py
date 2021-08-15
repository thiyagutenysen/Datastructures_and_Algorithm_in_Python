from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class min_heap():
    def __init__(self):
        self.root = None

    def swap_data(self, node1, node2):
        temp = node1.data
        node1.data = node2.data
        node2.data = temp

    def add_last(self, data):
        new_node = Node(data)
        q = deque()
        q.append(self.root)
        while(len(q) != 0):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            else:
                node.left = new_node
                break
            if node.right:
                q.append(node.right)
            else:
                node.right = new_node
                break
        new_node.parent = node
        return new_node

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return

        new_node = self.add_last(data)
        while(new_node.parent != None):
            if new_node.data < new_node.parent.data:
                self.swap_data(new_node, new_node.parent)
                new_node = new_node.parent
            else:
                break
                # self.root = new_node
        return

    def last_element(self):
        q = deque()
        q.append(self.root)
        n = len(q)
        last_node = None
        while(n != 0):
            last_node = q[-1]
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            n = len(q)
        return last_node

    def bubble_down(self, node):
        left_child = node.left
        right_child = node.right
        if left_child == None:
            pass
        elif right_child == None:
            if node.data > left_child.data:
                self.swap_data(node, left_child)
                self.bubble_down(left_child)
        else:
            if left_child.data < right_child.data:
                if node.data > left_child.data:
                    self.swap_data(node, left_child)
                    self.bubble_down(left_child)
            else:
                if node.data > right_child.data:
                    self.swap_data(node, right_child)
                    self.bubble_down(right_child)

    def extract_min(self):
        if self.root == None:
            return "no min heap"
        last_node = self.last_element()
        extracted_min = self.root.data
        self.swap_data(last_node, self.root)

        parent = last_node.parent
        if parent != None:
            if parent.left == last_node:
                parent.left = None
            else:
                parent.right = None
        else:
            self.root = None
            return extracted_min

        self.bubble_down(self.root)
        return extracted_min


def levelorder(root):
    if root == None:
        return
    q = deque()
    q.append(root)
    while(len(q) != 0):
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        print(node.data)


# output
print('The minHeap is ')
minHeap = min_heap()
minHeap.insert(5)
print("Min-Heap =")
levelorder(minHeap.root)
minHeap.insert(3)
print("Min-Heap =")
levelorder(minHeap.root)
minHeap.insert(17)
print("Min-Heap =")
levelorder(minHeap.root)
minHeap.insert(10)
print("Min-Heap =")
levelorder(minHeap.root)
minHeap.insert(84)
print("Min-Heap =")
levelorder(minHeap.root)
minHeap.insert(19)
print("Min-Heap =")
levelorder(minHeap.root)
minHeap.insert(6)
print("Min-Heap =")
levelorder(minHeap.root)
minHeap.insert(22)
print("Min-Heap =")
levelorder(minHeap.root)
minHeap.insert(9)
print("Min-Heap =")
levelorder(minHeap.root)
print("The Min val is " + str(minHeap.extract_min()))
print("Min-Heap =")
levelorder(minHeap.root)
print("The Min val is " + str(minHeap.extract_min()))
print("Min-Heap =")
levelorder(minHeap.root)
print("The Min val is " + str(minHeap.extract_min()))
print("Min-Heap =")
levelorder(minHeap.root)
print("The Min val is " + str(minHeap.extract_min()))
print("Min-Heap =")
levelorder(minHeap.root)
print("The Min val is " + str(minHeap.extract_min()))
print("Min-Heap =")
levelorder(minHeap.root)
print("The Min val is " + str(minHeap.extract_min()))
print("Min-Heap =")
levelorder(minHeap.root)
print("The Min val is " + str(minHeap.extract_min()))
print("Min-Heap =")
levelorder(minHeap.root)
print("The Min val is " + str(minHeap.extract_min()))
print("Min-Heap =")
levelorder(minHeap.root)
print("The Min val is " + str(minHeap.extract_min()))
print("Min-Heap =")
levelorder(minHeap.root)
print("The Min val is " + str(minHeap.extract_min()))
print("Min-Heap =")
levelorder(minHeap.root)
