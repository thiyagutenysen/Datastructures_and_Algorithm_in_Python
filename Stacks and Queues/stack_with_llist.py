class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LLStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def push(self, data):
        # we add node at the front
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def peek(self):
        # return the head or front node data
        if self.head == None:
            return "Nothing"
        else:
            return self.head.data

    def pop(self):
        # we delete node at the front
        if self.head == None:
            return "Empty stack cannot be popped"
        else:
            deleted_data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return deleted_data


S = LLStack()
S.push(5)
S.push(3)
print(len(S))
print(S.pop())
print(S.isEmpty())
print(S.pop())
print(S.isEmpty())
S.push(7)
S.push(9)
print(S.peek())
S.push(4)
print(len(S))
print(S.pop())
S.push(6)
