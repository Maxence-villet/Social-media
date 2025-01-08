class Top1:
    def __init__(self):
        self.top = []
        self.node_to_index = {}

    def influencer(self, graph_tuple):
        SOM, MAT = graph_tuple
        self.top = []
        list_neighbor = [0] * len(SOM)
        self.node_to_index = {node: i for i, node in enumerate(SOM)}

        for index in range(len(SOM)):
            for i, is_connected in enumerate(MAT):
                if is_connected[index] == 1:
                    list_neighbor[index] += 1

        self.top = self.Top_Infl(list_neighbor)
        return [SOM[i] for i in self.top]

    def Top_Infl(self, list_neighbor):
        if not list_neighbor:
            print("La liste ne peut pas être vide")
            return None

        top_value = max(list_neighbor)
        top_list = [index for index, value in enumerate(list_neighbor) if value == top_value]
    
        return top_list


