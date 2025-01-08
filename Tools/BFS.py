from collections import deque

def bfs(graph, root):
    """
    Performs a breadth-first search (BFS) on a given graph.

    Args:
        graph (dict): A dictionary representing a graph, where keys are nodes
        and values ​​are lists of neighboring nodes.

        root (any): The starting node for breadth-first search.

    Returns:
        set: A set containing all visited nodes.

    
    """
    visited = set()
    queue = deque([root])

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)

    return visited
