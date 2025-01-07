from collections import deque

def bfs(graph, root):
    
    visited = set()
    queue = deque([root])

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)

    return visited

