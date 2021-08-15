# How to search in BST

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# insert node in BST


def insert(root, data):

    if root == None:
        return Node(data)

    if data <= root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root

# search in BST


def search(root, data):
    if root is None:
        return False
    elif root.data == data:
        return root
    elif data < root.data:
        return search(root.left, data)
    else:
        return search(root.right, data)


# output
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# search query
print(search(r, 10))
