class BFS:
    def __init__(self):
        self.visited = set()

    def bfs(self, graph, root):
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
        SOM, MAT = graph
        queue = [SOM.index(root)]
        self.visited = set(root)
        result = []

        while queue:
            node = queue.pop(0)
            result.append(SOM[node])

            for neighbor in range(len(SOM)):
                if MAT[node][neighbor] == 1 and SOM[neighbor] not in self.visited:
                    self.visited.add(SOM[neighbor])
                    queue.append(neighbor)

        return result  



