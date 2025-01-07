class Edge:
    def __init__(self):
        self.sum_matrice:input = 0
        self.sum_list:int = 0
    
    def count_matrice(self, matrice_adjacence):
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
        for i in list_adjacence.values():
            self.sum_list += 1;
        return self.sum_list


