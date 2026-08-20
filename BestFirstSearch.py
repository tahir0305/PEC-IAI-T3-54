import heapq

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': ['T'],
    'F': ['R'],
    'G': ['N'],
    'H': ['O', 'P'],
    'I': ['P', 'Q'],
    'J': ['R'],
    'O': [],
    'P': [],
    'Q': [],
    'R': [],
    'T': [],
    'N': []
}

h = {
    'A': 5,
    'B': 4,
    'C': 4,
    'D': 6,
    'E': 5,
    'F': 5,
    'G': 4,
    'H': 3,
    'I': 0,
    'J': 0,
    'O': 2,
    'P': 3,
    'Q': 0,
    'R': 4,
    'T': 5,
    'N': 0
}

start = 'A'
goal = 'P'

open = [(h[start], start)]
closed = []
parent = {start: None}

while open:

    value, node = heapq.heappop(open)

    if node in closed:
        continue

    closed.append(node)

    if node == goal:
        break

    for neighbour in graph[node]:
        if neighbour not in closed:
            heapq.heappush(open, (h[neighbour], neighbour))

            if neighbour not in parent:
                parent[neighbour] = node

print("Closed:", closed)

# Find solution path
path = []
node = goal

while node is not None:
    path.append(node)
    node = parent[node]

path.reverse()

print("Solution Path:", path)