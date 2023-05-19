from collections import defaultdict
import heapq
import math


class Graph_astar:
    def __init__(self, directed=False):
        self.adjacency_list = defaultdict(list)
        self.directed = directed
        self.heuristic_dict = {}

    def heuristic(self, node, goal):
        x1, y1 = node
        x2, y2 = goal
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    def set_huristics(self, heuristic_dict):
        self.heuristic_dict = heuristic_dict

    @staticmethod
    def print_path(traced_path, goal):
        if traced_path:
            for i in range(len(traced_path) - 1):
                print(traced_path[i], "->", end=" ")
            print(goal)
        else:
            print("No path found.")

    def add_edge(self, node1, node2, cost):
        self.adjacency_list[node1].append((node2, cost))
        if not self.directed:
            self.adjacency_list[node2].append((node1, cost))

    def astar_search(self, start, goals):
        visited = set()
        queue = [(0, 0, start, [start])]
        heapq.heapify(queue)
        while queue:
            _, cost, node, traced_path = heapq.heappop(queue)
            if node not in visited:
                visited.add(node)
                if node in goals:
                    return traced_path, cost, node
                for neighbor, edge_cost in self.adjacency_list[node]:
                    if neighbor not in visited:
                        total_cost = cost + edge_cost
                        heuristic_cost = self.heuristic_dict.get(neighbor, 0)
                        heapq.heappush(
                            queue, (total_cost + heuristic_cost, total_cost, neighbor, traced_path + [neighbor])
                        )
        return None, None, None
