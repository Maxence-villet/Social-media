from Tools import generate_graph, DFS, BFS, Load_graph, Top_Influencer, propagation_path, Propagation_Time
import sys

class CLI:
    def __init__(self):
        """
        Initializes the CLI class and retrieves the command-line arguments.
        """
        self.argument = []
        self.args = sys.argv
        self.matrix = list[list[int]]
        self.vertices = []

    def check_args(self):
        """
        Checks the command-line arguments and stores them in a list.

        Args:
        -----
        self.args (list) : List of command-line arguments.

        Returns:
        --------
        None
        """

        for i in range(len(self.args)):
            try:
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
            except Exception as e:
                print(f"Il vous manque des arguments pour générer le graphe, veuillez vous référez à la documentation pdf. Error : {e}")

            try:
                if self.args[i] == "dfs":
                    self.argument.append(self.args[i])
            
                if self.args[i-1] == "dfs" and self.args[i] == "--root":
                    self.argument.append(self.args[i])
                if self.args[i-2] == "dfs":
                    self.argument.append(self.args[i])
            except Exception as e:
                print(f"Il vous manque des arguments pour faire le DFS, veuillez vous référez à la documentation pdf. Error : {e}")

            try:        
                if self.args[i] == "bfs":
                    self.argument.append(self.args[i])
                
                if self.args[i-1] == "bfs" and self.args[i] == "--root":
                    self.argument.append(self.args[i])
                if self.args[i-2] == "bfs":
                    self.argument.append(self.args[i])
            except Exception as e:
                print(f"Il vous manque des arguments pour faire le BFS, veuillez vous référez à la documentation pdf. Error : {e}")
    
            try:
                if self.args[i] == "load":
                    self.argument.append(self.args[i])
                if self.args[i-1] == "load" and self.args[i] == "--filename":
                    self.argument.append(self.args[i])
                if self.args[i-2] == "load":
                    self.argument.append(self.args[i])
            except Exception as e:
                print(f"Il vous manque des arguments pour charger le fichier txt, veuillez vous référez à la documentation pdf. Error : {e}")
    
            try:
                if self.args[i] == "top-influenceur":
                    self.argument.append(self.args[i])
            except Exception as e:
                print(f"Il vous manque des arguments pour avoir le top influenceur, veuillez vous référez à la documentation pdf. Error : {e}")
    
            try:
                if self.args[i] == "propage":
                    self.argument.append(self.args[i])
                if self.args[i-1] == "propage" and self.args[i] == "--start":
                    self.argument.append(self.args[i])
                if self.args[i-2] == "propage":
                    self.argument.append(self.args[i])
                if self.args[i-3] == "propage" and self.args[i] == "--end":
                    self.argument.append(self.args[i])
                if self.args[i-4] == "propage":
                    self.argument.append(self.args[i])
            except Exception as e:
                print(f"Il vous manque des arguments pour avoir le chemin de propagation, veuillez vous référer à la documentation pdf. Error : {e}")
            
            try:
                if self.args[i] == "time":
                    self.argument.append(self.args[i])
                if self.args[i-1] == "time" and self.args[i] == "--start":
                    self.argument.append(self.args[i])
                if self.args[i-2] == "time":
                    self.argument.append(self.args[i])
                if self.args[i-3] == "time" and self.args[i] == "--end":
                    self.argument.append(self.args[i])
                if self.args[i-4] == "time":
                    self.argument.append(self.args[i])    
            except Exception as e:
                print(f"Il vous manque des arguments pour avoir le temps de propagation, veuillez vous référer à la documentation pdf. Error : {e}")
    
            # if self.args[i] == "--arcs-list":
            #     self.argument.append(self.args[i])
            
            # if self.args[i] == "--arcs-matrice":
            #     self.argument.append(self.args[i])
            
            # if self.args[i] == "--edges-list":
            #     self.argument.append(self.args[i])
            
            # if self.args[i] == "--edges-matrice":
            #     self.argument.append(self.args[i])
            

    
    def execute(self):
        """
        Executes commands based on the command-line arguments provided.

        Args:
        -----
        self.argument (list) : List of validated arguments.

        Returns:
        --------
        None
        """
        for i in range(len(self.argument)): 
            try:
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
                    generate.generate_graph(isOriented, num_vertices, min_degree, max_degree, num_communities, max_distance)
                    generate.save_graph_to_file(output)
                    print(f"Graphe généré et enregistré dans {output}")
            except Exception as e:
                print(f"Une erreur inattendu est survenue lors de la génération du graphe, veuillez vous référer à la documentation pdf. Erreur : {e}")
            try:
                #load
                if self.argument[i] == "load":
                    loadGraph = Load_graph.LoadGraph()
                    filename = self.argument[i + 2]
                    self.vertices, self.matrix = loadGraph.process_graph_file(filename)
                    print(f"Fichier {filename} chargée avec succès")
            except Exception as e:
                print(f"Une erreur inattendu est survenue lors du chargement du fichier, veuillez vous référer à la documentation pdf. Erreur : {e}")
            
            try:
                #DFS
                if self.argument[i] == "dfs":
                    root = self.argument[i + 2]
                    dfs = DFS.Dfs()
                    print(f"DFS : {dfs.visited_dfs((self.vertices, self.matrix), str(root))}")
            except Exception as e:
                print(f"Une erreur inattendu est survenue lors l'éxécution du DFS, veuillez vous référer à la documentation pdf. Erreur : {e}")
            
            
            try:
                #BFS
                if self.argument[i] == "bfs":
                    root = self.argument[i + 2]
                    bfs = BFS.BFS()
                    print(f"BFS : {bfs.bfs((self.vertices, self.matrix), str(root))}")
            except Exception as e:
                print(f"Une erreur inattendu est survenue lors de l'éxécution du BFS, veuillez vous référer à la documentation pdf. Erreur : {e}")
                    
            try:
                # Top Influenceur
                if self.argument[i] == "top-influenceur":
                    top_influenenceur = Top_Influencer.Top1()
                    print(f"TOP INFLUENCEUR : {top_influenenceur.influencer((self.vertices, self.matrix))}")
            except Exception as e:
                print(f"Une erreur inattendu est survenue lors de l'éxécution du Top-influenceur', veuillez vous référer à la documentation pdf. Erreur : {e}")
            
            try:
                # Propagation path
                if self.argument[i] == "propage":
                    start = self.argument[i+2]
                    end = self.argument[i+4]
                    propage = propagation_path.PropagationPath()
                    print(f"PROPAGATION PATH : {propage.best_path((self.vertices, self.matrix), start, end)}")
            except Exception as e:
                print(f"Une erreur inattendu est survenue lors de l'éxécution du chemin de propagation, veuillez vous référer à la documentation pdf. Erreur : {e}")

            try:    
                #time
                if self.argument[i] == "time":
                    start = self.argument[i+2]
                    end = self.argument[i+4]
                    time = Propagation_Time.PropagationTime()
                    print(f"PROPAGATION TIME : {time.time_path((self.vertices, self.matrix), start, end)}")
            except Exception as e:
                print(f"Une erreur inattendu est survenue lors de l'éxécution du temps de propagation, veuillez vous référer à la documentation pdf. Erreur : {e}")
            
            # #Arcs
            # if self.argument[i] == "--arcs-list":
            #     arc = arcs.Arcs()
            #     print(arc.count_list(self.vertices))
            # if self.argument[i] == "--arcs-matrice":
            #     arc = arcs.Arcs()
            #     print(arc.count_matrix(self.matrix))





                

            



                
                    