from collections import defaultdict
import heapq
import math


class Graph_best_first:
    def __init__(self, directed=False):
        self.adjacency_list = defaultdict(list)
        self.directed = directed
        self.heuristic_dict = {}

    def heuristic(self, node, goal):
        x1, y1 = node
        x2, y2 = goal
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    def set_heuristics(self, heuristic_dict):
        self.heuristic_dict = heuristic_dict

    @staticmethod
    def print_path(traced_path, goal):
        if traced_path:
            path = " -> ".join(map(str, traced_path))
            print(path)
        else:
            print("No path found.")

    def add_edge(self, node1, node2, weight):
        self.adjacency_list[node1].append((node2, weight))
        if not self.directed:
            self.adjacency_list[node2].append((node1, weight))

    def best_first_search(self, start, goals):
        visited = set()
        queue = [(0, start, [start])]
        heapq.heapify(queue)
        while queue:
            _, node, traced_path = heapq.heappop(queue)
            if node not in visited:
                visited.add(node)
                if node in goals:
                    return traced_path, self.calculate_cost(traced_path), node
                for neighbor, weight in self.adjacency_list[node]:
                    if neighbor not in visited:
                        new_traced_path = traced_path + [neighbor]
                        heapq.heappush(queue, (self.heuristic_dict.get(neighbor, 0), neighbor, new_traced_path))
        return None, None, None

    def calculate_cost(self, traced_path):
        cost = 0
        for i in range(len(traced_path) - 1):
            current_node = traced_path[i]
            next_node = traced_path[i + 1]
            for neighbor, weight in self.adjacency_list[current_node]:
                if neighbor == next_node:
                    cost += weight
                    break
        return cost
