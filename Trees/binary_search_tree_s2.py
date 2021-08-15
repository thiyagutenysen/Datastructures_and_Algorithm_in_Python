# how to delete a node in the BST
# there are 3 cases to consider when we try to delete a node
# 1. Node to be deleted is the leaf
# 2. Node to be deleted has only one child
# 3. Node to be deleted has two children

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

# check number of children of a node and return atleast one child node


def check_children(root):
    count = 0
    child = None
    if root.left:
        count += 1
        child = root.left
    if root.right:
        count += 1
        child = root.right
    return count, child

# successor retrieval for 2 child case


def inorder_successor(node):
    root = node.right
    while(root.left != None):
        root = root.left
    return root

# how to delete node in a BST


def delete(root, data):
    if root == None:
        return root

    if root.data == data:
        children, child_node = check_children(root)
        if children == 0:
            return None
        elif children == 1:
            return child_node
        else:
            successor = inorder_successor(root)
            root.data = successor.data
            root.right = delete(root.right, successor.data)
            return root

    elif data < root.data:
        root.left = delete(root.left, data)

    else:
        root.right = delete(root.right, data)

    return root

# traversal


def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


# output
""" Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 """

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = delete(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 30")
root = delete(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 50")
root = delete(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)
