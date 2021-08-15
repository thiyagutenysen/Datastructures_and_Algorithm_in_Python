# create a stack
stack = []
# push elements to the top of the stack
stack.append(1)
stack.append(2)
stack.append(3)
# return length of stack
print(len(stack))
# check if the stack is empty
if len(stack) == 0:
    print("True")
else:
    print("False")
# pop the element at the top of the stack
print(stack.pop())
print(stack.pop())
# peek at the stack
print(stack[-1])
