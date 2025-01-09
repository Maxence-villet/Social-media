from BFS import bfs

class PropagationPath:

    def __init__(self):
        self.visited = []
        self.node_to_index = {}

    def bfs_bidirectionnel(self, graph_tuple, start, end):
        SOM, MAT = graph_tuple
        bfs_start = bfs(start)
        bfs_end = bfs(end)
        self.visited = []
        self.node_to_index = {node: i for i, node in enumerate(SOM)}

        while bfs_start and bfs_end:
            for i in enumerate(bfs_end):
                for 

