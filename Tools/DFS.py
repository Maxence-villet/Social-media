class Dfs:
    def __init__(self):
        self.visited_nodes = []

    def visited_dfs(self, graph_tuple, start):
        SOM, MAT = graph_tuple 
        self.visited_nodes = []
        self.node_to_index = {node: i for i, node in enumerate(SOM)}
        self.dfs(graph_tuple, start)
    
        return self.visited_nodes

    def dfs(self, graph_tuple, node) :
        nodes, matrix = graph_tuple

        if node not in self.visited_nodes :
            self.visited_nodes.append(node)
            node_index = self.node_to_index[node]
        
            for i, is_connected in enumerate(matrix[node_index]):
                if is_connected:
                    self.dfs(graph_tuple, nodes[i])

