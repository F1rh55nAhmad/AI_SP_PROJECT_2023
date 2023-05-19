from collections import defaultdict
import heapq

class AlphaBetaPruning:
    def __init__(self, directed):
        self.graph = defaultdict(dict)
        self.directed = directed

    def add_edge(self, node1, node2, weight):
        self.graph[node1][node2] = weight

        if not self.directed:
            self.graph[node2][node1] = weight

    def get_neighbors(self, node):
        return self.graph[node]

    def alpha_beta_search(self, start, goals):
        goal_pqs = {goal: [(float('-inf'), 0, start, [])] for goal in goals}
        visited = set()
        best_path = {}
        best_cost = {}
        best_goal = None

        while any(goal_pqs.values()):
            for goal, pq in goal_pqs.items():
                if not pq:
                    continue
                score, cost, node, path = heapq.heappop(pq)

                if node in visited:
                    continue
                visited.add(node)

                if node == goal:
                    if goal not in best_cost or cost < best_cost[goal]:
                        best_cost[goal] = cost
                        best_path[goal] = path + [node]
                        best_goal = goal

                for neighbor, weight in self.get_neighbors(node).items():
                    new_path = path + [node]
                    new_cost = cost + weight
                    new_score = new_cost + sum(self.graph[neighbor].values())

                    if neighbor in best_cost and new_cost >= best_cost[neighbor]:
                        continue

                    heapq.heappush(goal_pqs[goal], (new_score, new_cost, neighbor, new_path))

        return best_path[best_goal], best_cost[best_goal], best_goal

    def print_path(self, path):
        print(' -> '.join(str(node) for node in path))
