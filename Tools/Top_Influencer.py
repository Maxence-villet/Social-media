class Top1:
    def __init__(self):
        self.top = []
        self.node_to_index = {}

    def influencer(self, graph_tuple):
        """
        This fonction enumerate the neighbor(e) of each nodes and save it in a list

        Args:
        ------
        [graph_tuple] (tuple of a list and of a list of a list) : a tuple where we can find our matrix and our nodes

        Returns:
        ---------
        type : (list) of the node(s) with the most amount of neighbor
        """
        SOM, MAT = graph_tuple
        self.top = []
        list_neighbor = [0] * len(SOM) # It will be increment so we need to set them up at 0
        self.node_to_index = {node: i for i, node in enumerate(SOM)} # It's a dictionnary where each nodes have their index as key

        for index in range(len(SOM)):
            for i, is_connected in enumerate(MAT): # it will travel from column to column 
                if is_connected[index] == 1: # if it's a neighbor in the matrix (=1) it will add a new neighbor in the list at the index of the node who corresponds
                    list_neighbor[index] += 1

        self.top = self.Top_Infl(list_neighbor)
        return [SOM[i] for i in self.top]

    def Top_Infl(self, list_neighbor):
        """
        This function takes the biggest neighbor of the list and compared to all of the list of neighbor.
        If this is equal to the biggest neighbor possible it's save on a list. In case two or more nodes
        have the same amount of neighbor(s)

        Args:
        ------
        [list_neighbor] (list) : a list of the amount of neighbor(s) foreach nodes. Where the index of the list
        corresponds with the index of the SUM list (the list of the nodes in the tuple graph_tuple)

        Returns:
        ---------
        type : (list) of the index of the node(s) with the most amount of neighbor(s)
        """
        if not list_neighbor: # a protection if the list is empty
            print("La liste ne peut pas être vide")
            return None

        top_value = max(list_neighbor) # get the biggest value of neighbor
        top_list = [index for index, value in enumerate(list_neighbor) if value == top_value] # if the value is the same as the top value found, it will register the index in the list, in order to find the node associated with the index
    
        return top_list


