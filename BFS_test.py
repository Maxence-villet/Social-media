from Tools import BFS

def main():
    graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
    visited_nodes = BFS.bfs(graph, 'F')
    print("node visited :", visited_nodes)

main()