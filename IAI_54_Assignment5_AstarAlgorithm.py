import heapq

# Graph
graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('D', 2), ('C', 3)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('G', 3), ('H', 2), ('E', 5), ('J', 3)],
    'J': [('E', 5), ('I', 3)]
}

# Heuristic values
h = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}

def astar(start, goal):

    queue = [(h[start], 0, start)]
    cost = {start: 0}
    parent = {start: None}

    while queue:

        f, g, current = heapq.heappop(queue)

        if current == goal:
            break

        for neighbour, edge_cost in graph[current]:

            new_cost = g + edge_cost

            if neighbour not in cost or new_cost < cost[neighbour]:

                cost[neighbour] = new_cost
                f = new_cost + h[neighbour]

                heapq.heappush(queue, (f, new_cost, neighbour))

                parent[neighbour] = current

    # Construct path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("Path:", " -> ".join(path))
    print("Total Cost:", cost[goal])


astar('A', 'J')