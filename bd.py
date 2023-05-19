class Graph_bd:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append((node2, weight))
        if not self.directed:
            if node2 not in self.graph:
                self.graph[node2] = []
            self.graph[node2].append((node1, weight))

    def bidirectional_search(self, start, goals):
        queue1 = [(start, [start], 0)]
        queue2 = [(goal, [goal], 0) for goal in goals]
        visited1 = {start: 0}
        visited2 = {goal: 0 for goal in goals}
        common_node = None
        min_cost = float('inf')

        while queue1 and queue2:
            current_node1, path1, cost1 = queue1.pop(0)
            current_node2, path2, cost2 = queue2.pop(0)

            if current_node1 == current_node2:
                if cost1 + cost2 < min_cost:
                    min_cost = cost1 + cost2
                    common_node = current_node1

            if cost1 < visited1[current_node1]:
                visited1[current_node1] = cost1
                for neighbor, weight in self.graph.get(current_node1, []):
                    if neighbor not in visited1 or cost1 + weight < visited1[neighbor]:
                        queue1.append((neighbor, path1 + [neighbor], cost1 + weight))

            if cost2 < visited2[current_node2]:
                visited2[current_node2] = cost2
                for neighbor, weight in self.graph.get(current_node2, []):
                    if neighbor not in visited2 or cost2 + weight < visited2[neighbor]:
                        queue2.append((neighbor, path2 + [neighbor], cost2 + weight))

        if common_node is not None:
            path1 = self.get_path(visited1, common_node)
            path2 = self.get_path(visited2, common_node)
            path = path1[::-1] + path2[1:]
            return path, common_node
        else:
            return None, None

    def get_path(self, visited, node):
        path = []
        while node in visited:
            path.append(node)
            node = visited[node]
        return path

    def print_path(self, path, goal):
        if path is None:
            print("No path found.")
        else:
            print("Path:", end=' ')
            for node in path:
                print(node, end=' ')
            print("\nCost:", sum(self.get_edge_weight(path[i], path[i+1]) for i in range(len(path)-1)))

    def get_edge_weight(self, node1, node2):
        edges = self.graph.get(node1, [])
        for neighbor, weight in edges:
            if neighbor == node2:
                return weight
        return 0
