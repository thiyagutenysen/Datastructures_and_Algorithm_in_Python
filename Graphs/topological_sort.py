# Topological sorting for Directed Acyclic Graph (DAG)
# is a linear ordering of vertices such that for every directed edge u v,
# vertex u comes before v in the ordering.
# Topological Sorting for a graph is not possible if the graph is not a DAG.

# Idea
# 1. Find SINK
# 2. Put at end of order
# 3. Remove from graph
# 4. Repeat

# we are gonna use DFS which tries to fastly reach sink
# In dfs we print vertex and then search it's neighbors
# here we need to search neighbors and then add vertex to the stack and then
# pop the stack one by one and print the vertex values

from collections import defaultdict


class DAG:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def topological_sort_recursion(self, v, visited, stack):
        visited.add(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topological_sort_recursion(i, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = set()
        stack = []
        print("Visiting order =")
        for node in list(self.graph):
            if node not in visited:
                self.topological_sort_recursion(node, visited, stack)
        for i in range(len(stack)):
            print(stack.pop())


# Output
g = DAG()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Following is a Topological Sort of the given graph")

# Function Call
g.topological_sort()
