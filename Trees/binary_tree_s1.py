# Node representation for a binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# class Tree:
# 	def __init__(self):
# 		self.root = None


# let's create a simple tree with 4 nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
