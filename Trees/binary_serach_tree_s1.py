class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# insert a node into the BST version-1


def insert(root, data):

    if root == None:
        return Node(data)

    if data <= root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root

# insert a node into the BST version-2


def insert2(root, data):
    if root == None:
        root = Node(data)
    else:
        if data <= root.data:
            if root.left == None:
                root.left = Node(data)
            else:
                insert(root.left, data)
        else:
            if root.right == None:
                root.right = Node(data)
            else:
                insert(root.right, data)

# insert a node into the BST version-3 iterative method


def insert3(root, data):
    if root == None:
        root = Node(data)
    while(root != None):
        if data <= root.data:
            if root.left == None:
                root.left = Node(data)
                break
            else:
                root = root.left
        else:
            if root.right == None:
                root.right = Node(data)
                break
            else:
                root = root.right

# traversal


def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


# create a BST
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

# output
print("insert1 =")
inorder(r)

r = Node(50)
insert2(r, 30)
insert2(r, 20)
insert2(r, 40)
insert2(r, 70)
insert2(r, 60)
insert2(r, 80)

# output
print("insert2 =")
inorder(r)

r = Node(50)
insert3(r, 30)
insert3(r, 20)
insert3(r, 40)
insert3(r, 70)
insert3(r, 60)
insert3(r, 80)

# output
print("insert3 =")
inorder(r)
