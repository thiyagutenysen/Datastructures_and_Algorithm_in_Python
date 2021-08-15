from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# inorder traversal


def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

# inorder traversal


def preorder(root):
    if root != None:
        print(root.data)
        inorder(root.left)
        inorder(root.right)

# inorder traversal


def postorder(root):
    if root != None:
        inorder(root.left)
        inorder(root.right)
        print(root.data)

# level order traversal


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


# create tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# output
print("inorder traversal =")
inorder(root)
print("preorder traversal =")
preorder(root)
print("postorder traversal =")
postorder(root)
print("levelorder traversal =")
levelorder(root)
