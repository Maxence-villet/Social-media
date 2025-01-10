class Dfs:
    def __init__(self):
        self.visited_nodes = []

    def visited_dfs(self, graph_tuple, start):
        """
        Initialize the visited nodes and do the dfs function below

        Args:
        ------
        [graph_tuple] (tuple of a list and of a list of a list) : a tuple where we can find our matrix and our nodes
        [start] (str, int, ... whatever you want) : this node is where we want to applie the DFS algorithm from

        Returns:
        ---------
        type : (list) of visited nodes with the DFS applies
        """
        SOM, MAT = graph_tuple
        if start not in SOM :
            print("The node doesn't exit, you should pick another 'start' node")
            return None
        self.visited_nodes = []
        self.node_to_index = {node: i for i, node in enumerate(SOM)} # create a ditionnary where each nodes have their unique index value
        self.dfs(graph_tuple, start) # applies the DFS algorithm
    
        return self.visited_nodes

    def dfs(self, graph_tuple, node) :
        """
        A recursion function where we applie the DFS algorithm

        Args:
        ------
        [graph_tuple] (tuple of a list and of a list of a list) : a tuple where we can find our matrix and our nodes
        [node] (str, int, ... whatever you want) : this node is where we want to applie the DFS algorithm from,
        and is from a seed at the beggining of this recursion

        Returns:
        ---------
        type : (fonction) This function returns the same function to apply recursion, which will allow obtaining all possible depth paths."
        """
        nodes, matrix = graph_tuple

        if node not in self.visited_nodes :
            self.visited_nodes.append(node)
            node_index = self.node_to_index[node]
        
            for i, is_connected in enumerate(matrix[node_index]):
                if is_connected:
                    self.dfs(graph_tuple, nodes[i])

