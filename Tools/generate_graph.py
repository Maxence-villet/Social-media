import random


class Generate_Graph:
    def __init__(self):
        self.vertices
        self.communities = []
        self.edges = []
        self.oriented

    def generate_graph(self, oriented, num_vertices, min_degree, max_degree, num_communities, max_distance):
        self.generate_vertices(num_vertices)
        self.generate_communities(num_communities)

        if(oriented == False):
            inverse_edge = [(y, x) for x, y in edges]
            edges = edges + inverse_edge

        return vertices, edges, communities

    def setOriented(self, oriented):
        if not oriented:
            raise ValueError("oriented ne peux pas être vide")
        
        if type(oriented) != bool:
            raise ValueError("L'orientation doit être un boolean")
        
        self.oriented = oriented
    
    def generate_vertices(self, num_vertices):
        """
        this function generate an vertices list

        Args:
        -----
            num_vertices (int) : number of vertices

        Returns:
        --------
            None

        """
        if not num_vertices:
            raise ValueError("num_vertices ne peux pas être vide")
        
        if type(num_vertices) != int:
            raise ValueError("Le nombre de sommets doit être un entier")
        
        self.vertices = list(range(num_vertices))
    
    def generate_communities(self, num_communities):
        """
        this function generate an communities list

        Args:
        -----
            num_communities (int) : number of communities

        Returns:
        --------
            None

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

    def generate_edges(self, min_degree, max_degree):
        """
        this function generate an edges list

        Args:
        -----
            min_degree (int) : minimal degree allow
            max_degree (int) : maximal degree allow

        Returns:
        --------
            None

        """
        if not min_degree:
            raise ValueError("min_degree ne peux pas être vide")
        
        if type(min_degree) != int:
            raise ValueError("Le nombre minimal de degree doit être un entier")

        if not max_degree:
            raise ValueError("max_degree ne peux pas être vide")
        
        if type(max_degree) != int:
            raise ValueError("Le nombre maximal de degree doit être un entier")

        for vertex in self.vertices:
            degree = random.randint(min_degree, max_degree)
            possible_neighbors = [v for v in self.vertices if v != vertex]
            neighbors = random.sample(possible_neighbors, min(degree, len(possible_neighbors)))
            
            for neighbor in neighbors:
                if self.oriented:
                    self.edges.append((vertex, neighbor))
                else:
                    if (neighbor, vertex) not in self.edges:
                        self.edges.append((vertex, neighbor))
    
    def generate_max_distance(self, max_distance):
        """
        this function generate an edges list with maximal distance

        Args:
        -----
            
            max_distance (int) : maximal distance of edges from _ to _

        Returns:
        --------
            None

        """

        if not max_distance:
            raise ValueError("max_distance ne peux pas être vide")
        
        if type(max_distance) != int:
            raise ValueError("La distance maximal doit être un entier")

        if max_distance:
            self.edges = [edge for edge in self.edges if abs(edge[0] - edge[1]) <= max_distance]
        
        
    def save_graph_to_file(self, filename, oriented, vertices, edges):
        with open(filename, 'w') as file:
            file.write("GRAPHE ORIENTE\n" if oriented else "GRAPHE NON ORIENTE\n")
            file.write(f"{len(vertices)} SOMMETS\n")
            for vertex in vertices:
                file.write(f"{vertex}\n")
            file.write(f"{len(edges)} ARCS\n" if oriented else f"{len(edges)} ARETES\n")
            for edge in edges:
                file.write(f"{edge[0]} {edge[1]}\n")

