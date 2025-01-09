class PropagationPath:

    def __init__(self):
        self.node_to_index = {}

    def best_path(self, graph_tuple, start, end):
        
        SOM, MAT = graph_tuple
        self.node_to_index = {node: i for i, node in enumerate(SOM)}

        if start not in SOM or end not in SOM:
            raise ValueError(f"Node {start} or node {end} is not in the graph.")

        queue = [(start, [start])]

        while queue:
            current, path = queue.pop(0)

            if current == end:
                return path
            
            current_index = self.node_to_index[current]


            for neighbor_index, is_connected in enumerate(MAT[current_index]):
                neighbor = SOM[neighbor_index]

                if is_connected == 1 and neighbor not in path:
                    queue.append((neighbor, path + [neighbor]))

        raise ValueError(f"No path find between {start} and {end}.")

