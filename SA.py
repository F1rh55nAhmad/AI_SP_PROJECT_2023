import random
import math


class SimulatedAnealing:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight

        if not self.directed:
            if node2 not in self.graph:
                self.graph[node2] = {}
            self.graph[node2][node1] = weight

    def get_neighbors(self, node):
        if node in self.graph:
            return self.graph[node]
        return {}

    def simulated_annealing_search(self, start, goals, temperature=1000, cooling_rate=0.99):
        current_node = start
        current_cost = 0
        current_path = [current_node]

        while temperature > 1:
            neighbors = self.get_neighbors(current_node)
            next_node = random.choice(list(neighbors.keys()))
            next_cost = current_cost + neighbors[next_node]

            if next_node in goals:
                current_node = next_node
                current_cost = next_cost
                current_path.append(current_node)
                return current_path, current_cost, current_node

            if next_cost < current_cost:
                current_node = next_node
                current_cost = next_cost
                current_path.append(current_node)
            else:
                acceptance_probability = math.exp((current_cost - next_cost) / temperature)
                if random.random() < acceptance_probability:
                    current_node = next_node
                    current_cost = next_cost
                    current_path.append(current_node)

            temperature *= cooling_rate

        return None, None, None

    def print_path(self, path):
        print(' -> '.join(path))

