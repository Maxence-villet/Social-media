import time
import argparse
from Tools import generate_graph

def main():
    parser = argparse.ArgumentParser(description="Générer un graphe aléatoire avec des contraintes.")
    parser.add_argument('--oriented', action='store_true', help="Graphe orienté (par défaut non orienté)")
    parser.add_argument('--num_vertices', type=int, required=True, help="Nombre de sommets")
    parser.add_argument('--min_degree', type=int, required=True, help="Degré minimum des sommets")
    parser.add_argument('--max_degree', type=int, required=True, help="Degré maximum des sommets")
    parser.add_argument('--num_communities', type=int, required=True, help="Nombre de communautés")
    parser.add_argument('--max_distance', type=int, help="Distance maximale entre deux sommets")
    parser.add_argument('--output', type=str, required=True, help="Fichier de sortie")
    
    args = parser.parse_args()
    
    graph = generate_graph.Generate_Graph()
    vertices, edges, communities = graph.generate_graph(
        args.oriented,
        args.num_vertices,
        args.min_degree,
        args.max_degree,
        args.num_communities,
        args.max_distance
    )

    
    
    graph.save_graph_to_file(args.output, args.oriented, vertices, edges)
    print(f"Graphe généré et enregistré dans {args.output}")

if __name__ == "__main__":
    main()
