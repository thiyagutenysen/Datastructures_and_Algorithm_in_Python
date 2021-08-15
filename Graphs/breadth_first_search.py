# Breadth First Traversal (or Search) for a graph is similar to
# Breadth First Traversal of a tree (See method 2 of this post).
# The only catch here is, unlike trees, graphs may contain cycles,
# so we may come to the same node again. To avoid processing a node more than once,
# we use a boolean visited array.

from collections import deque, defaultdict


class Connected_Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def bfs(self, v):
        visited = set()
        queue = deque()
        queue.append(v)
        visited.add(v)
        while(queue):
            v = queue.popleft()
            print(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# output
g = Connected_Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.bfs(2)


class DisConnected_Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def bfs(self):
        visited = set()
        queue = deque()
        for node in list(self.graph.keys()):
            if node not in visited:
                queue.append(node)
                visited.add(node)
                while(queue):
                    v = queue.popleft()
                    print(v)
                    for neighbor in self.graph[v]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)


# output
g = DisConnected_Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.add_edge(9, 8)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.bfs()
