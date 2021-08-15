# Construct Binary Tree from given Parent Array representation
# https://www.geeksforgeeks.org/construct-a-binary-tree-from-parent-array-representation/
# Given an array that represents a tree in such a way that array indexes are values in tree nodes and array values give the parent node of that particular index (or node). The value of the root node index would always be -1 as there is no parent for root.
# Construct the standard linked representation of given Binary Tree from this given representation.
# Input: parent[] = {1, 5, 5, 2, 2, -1, 3}
# Output: root of below tree
#           5
#         /  \
#        1    2
#       /    / \
#      0    3   4
#          /
#         6

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_node(parent, created, i, root):
    if created[i]:
        return root

    created[i] = Node(i)

    if parent[i] == -1:
        return created[i]

    if parent[i] == None:
        root = create_node(parent, created, parent[i], root)

    father = created[parent[i]]
    if father.left:
        father.right = created[i]
    else:
        father.left = created[i]

    return root


def construct_tree(parent):
    created = [None]*len(parent)
    root = None
    for i in range(len(parent)):
        root = create_node(parent, created, i, root)
    return root


def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


# output
parent = [-1, 0, 0, 1, 1, 3, 5]
root = construct_tree(parent)
print("Inorder Traversal of constructed tree")
inorder(root)
