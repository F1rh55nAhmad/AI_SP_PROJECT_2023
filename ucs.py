from queue import PriorityQueue

class Graph_ucs:
    def __init__(self, directed=False):
        self.adjacency_list = {}
        self.directed = directed

    def add_edge(self, node1, node2, cost):
        if node1 not in self.adjacency_list:
            self.adjacency_list[node1] = []
        if node2 not in self.adjacency_list:
            self.adjacency_list[node2] = []
        self.adjacency_list[node1].append((node2, cost))
        if not self.directed:
            self.adjacency_list[node2].append((node1, cost))

    def uniform_cost_search(self, start, goals):
        visited = set()
        queue = PriorityQueue()
        queue.put((0, start, [start], 0))  # (priority, node, path, cost)
        while not queue.empty():
            _, node, traced_path, total_cost = queue.get()
            if node not in visited:
                visited.add(node)
                if node in goals:
                    return traced_path, node, total_cost
                for neighbor, cost in self.adjacency_list[node]:
                    if neighbor not in visited:
                        new_path = traced_path + [neighbor]
                        new_cost = total_cost + cost
                        queue.put((new_cost, neighbor, new_path, new_cost))
        return None, None, None

    def print_path(self, traced_path, goal, total_cost):
        if traced_path:
            for i in range(len(traced_path) - 1):
                print(traced_path[i], "->", end=" ")
            print(goal)
            print("Total cost:", total_cost)
        else:
            print("No path found.")
