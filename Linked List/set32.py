# Deleting a node
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
    # given a key, delete the first occurance of this key

    def recursive_delete_node(self, key):
        temp = self.head

        def remove(prev, temp, key):
            if temp == None:
                return
            elif temp.data == key:
                if prev == None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                return
            else:
                remove(temp, temp.next, key)
        remove(None, temp, key)


llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.print_list()
print("Deletion is happening...")
llist.recursive_delete_node(1)
print("After Deletion ")
llist.print_list()
