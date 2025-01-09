from Tools import generate_graph, DFS, BFS, Load_graph
import sys

class CLI:
    def __init__(self):
        self.argument = []
        self.args = sys.argv
        self.matrix = list[list[int]]
        self.vertices = int

    def check_args(self):
        
        print(len(self.args))
        for i in range(len(self.args)):
            print(self.args[i])

            if len(self.args) > 12:
                if self.args[i] == "generate":
                    self.argument.append(self.args[i])
                
                if self.args[i-1] == "generate" and self.args[i] == "--oriented":
                    self.argument.append(self.args[i])
                if self.args[i-1] == "generate" and self.args[i] == "--not_oriented":
                    self.argument.append(self.args[i])
                if self.args[i-2] == "generate" and self.args[i] == "--min_degree":
                    self.argument.append(self.args[i])
                if self.args[i-3] == "generate" and type(int(self.args[i])) == int:
                    self.argument.append(self.args[i])
                if self.args[i-4] == "generate" and self.args[i] == "--max_degree":
                    self.argument.append(self.args[i])
                if self.args[i-5] == "generate" and type(int(self.args[i])) == int:
                    self.argument.append(self.args[i])
                if self.args[i-6] == "generate" and self.args[i] == "--num_communities":
                    self.argument.append(self.args[i])
                if self.args[i-7] == "generate" and type(int(self.args[i])) == int:
                    self.argument.append(self.args[i])
                if self.args[i-8] == "generate" and self.args[i] == "--max_distance":
                    self.argument.append(self.args[i])
                if self.args[i-9] == "generate" and type(int(self.args[i])) == int:
                    self.argument.append(self.args[i])
                if self.args[i-10] == "generate" and self.args[i] == "--num_vertices":
                    self.argument.append(self.args[i])
                if self.args[i-11] == "generate" and type(int(self.args[i])) == int:
                    self.argument.append(self.args[i])    
                if self.args[i-12] == "generate" and self.args[i] == "--output":
                    self.argument.append(self.args[i])    
                if self.args[i-13] == "generate" and type(self.args[i]) == str:
                    self.argument.append(self.args[i])

            if self.args[i] == "dfs":
                self.argument.append(self.args[i])
                
            
            if self.args[i-1] == "dfs" and self.args[i] == "--root":
                self.argument.append(self.args[i])
            if self.args[i-2] == "dfs" and type(int(self.args[i])) == int:
                self.argument.append(self.args[i])
                
            if self.args[i] == "bfs":
                self.argument.append(self.args[i])
            
            if self.args[i-1] == "bfs" and self.args[i] == "--root":
                self.argument.append(self.args[i])
            if self.args[i-2] == "bfs" and type(int(self.args[i])) == int:
                self.argument.append(self.args[i])
            
            if self.args[i] == "load":
                self.argument.append(self.args[i])
            if self.args[i-1] == "load" and self.args[i] == "--filename":
                self.argument.append(self.args[i])
            if self.args[i-2] == "load" and type(self.args[i]) == str:
                self.argument.append(self.args[i])
    
    def execute(self):
        for i in range(len(self.argument)):
            
            # generate
            if self.argument[i] == "generate": 
                generate = generate_graph.Generate_Graph()
                isOriented = True
                if self.argument[i+1] == "--not_oriented":
                    isOriented = False
                if self.argument[i+1] == "--oriented":
                    isOriented = True
                min_degree = int(self.argument[i+3])
                max_degree = int(self.argument[i+5])
                num_communities = int(self.argument[i+7])
                max_distance = int(self.argument[i+9])
                output = self.argument[i+13]
                num_vertices = int(self.argument[i+11])
                vertices, edges, communities  = generate.generate_graph(isOriented, num_vertices, min_degree, max_degree, num_communities, max_distance)
                generate.save_graph_to_file(output, isOriented, vertices, edges)
                print(f"Graphe généré et enregistré dans {output}")

            #load
            if self.argument[i] == "load":
                loadGraph = Load_graph.LoadGraph()
                filename = self.argument[i + 2]
                print(filename)
                self.vertice, self.matrix = loadGraph.process_graph_file(filename)
                print("Matrice d'adjacence:")
                for row in self.matrix:
                    print(row)
                print("\nListe d'adjacence:")

            #DFS
            if self.argument[i] == "bfs":
                root = int(self.argument[i + 2])
                visited_nodes = BFS.bfs(self.matrix, root)
                print("Nœuds visités:", visited_nodes)




cli = CLI()
cli.check_args()
print(cli.argument)
cli.execute()

                

            



                
                    