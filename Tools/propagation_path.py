class PropagationPath:

    def __init__(self):
        self.node_to_index = {}

    def best_path(self, graph_tuple, start, end):
        """
        This function return the best path from start to end

        Args:
        ------
        [start] (str or int or float) : the node where the path must start
        [end] (str or int or float) : the node where the path must end
        [graph_tuple] (tuple of a list and of a list of a list) : a tuple where we can find our matrix and our nodes

        Returns:
        --------
        [path] : (list) : the path where u pass trough in order to fin the node end
        """
        SOM, MAT = graph_tuple
        self.node_to_index = {node: i for i, node in enumerate(SOM)} # a dictionnary where all node(s) have their index attributed

        if start not in SOM or end not in SOM: #if Start or End are note present in the node list SOM it return an error
            raise ValueError(f"Node {start} or node {end} is not in the graph.")

        queue = [(start, [start])] # [(current, [path])] the current node with all the path

        while queue:
            current, path = queue.pop(0) # [(current, [path])] get the change values

            if current == end: # if we find the node end we can return the path
                return path
            
            current_index = self.node_to_index[current] # Get the name/SOM value from the node_to_index dictionnary

            for neighbor_index, is_connected in enumerate(MAT[current_index]): # check all the column of the current index

                neighbor = SOM[neighbor_index] # get the neighbor name from the SOM list
                if is_connected == 1 and neighbor not in path: # if it's a neighbor (==1) and not already in our path
                    queue.append((neighbor, path + [neighbor])) # We add in the truple queue the current and the path concatenate with the new current

        raise ValueError(f"No path find between {start} and {end}.") # if it doesn't find any path where end exist, an error occured

