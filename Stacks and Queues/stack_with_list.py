class ArrayStack:
    def __init__(self):
        self.stack = []
        self.top = 0

    def __len__(self):
        return self.top

    def isEmpty(self):
        if self.top == 0:
            return True
        return False

    def push(self, data):
        if len(self.stack) == self.top:
            self.stack.append(data)
        else:
            self.stack[self.top] = data
        self.top += 1

    def peek(self):
        if self.top == 0:
            return "stack is empty"
        else:
            return self.stack[self.top - 1]

    def pop(self):
        if self.top == 0:
            print("stack is empty")
        else:
            deleted_item = self.stack[self.top - 1]
            self.top -= 1
            return deleted_item


S = ArrayStack()
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
