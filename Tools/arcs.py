class Arcs:
    def __init__(self):
        """
        initialize of the instance
        """
        self.sum_matrix:int
        self.sum_list:int
    
    def count_matrix(self, matrix_adjacency) :
        """
        Count the number of arcs in a matrix

        Args:
        ------
        [matrix_adjacency] (list of list of int) : a binary matrix where we can find neighbors and Predecessor of nodes
        Returns:
        ---------
        type : int : it returns the number of Arcs in a matrix

        """
        self.sum_matrix = 0 # initialize the sum_matrix value
        try:
            for i in range(0, len(matrix_adjacency)):
                for j in range(0,len(matrix_adjacency)):
                    if matrix_adjacency[i][j] == 1:
                        self.sum_matrix += 1
        except Exception as e:
            print(f"La matrice n'est pas carree | error: {e}")    
            return 0
        return int(self.sum_matrix)

    def count_list(self,list_adjacency:dict) :
        """
        Count the number of arcs in a list

        Args:
        ------
        [list_adjacency] (dict) : dictionnary with nodes as key(s) and list of neighbor(s) as value(s)
        Returns:
        ---------
        int : the number of Arcs in a list

        """
        self.sum_list = 0 # initialize the sum_list value
        for i in list_adjacency.values():
            if i == [] : # pass if the list is empty
                continue
            self.sum_list += 1
        return self.sum_list
