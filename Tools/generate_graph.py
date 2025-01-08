import random


class Generate_Graph:
    def __init__(self):
        pass

    def generate_graph(self, oriented, num_vertices, min_degree, max_degree, num_communities, max_distance):
        # Générer les sommets
        vertices = list(range(num_vertices))
        
        # Générer les communautés
        communities = []
        remaining_vertices = vertices.copy()
        for _ in range(num_communities):
            if not remaining_vertices:
                break
            community_size = random.randint(1, len(remaining_vertices))
            community = random.sample(remaining_vertices, community_size)
            communities.append(community)
            remaining_vertices = [v for v in remaining_vertices if v not in community]
        
        # Générer les arcs/arêtes
        edges = []
        for vertex in vertices:
            degree = random.randint(min_degree, max_degree)
            possible_neighbors = [v for v in vertices if v != vertex]
            neighbors = random.sample(possible_neighbors, min(degree, len(possible_neighbors)))
            
            for neighbor in neighbors:
                if oriented:
                    edges.append((vertex, neighbor))
                else:
                    if (neighbor, vertex) not in edges:
                        edges.append((vertex, neighbor))
        
        # Appliquer la contrainte de distance maximale
        if max_distance:
            edges = [edge for edge in edges if abs(edge[0] - edge[1]) <= max_distance]
        
        return vertices, edges, communities

    def save_graph_to_file(self, filename, oriented, vertices, edges):
        with open(filename, 'w') as file:
            file.write("GRAPHE ORIENTE\n" if oriented else "GRAPHE NON ORIENTE\n")
            file.write(f"{len(vertices)} SOMMETS\n")
            for vertex in vertices:
                file.write(f"{vertex}\n")
            file.write(f"{len(edges)} ARCS\n" if oriented else f"{len(edges)} ARETES\n")
            for edge in edges:
                file.write(f"{edge[0]} {edge[1]}\n")

