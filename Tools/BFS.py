class BFS:
    def __init__(self):
        self.visited = set()

    def bfs(self, graph, root):
        """
        Performs a breadth-first search (BFS) on a given graph using a list as the queue.
        Neighbors are visited in a sorted order.

     Args:
        graph (list[list[int]]): A matrix representing a graph, where keys are nodes
        and values are lists of neighboring nodes.

        root (any): The starting node for breadth-first search.

    Returns:
        list: A list of visited nodes in the order they were explored.
    """
        SOM, MAT = graph  # SOM represents the nodes and MAT the adjacency matrix of the graph
        if root not in SOM:
            # Checks if the starting node is valid
            raise ValueError("Ce nœud n'est pas correct, veuillez choisir un nœud disponible dans votre liste de nœuds")
        
        queue = [SOM.index(root)]  # Initializes the queue with the index of the starting node
        self.visited = set(root)  # Mark the starting node as visited
        result = []  # List to store visited nodes in visited order

        while queue:
            node = queue.pop(0)  # Retrieves and removes the first element from the queue
            result.append(SOM[node])  # Adds the current node to the results list

            for neighbor in range(len(SOM)):  # Browse  neighbors
                # Checks if the neighbor is online and has not been visited yet
                if MAT[node][neighbor] == 1 and SOM[neighbor] not in self.visited:
                    self.visited.add(SOM[neighbor])  # Mark neighbor as visited
                    queue.append(neighbor)  # Add neighbor to queue

        return result  # Returns the list of visited nodes



