class Node:
	def __init__(self, data):
		self.data = data
		self.parent = None
		self.children = []

class Tree:
	def __init__(self):
		self.root = None
