class Arcs:
    def __init__(self):
        self.sum_matrix:input = 0
        self.sum_list:int = 0
    
    def count_matrix(self, matrix_adjacency) :
        try:
            for i in range(0, len(matrix_adjacency)):
                for j in range(0,len(matrix_adjacency)):
                    if matrix_adjacency[i][j] == 1:
                        self.sum_matrice += 1
        except Exception as e:
            print(f"La matrice n'est pas carree | error: {e}")    
            return 0
        return int(self.sum_matrice)

    def count_list(self,list_adjacency:dict) :
        for i in list_adjacency.values():
            self.sum_list += 1
        return self.sum_list
