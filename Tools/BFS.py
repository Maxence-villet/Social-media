def bfs(graph, root):
    """
    Performs a breadth-first search (BFS) on a given graph using a list as the queue.
    Neighbors are visited in a sorted order.

    Args:
        graph (dict): A dictionary representing a graph, where keys are nodes
        and values are lists of neighboring nodes.

        root (any): The starting node for breadth-first search.

    Returns:
        list: A list of visited nodes in the order they were explored.
    """
    visited = set()
    queue = [root]  
    result = []  

    while queue:
        vertex = queue.pop(0)  
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in sorted(graph[vertex]):  
                if neighbor not in visited:
                    queue.append(neighbor)

    return result  


# Example : 
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


visited_nodes = bfs(graph, 'F')
print("node visited :", visited_nodes)
