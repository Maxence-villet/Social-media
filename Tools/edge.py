class Edge:
    def __init__(self):
        """
        Initializes an Edge object with attributes to store sums of adjacency matrix and list.

        Attributes:
        -----------
        sum_matrice (int): Sum of edges counted from the adjacency matrix.
        sum_list (int): Sum of edges counted from the adjacency list.
        """
        self.sum_matrice:int
        self.sum_list:int
    
    def count_matrice(self, matrice_adjacence):
        """
        Counts the number of edges in a given adjacency matrix.

        Args:
        ------
        matrice_adjacence (list of list of int): The adjacency matrix representing the graph.

        Returns:
        --------
        int: The number of edges in the graph, divided by 2 for asymmetric matrices.
             Returns 0 if the matrix is not square or an error occurs.
        """
        
        #reset value
        self.sum_matrice = 0
        
        try:
            for i in range(0, len(matrice_adjacence)):
                for j in range(0,len(matrice_adjacence)):
                    if matrice_adjacence[i][j] == 1:
                        self.sum_matrice += 1
        except Exception as e:
            print(f"La matrice n'est pas carree | error: {e}")    
            return 0
        return int(self.sum_matrice/2) #asymetric
    
    def count_list(self, list_adjacence:dict) :
        """
        Counts the number of edges in a given adjacency list.

        Args:
        ------
        list_adjacence (dict): The adjacency list representing the graph.

        Returns:
        --------
        int: The number of edges in the graph.
        """
        
        #reset value
        self.sum_list = 0

        for i in list_adjacence.values():
            self.sum_list += 1
        return self.sum_list


