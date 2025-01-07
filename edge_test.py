from Tools import edge




def main():  
    # List
    list_adjacency = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B'],
        'D': ['A', 'B'],
        'E': ['A', 'B']
    }

    # matrix
    matrix = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]

    board_list_adjacency = {
    "Aurora": ["Olavi", "Tapio"],  
    "Ilona": [],                   
    "Olavi": ["Aurora"],           
    "Tapio": ["Aurora"]           
    }

    # instance of edge
    e = edge.Edge()

    # print number of previous values
    print(e.count_matrix(matrix))
    print(e.count_list(list_adjacency))
    print(e.count_list(board_list_adjacency))


main()