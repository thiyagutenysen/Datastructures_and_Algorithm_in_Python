# There are two fundamental ways of representing a graph
# 1. Adjacency List - implemented using linked list or list or dictionary_of_sets
# 2. Adjacency Matrix - implemented using matrix
# The most important representation of them all is adjacency list using list.
from collections import defaultdict
# every example below is about undirected graph.

# Implementing adjacency list using linkedlist with continuous vertices from 1_to_n or 0_to_n - version1


class Node1:
    def __init__(self, data):
        self.data = data
        self.next = []


class Graph1:
    def __init__(self, v):
        self.vertices = v
        self.graph = [None]*v

    def add_edge(self, src, dest):
        if not self.graph[src]:
            self.graph[src] = Node1(src)
        if not self.graph[dest]:
            self.graph[dest] = Node1(dest)
        self.graph[src].next.append(self.graph[dest])
        self.graph[dest].next.append(self.graph[src])

    def print_graph(self):
        for i in range(self.vertices):
            print("Parent =", self.graph[i].data,
                  " --- Adjacency list = ", end="")
            for j in self.graph[i].next:
                print(j.data, ",", end=" ")
            print()


# output
V = 5
graph = Graph1(V)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.print_graph()
print("---------------------------------------")

# Implementing adjacency list using list with continuous vertices from 1_to_n or 0_to_n - version2


class Graph2:
    def __init__(self, v):
        self.vertices = v
        self.graph = [[] for i in range(self.vertices)]

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def print_graph(self):
        for i in range(self.vertices):
            print("Parent =", i, " --- Adjacency list = ", end="")
            for j in self.graph[i]:
                print(j, ",", end=" ")
            print()


# output
V = 5
graph = Graph2(V)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.print_graph()
print("---------------------------------------")

# Implementing adjacency matrix using matrix with continuous vertices from 1_to_n or 0_to_n - version1


class Graph3:
    def __init__(self, v):
        self.vertices = v
        self.graph = [[0]*v for i in range(self.vertices)]

    def add_edge(self, src, dest):
        self.graph[src][dest] = 1
        self.graph[dest][src] = 1

    def print_graph(self):
        for i in range(self.vertices):
            print(self.graph[i])


# output
V = 5
graph = Graph3(V)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.print_graph()
print("---------------------------------------")

# Implementing adjacency list using linked list with generic vertex names  - version3


class Node4:
    def __init__(self, data):
        self.data = data
        self.children = []


class Graph4:
    def __init__(self, v):
        self.vertices = 0
        self.graph = []

    def add_vertex(self, data):
        for vertex in self.graph:
            if vertex.data == data:
                return
        self.graph.append(Node4(data))

    def add_edge(self, src, dest):
        src_node = None
        dest_node = None
        for vertex in self.graph:
            if vertex.data == src:
                src_node = vertex
        for vertex in self.graph:
            if vertex.data == dest:
                dest_node = vertex
        if not src_node:
            src_node = Node4(src)
            self.graph.append(src_node)
        if not dest_node:
            dest_node = Node4(dest)
            self.graph.append(dest_node)
        src_node.children.append(dest_node)
        dest_node.children.append(src_node)

    def print_graph(self):
        for i in self.graph:
            print("Parent =", i.data,
                  " --- Adjacency list = ", end="")
            for j in i.children:
                print(j.data, ",", end=" ")
            print()


# output
V = 5
graph = Graph4(V)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.print_graph()
print("---------------------------------------")

# Implementing adjacency list using dictionary with generic vertex names  - version4


class Graph5:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def print_graph(self):
        for i in list(self.graph.keys()):
            print("Parent =", i,
                  " --- Adjacency list = ", end="")
            for j in self.graph[i]:
                print(j, ",", end=" ")
            print()


# output
V = 5
graph = Graph5()
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.print_graph()
print("---------------------------------------")
