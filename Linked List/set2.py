# insertion of a node
# it can be done in 3 ways
# 1. front of the list
# 2. after a given node
# 3. at the end of the list
class Node:
    def __init__(self, data):
        self.data = data
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
        self.head = node
    # add a node after a given node

    def insert_after_node(self, prev_node, new_data):
        if prev_node == None:
            print(" Given node is none")
        node = Node(new_data)
        node.next = prev_node.next
        prev_node.next = node
    # add a node after a given data

    def insert_after_data(self, new_data, node_data):
        node = Node(new_data)
        temp = self.head
        while(temp != None):
            if temp.data == node_data:
                node.next = temp.next
                temp.next = node
                break
            else:
                temp = temp.next
    # add a node at the end

    def append(self, new_data):
        node = Node(new_data)
        if self.head == None:
            self.head = node
            return
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = node


llist = LinkedList()
llist.append(6)
llist.push(7)
llist.push(1)
llist.append(4)
llist.insert_after_node(llist.head.next, 8)
llist.print_list()
