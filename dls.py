class Graph_dls:
    def __init__(self, directed=False):
        self.adjacency_list = {}
        self.directed = directed

    def add_edge(self, node1, node2, weight=None):
        if node1 not in self.adjacency_list:
            self.adjacency_list[node1] = []
        if node2 not in self.adjacency_list:
            self.adjacency_list[node2] = []
        self.adjacency_list[node1].append((node2, weight))
        if not self.directed:
            self.adjacency_list[node2].append((node1, weight))

    def depth_limited_search(self, start, goals, depth_limit):
        visited = set()
        stack = [(start, [start], 0)]
        while stack:
            node, traced_path, depth = stack.pop()
            if node not in visited:
                visited.add(node)
                if node in goals:
                    return traced_path, node, depth
                if depth < depth_limit:
                    for neighbor, _ in self.adjacency_list[node]:
                        if neighbor not in visited:
                            stack.append((neighbor, traced_path + [neighbor], depth + 1))
        return None, None, None

    def print_path(self, traced_path, goal):
        if traced_path:
            for i in range(len(traced_path) - 1):
                print(traced_path[i], "->", end=" ")
            print(goal)
        else:
            print("No path found.")
