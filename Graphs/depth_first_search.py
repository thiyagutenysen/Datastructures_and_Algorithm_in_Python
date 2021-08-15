# Depth First Traversal (or Search) for a graph is similar to
# Depth First Traversal of a tree(inorder, preorder, postorder).
# The only catch here is, unlike trees, graphs may contain cycles, a node may be visited twice.
# To avoid processing a node more than once, use a boolean visited array.

# we will implement dfs in directed graph
from collections import defaultdict


class Connected_Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def dfs_recursion(self, v, visited):
        visited.add(v)
        print(v)
        for i in self.graph[v]:
            if i not in visited:
                self.dfs_recursion(i, visited)

    def dfs(self, v):
        visited = set()
        print("Visiting order =")
        self.dfs_recursion(v, visited)
        # print("Visiting order =", visited) - Wrrroooonggggggg, wrong


# output
g = Connected_Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.dfs(2)


class DisConnected_Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def dfs_recursion(self, v, visited):
        visited.add(v)
        print(v)
        for i in self.graph[v]:
            if i not in visited:
                self.dfs_recursion(i, visited)

    def dfs(self):
        visited = set()
        print("Visiting order =")
        for node in list(self.graph.keys()):
            if node not in visited:
                '''visited is modified globally'''
                self.dfs_recursion(node, visited)


# output
g = DisConnected_Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.add_edge(9, 8)

print("Following is DFS from (starting from vertex 2)")
g.dfs()

# Iterative implementation of dfs algorithm


class IterDisConnected_Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def dfs(self):
        visited = set()
        stack = []
        print("Visiting order =")
        for node in list(self.graph.keys()):
            if node not in visited:
                stack.append(node)
                while(stack):
                    v = stack.pop()
                    if v not in visited:
                        stack.extend(self.graph[v])
                        visited.add(v)
                        print(v)


# output
g = IterDisConnected_Graph()
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(1, 4)

print("Following is Depth First Traversal")
g.dfs()
