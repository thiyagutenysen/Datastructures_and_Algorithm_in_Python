# a linked list is represented by a pointer to the first node of the linked list.
# The first node is called the head

# Node representation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List representation


class LinkedList:
    def __init__(self):
        self.head = None


# create a linked list with 3 nodes

# creation of nodes
llist = LinkedList()
llist.head = Node(1)  # llist.head has the address of first node
second = Node(2)
third = Node(3)
# linking of nodes
llist.head.next = second
second.next = third

# Traversal of linked list


def print_list(head):
    temp = head
    while(temp != None):
        print(temp.data)
        temp = temp.next
    print(head, temp)


print_list(llist.head)
