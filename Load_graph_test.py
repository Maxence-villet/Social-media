from Tools import Load_graph

# Example usage
filename = 'test2.txt'
l = Load_graph.LoadGraph()
vertices, matrix = l.process_graph_file(filename)

print("Matrice d'adjacence:")
for row in matrix:
    print(row)
print("\nListe d'adjacence:")
