from collections import deque

# Graph representation
graph = {
    5: [3, 7],
    3: [2, 4],
    7: [8],
    2: [],
    4: [8],
    8: []
}

start = 5
goal = 8

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