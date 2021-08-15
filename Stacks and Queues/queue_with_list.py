class ArrayQueue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def print_queue(self):
        print("(", self.queue, "queue_size =",
              self.size, "front =", self.front, ")")

    def peek(self):
        if self.size == 0:
            return "Empty queue"
        return self.queue[self.front]

    def dequeue(self):
        if self.size == 0:
            raise Exception("cannot dequeue empty queue")
        deleted_item = self.queue[self.front]
        self.queue[self.front] = 0
        self.front = (self.front+1) % len(self.queue)
        self.size -= 1
        return deleted_item

    def enqueue(self, data):
        if self.front > 0:
            self.reorder()
        if self.front+self.size < len(self.queue):
            self.queue[self.front+self.size] = data
            self.size += 1
            return
        self.queue.append(data)
        self.size += 1

    def reorder(self):
        new_queue = [0]*self.size
        index = 0
        for i in range(self.front, len(self.queue)):
            new_queue[index] = self.queue[i]
            index += 1
        self.queue = new_queue
        self.front = 0


Q = ArrayQueue()
Q.print_queue()
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
