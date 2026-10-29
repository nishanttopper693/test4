import heapq

class MapSearchSystem:
    def __init__(self):

        self.graph = {
            'City_A': {'City_B': 5, 'City_C': 8, 'City_D': 12},
            'City_B': {'City_A': 5, 'City_E': 7, 'City_F': 15},
            'City_C': {'City_A': 8, 'City_G': 9},
            'City_D': {'City_A': 12, 'City_H': 6},
            'City_E': {'City_B': 7, 'City_I': 8},
            'City_F': {'City_B': 15, 'City_J': 5},
            'City_G': {'City_C': 9, 'City_J': 11},
            'City_H': {'City_D': 6, 'City_I': 4},
            'City_I': {'City_E': 8, 'City_H': 4, 'City_J': 9},
            'City_J': {'City_F': 5, 'City_G': 11, 'City_I': 9}
        }
        
        self.heuristics = {
            'City_A': 18,
            'City_B': 12,
            'City_C': 15,
            'City_D': 10,
            'City_E': 8,
            'City_F': 4,
            'City_G': 10,
            'City_H': 7,
            'City_I': 5,
            'City_J': 0
        }

    def uniform_cost_search(self, start, goal):
        """Uninformed Search: Uniform Cost Search (UCS / Dijkstra)"""

        pq = [(0, start, [start])]
        visited = set()
        nodes_explored = 0

        while pq:
            cost, current, path = heapq.heappop(pq)
            nodes_explored += 1

            if current == goal:
                return path, cost, nodes_explored

            if current not in visited:
                visited.add(current)
                for neighbor, weight in self.graph[current].items():
                    if neighbor not in visited:
                        heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
                        
        return None, float('inf'), nodes_explored

    def a_star_search(self, start, goal):
        """Informed Search: A* Search using f(n) = g(n) + h(n)"""

        initial_f = 0 + self.heuristics[start]
        pq = [(initial_f, 0, start, [start])]
        closed_set = set()
        nodes_explored = 0

        while pq:
            f, g, current, path = heapq.heappop(pq)
            nodes_explored += 1

            if current == goal:
                return path, g, nodes_explored

            if current not in closed_set:
                closed_set.add(current)
                for neighbor, weight in self.graph[current].items():
                    if neighbor in closed_set:
                        continue
                    
                    g_new = g + weight
                    f_new = g_new + self.heuristics[neighbor]
                    heapq.heappush(pq, (f_new, g_new, neighbor, path + [neighbor]))
                        
        return None, float('inf'), nodes_explored

if __name__ == "__main__":
    system = MapSearchSystem()
    start_city = 'City_A'
    goal_city = 'City_J'

    print(f"--- Finding Shortest Path from {start_city} to {goal_city} ---\n")

    ucs_path, ucs_cost, ucs_nodes = system.uniform_cost_search(start_city, goal_city)
    print("Uninformed Search (Uniform Cost Search):")
    print(f"  * Path: {' -> '.join(ucs_path)}")
    print(f"  * Total Distance (Cost): {ucs_cost} km")
    print(f"  * Nodes Explored: {ucs_nodes}\n")
    
    astar_path, astar_cost, astar_nodes = system.a_star_search(start_city, goal_city)
    print("Informed Search (A* Search):")
    print(f"  * Path: {' -> '.join(astar_path)}")
    print(f"  * Total Distance (Cost): {astar_cost} km")
    print(f"  * Nodes Explored: {astar_nodes}\n")

    print("--- Analysis ---")
    print(f"Both algorithms successfully found the optimal path with a cost of {ucs_cost} km.")
    print(f"A* Search explored {astar_nodes} nodes, whereas UCS explored {ucs_nodes} nodes.")
    print("Conclusion: Informed search (A*) expands fewer nodes because it uses heuristic straight-line distance guidance toward the goal, making it more efficient than uninformed search.")