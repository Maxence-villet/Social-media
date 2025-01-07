from Tools import edge




def main():  
    # List
    liste_adjacence = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B'],
        'D': ['A', 'B'],
        'E': ['A', 'B']
    }

    # Matrice
    matrice = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    
    # instance of edge
    e = edge.Edge()

    # print number of previous values
    print(e.count_matrice(matrice))
    print(e.count_list(liste_adjacence))


