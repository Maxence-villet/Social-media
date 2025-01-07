from Tools import arcs

def main():

    matrix_adjacency = [
    #matrix_test
        [0, 1, 1],
        [1, 0, 0],
        [0, 1, 0]
    ]
    #list_test
    list_adjacency = {

        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B'],
        'D': ['A'],
    }

    #instance of arc
    a = arcs.Arcs()

    #display of the count matrice and list results
    print(a.count_matrix(matrix_adjacency))
    print(a.count_list(list_adjacency))

main()
