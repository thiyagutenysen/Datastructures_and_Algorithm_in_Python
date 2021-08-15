class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LLQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def print_queue(self):
        temp = self.head
        while(temp != None):
            print(temp.data, "->", end=" ")
            temp = temp.next
        print()

    def peek(self):
        if self.size == 0:
            return "Empty queue"
        return self.head.data

    def dequeue(self):
        if self.size == 0:
            raise Exception("cannot dequeue empty queue")
        deleted_item = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return deleted_item

    def enqueue(self, data):
        node = Node(data)
        if self.size == 0:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1


Q = LLQueue()
Q.enqueue(5)
Q.print_queue()
Q.enqueue(3)
Q.print_queue()
print(len(Q))
print(Q.dequeue())
Q.print_queue()
print(Q.isEmpty())
print(Q.dequeue())
Q.print_queue()
print(Q.isEmpty())
# print(Q.dequeue())
Q.print_queue()
Q.enqueue(7)
Q.print_queue()
Q.enqueue(9)
Q.print_queue()
print(Q.peek())
Q.enqueue(4)
Q.print_queue()
print(len(Q))
print(Q.dequeue())
Q.print_queue()
