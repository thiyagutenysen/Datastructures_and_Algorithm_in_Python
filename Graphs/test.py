import sys
from heapq import heappush, heappop, heapify


class WeightedGraph:
    def __init__(self, v):
        self.vertices = v
        self.graph = [[0]*self.vertices for _ in range(self.vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.vertices):
            print(node, "\t", dist[node])

    def dijkstra(self, src):
        dist = [sys.maxsize]*self.vertices
        dist[src] = 0
        visited = set()
        pq = [(dist[src], src)]
        for _ in range(self.vertices):
            node = heappop(pq)
            v = node[1]
            dist_v = node[0]
            visited.add(v)
            for neighbor in range(self.vertices):
                if (neighbor not in visited) and (self.graph[v][neighbor] > 0):
                    if dist[neighbor] > (dist_v + self.graph[v][neighbor]):
                        dist[neighbor] = (dist_v + self.graph[v][neighbor])
                        heappush(pq, (dist[neighbor], neighbor))
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
