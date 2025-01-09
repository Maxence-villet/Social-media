class LoadGraph:
    def read_graph_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Remove any leading/trailing whitespace characters from each line
        lines = [line.strip() for line in lines]

        # Check if the first line is "GRAPHE ORIENTE" or "GRAPHE NON ORIENTE"
        if lines[0] not in ["GRAPHE ORIENTE", "GRAPHE NON ORIENTE"]:
            raise ValueError("Le fichier doit commencer par 'GRAPHE ORIENTE' ou 'GRAPHE NON ORIENTE'")

        is_oriented = lines[0] == "GRAPHE ORIENTE"

        # Check the second line for the number of vertices
        if not lines[1].endswith("SOMMETS"):
            raise ValueError("La deuxième ligne doit contenir le nombre de sommets suivi de 'SOMMETS'")

        num_vertices = int(lines[1].split()[0])

        # Read the vertices
        vertices = []
        for i in range(2, 2 + num_vertices):
            vertices.append(lines[i])

        # Check the line after vertices for the number of edges
        edges_line_index = 2 + num_vertices
        if is_oriented:
            if not lines[edges_line_index].endswith("ARCS"):
                raise ValueError("Pour un graphe orienté, la ligne suivante doit contenir le nombre d'arcs suivi de 'ARCS'")
        else:
            if not lines[edges_line_index].endswith("ARETES"):
                raise ValueError("Pour un graphe non orienté, la ligne suivante doit contenir le nombre d'arêtes suivi de 'ARETES'")

        num_edges = int(lines[edges_line_index].split()[0])

        # Read the edges
        edges = []
        for i in range(edges_line_index + 1, edges_line_index + 1 + num_edges):
            edge = tuple(lines[i].split())  # Keep edges as tuples of strings
            edges.append(edge)

        # For non-oriented graphs, check that edges are bidirectional
        if not is_oriented:
            for edge in edges:
                if (edge[1], edge[0]) not in edges:
                    raise ValueError(f"Pour un graphe non orienté, l'arête {edge} doit être présente dans les deux sens")

        return is_oriented, vertices, edges

    def create_adjacency_matrix(self, vertices, edges, is_oriented):
        num_vertices = len(vertices)
        matrix = [[0] * num_vertices for _ in range(num_vertices)]

        # Create a mapping from vertex to index
        vertex_to_index = {vertex: i for i, vertex in enumerate(vertices)}

        for edge in edges:
            src, dest = edge
            src_index = vertex_to_index[src]
            dest_index = vertex_to_index[dest]
            matrix[src_index][dest_index] = 1
            if not is_oriented:
                matrix[dest_index][src_index] = 1

        return matrix

    def create_adjacency_list(self, vertices, edges, is_oriented):
        adj_list = {vertex: [] for vertex in vertices}

        for edge in edges:
            src, dest = edge
            adj_list[src].append(dest)
            if not is_oriented:
                adj_list[dest].append(src)

        return adj_list

    def process_graph_file(self, filename):
        is_oriented, vertices, edges = self.read_graph_file(filename)

        adjacency_matrix = self.create_adjacency_matrix(vertices, edges, is_oriented)
        adjacency_list = self.create_adjacency_list(vertices, edges, is_oriented)

        return vertices, adjacency_matrix 