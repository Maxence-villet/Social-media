from Tools import BFS

class PropagationPath:

    def __init__(self):
        self.visited = []
        self.node_to_index = {}

    def best_path(self, graph_tuple, start, end):
        SOM, MAT = graph_tuple
        
        bfs_start = bfs(start)
        self.visited = []
        self.node_to_index = {node: i for i, node in enumerate(SOM)}

        while bfs_start:
            current, path = bfs_start.popleft()
            if current == end:
                return path
            if current not in self.visited:
                self.visited.append(current)
                current_index = self.node_to_index[current]
                for neighbor_index, is_connected in enumerate(MAT[current_index]):
                    if is_connected:
                        neighbor = SOM[neighbor_index]
                        bfs_start.append((neighbor, path + [neighbor]))

        raise ValueError(f"No path find between {start} eand {end}.")

