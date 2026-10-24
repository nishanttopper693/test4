import heapq

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5, 'E': 3},
    'C': {'A': 2, 'D': 8, 'F': 6},
    'D': {'B': 5, 'C': 8, 'G': 2},
    'E': {'B': 3, 'G': 4},
    'F': {'C': 6, 'G': 3},
    'G': {'D': 2, 'E': 4, 'F': 3}
}

h = {'A': 7, 'B': 6, 'C': 5, 'D': 2, 'E': 4, 'F': 3, 'G': 0}


def bfs(start, goal):
    queue = [(start, [start], 0)]
    visited = []

    while queue:
        node, path, cost = queue.pop(0)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.append(node)
            for neighbour, distance in graph[node].items():
                if neighbour not in visited:
                    queue.append((neighbour, path + [neighbour],
                                  cost + distance))


def astar(start, goal):
    queue = [(h[start], 0, start, [start])]

    while queue:
        _, cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path, cost

        for neighbour, distance in graph[node].items():
            if neighbour not in path:
                new_cost = cost + distance
                heapq.heappush(queue, (
                    new_cost + h[neighbour],
                    new_cost,
                    neighbour,
                    path + [neighbour]
                ))


start = input("Enter start node (A-G): ").upper()
goal = input("Enter goal node (A-G): ").upper()

if start in graph and goal in graph:
    print("\nBFS Result:", bfs(start, goal))
    print("A* Result:", astar(start, goal))
else:
    print("Invalid node!")