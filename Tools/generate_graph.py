import random


class Generate_Graph:
    def __init__(self):
        self.vertices
        self.communities = []

    def generate_graph(self, oriented, num_vertices, min_degree, max_degree, num_communities, max_distance):
        self.generate_vertices(num_vertices)
        self.generate_communities(num_communities)
        
        
        # Générer les arcs/arêtes
        edges = []
        for vertex in self.vertices:
            degree = random.randint(min_degree, max_degree)
            possible_neighbors = [v for v in self.vertices if v != vertex]
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
        
        if(oriented == False):
            inverse_edge = [(y, x) for x, y in edges]
            edges = edges + inverse_edge
            
        return vertices, edges, communities

    def generate_vertices(self, num_vertices) -> list[int]:
        """
        this function generate an vertices list

        Args:
        -----
        num_vertices (int) : number of vertices

        Returns:
        --------
        (list[int]) : list of vertices

        """
        if not num_vertices:
            raise ValueError("num_vertices ne peux pas être vide")
        
        if type(num_vertices) != int:
            raise ValueError("Le nombre de sommets doit être un entier")
        
        self.vertices = list(range(num_vertices))
    
    def generate_communities(self, num_communities) -> list[int]:
        """
        this function generate an communities list

        Args:
        -----
        num_communities (int) : number of communities

        Returns:
        --------
        (list[int]) : list of communities

        """
        if not num_communities:
            raise ValueError("num_communities ne peux pas être vide")
        
        if type(num_communities) != int:
            raise ValueError("Le nombre de communautées doit être un entier")
        
        remaining_vertices = self.vertices.copy()
        for _ in range(num_communities):
            if not remaining_vertices:
                break
            community_size = random.randint(1, len(remaining_vertices))
            community = random.sample(remaining_vertices, community_size)
            self.communities.append(community)
            remaining_vertices = [v for v in remaining_vertices if v not in community]


    def save_graph_to_file(self, filename, oriented, vertices, edges):
        with open(filename, 'w') as file:
            file.write("GRAPHE ORIENTE\n" if oriented else "GRAPHE NON ORIENTE\n")
            file.write(f"{len(vertices)} SOMMETS\n")
            for vertex in vertices:
                file.write(f"{vertex}\n")
            file.write(f"{len(edges)} ARCS\n" if oriented else f"{len(edges)} ARETES\n")
            for edge in edges:
                file.write(f"{edge[0]} {edge[1]}\n")

