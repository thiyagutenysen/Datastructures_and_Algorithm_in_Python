# Simple dijkstra implementation - O(V^2)
import sys


class WeightedGraph:
    def __init__(self, v):
        self.vertices = v
        self.graph = [[0]*self.vertices for _ in range(self.vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.vertices):
            print(node, "\t", dist[node])

    def min_distance(self, dist, visited):
        min_value = sys.maxsize
        min_index = None
        for i in range(self.vertices):
            if i not in visited:
                if min_value > dist[i]:
                    min_value = dist[i]
                    min_index = i
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize]*self.vertices
        dist[src] = 0
        visited = set()
        for _ in range(self.vertices):
            v = self.min_distance(dist, visited)
            visited.add(v)
            for neighbor in range(self.vertices):
                if (neighbor not in visited) and (self.graph[v][neighbor] > 0):
                    if dist[neighbor] > (dist[v] + self.graph[v][neighbor]):
                        dist[neighbor] = (dist[v] + self.graph[v][neighbor])
        self.printSolution(dist)


# Output
g = WeightedGraph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]
g.dijkstra(0)
