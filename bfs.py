class Graph_bfs:
    def __init__(self, directed=False):
        self.adjacency_list = {}
        self.directed = directed

    def add_edge(self, node1, node2):
        if node1 not in self.adjacency_list:
            self.adjacency_list[node1] = []
        if node2 not in self.adjacency_list:
            self.adjacency_list[node2] = []
        self.adjacency_list[node1].append(node2)
        if not self.directed:
            self.adjacency_list[node2].append(node1)

    def breadth_first_search(self, start, goals):
        visited = set()
        queue = [(start, [start])]
        while queue:
            node, traced_path = queue.pop(0)
            if node not in visited:
                visited.add(node)
                if node in goals:
                    return traced_path, node
                for neighbor in self.adjacency_list[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, traced_path + [neighbor]))
        return None, None

    def print_path(self, traced_path, goal):
        if traced_path:
            for i in range(len(traced_path) - 1):
                print(traced_path[i], "->", end=" ")
            print(goal)
        else:
            print("No path found.")
