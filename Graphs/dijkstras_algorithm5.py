# More general algorithm Using adjacency list

import sys
from collections import defaultdict
from heapq import heappush, heappop


class WeightedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, src, dest, weight):
        self.graph[src].append((dest, weight))
        self.graph[dest].append((src, weight))

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in self.graph:
            print(node, "\t", dist[node])

    def dijkstra(self, src):
        dist = dict.fromkeys(self.graph, sys.maxsize)
        dist[src] = 0
        pq = [(dist[src], src)]
        while(pq):
            node = heappop(pq)
            v = node[1]
            print("popped node =", v)
            dist_v = node[0]
            if dist_v > dist[v]:
                continue
            for neighbor, weight in self.graph[v]:
                if dist[neighbor] > (dist_v + weight):
                    dist[neighbor] = (dist_v + weight)
                    heappush(pq, (dist[neighbor], neighbor))
            print(pq)
        self.printSolution(dist)


# Output
graph = WeightedGraph()
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.dijkstra(0)
