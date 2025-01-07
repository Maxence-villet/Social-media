from Tools import BFS

def main():
    graph = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [4], 4: [3]}
    visited_nodes = BFS.bfs(graph, 1)
    print("Nœuds visités:", visited_nodes)

main()