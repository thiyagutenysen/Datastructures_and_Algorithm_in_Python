# Doubly Linked List

# Doubly linked list node representation
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    # reference a linked list by head
    def __init__(self):
        self.head = None
    # traverse a linked list and print

    def print_list(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next
    # add a node at the front of the list

    def push(self, new_data):
        node = Node(new_data)
        node.next = self.head
        if self.head != None:
            self.head.prev = node
        self.head = node
        node.prev = None
    # add a node after a given node

    def insert_after(self, new_data, prev_node):
        if prev_node == None:
            print(" None is given as previous node ")
            return
        node = Node(new_data)
        node.next = prev_node.next
        node.prev = prev_node
        prev_node.next = node
    # add a node at the end

    def append(self, new_data):
        temp = self.head
        node = Node(new_data)
        if temp == None:
            self.head = node
        else:
            while(temp.next != None):
                temp = temp.next
            node.prev = temp
            temp.next = node
    # add a node before a given node

    def insert_before(self, new_data, next_node):
        node = Node(new_data)
        node.next = next_node
        node.prev = next_node.prev
        if next_node.prev != None:
            next_node.prev.next = node
        next_node.prev = node


llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(4)
llist.insert_before(8, llist.head.next)
llist.print_list()
