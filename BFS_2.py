from collections import deque

# Graph representation
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['G', 'H'],
    'C': ['E', 'F'],
    'D': [],
    'G': ['I'],
    'H': [],
    'E': ['K'],
    'F': [],
    'I': [],
    'K': []
}

start = 'S'
goal = 'K'

queue = deque([start])
visited = []
parent = {start: None}

while queue:
    node = queue.popleft()

    if node not in visited:
        visited.append(node)

        if node == goal:
            break

        for neighbor in graph[node]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                parent[neighbor] = node

print("BFS Traversal:", visited)

# Find path
path = []
current = goal

while current is not None:
    path.append(current)
    current = parent[current]

path.reverse()

print("Goal Path:", path)