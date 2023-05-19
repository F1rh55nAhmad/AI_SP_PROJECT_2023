class Graph_ids:
    def __init__(self, directed=False):
        self.adjacency_list = {}
        self.directed = directed

    def add_edge(self, node1, node2,weight=None):
        if node1 not in self.adjacency_list:
            self.adjacency_list[node1] = []
        if node2 not in self.adjacency_list:
            self.adjacency_list[node2] = []
        self.adjacency_list[node1].append((node2,weight))
        if not self.directed:
            self.adjacency_list[node2].append((node1,weight))

    def depth_limited_search(self, start, goals, depth_limit):
        visited = set()
        stack = [(start, [start])]
        while stack:
            node, traced_path = stack.pop()
            if node not in visited:
                visited.add(node)
                if node in goals:
                    return traced_path, node
                if len(traced_path) <= depth_limit:
                    for neighbor in self.adjacency_list[node]:
                        if neighbor[0] not in visited:
                            stack.append((neighbor[0], traced_path + [neighbor[0]]))
        return None, None

    def iterative_deepening_search(self, start, goals, max_depth):
        for depth_limit in range(max_depth + 1):
            traced_path, goal = self.depth_limited_search(start, goals, depth_limit)
            if goal is not None:
                return traced_path, goal
        return None, None

    def print_path(self, traced_path, goal):
        if traced_path:
            for i in range(len(traced_path) - 1):
                print(traced_path[i], "->", end=" ")
            print(goal)
        else:
            print("No path found.")
