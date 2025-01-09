from Tools import BFS

def main():
    # Test 1: Simple graph (starting from 'B')
    # Define the graph with a list of nodes (SOM1) and an adjacency matrix (MAT1)
    SOM1 = ["A", "B", "C", "D"]
    MAT1 = [
        [0, 1, 0, 0],  # A is connected to B
        [1, 0, 1, 1],  # B is connected to A, C, D
        [0, 1, 0, 1],  # C is connected to B, D
        [0, 1, 1, 0]   # D is connected to B, C
    ]
    graph1 = (SOM1, MAT1)  # The graph is a tuple containing the nodes and adjacency matrix
    bfs = BFS.BFS()
    result1 = bfs.bfs(graph1, "B")
    print("Test 1 (Expected: ['B', 'A', 'C', 'D']) - BFS result (starting from 'B'):", result1)

    # Test 2: Disconnected graph (starting from 'A')
    SOM2 = ["A", "B", "C", "D", "E"]
    MAT2 = [
        [0, 1, 0, 0, 0],  # A is connected to B
        [1, 0, 1, 1, 0],  # B is connected to A, C, D
        [0, 1, 0, 0, 0],  # C is connected to B
        [0, 1, 0, 0, 0],  # D is connected to B
        [0, 0, 0, 0, 0]   # E has no neighbors (isolated)
    ]
    graph2 = (SOM2, MAT2)
    result2 = bfs.bfs(graph2, "A")
    print("Test 2 (Expected: ['A', 'B', 'C', 'D']) - BFS result (starting from 'A') in disconnected graph:", result2)

    # Test 3: Fully connected graph (starting from 'C')
    SOM3 = ["A", "B", "C", "D"]
    MAT3 = [
        [0, 1, 1, 1],  # A is connected to B, C, D
        [1, 0, 1, 1],  # B is connected to A, C, D
        [1, 1, 0, 1],  # C is connected to A, B, D
        [1, 1, 1, 0]   # D is connected to A, B, C
    ]
    graph3 = (SOM3, MAT3)
    result3 = bfs.bfs(graph3, "C")
    print("Test 3 (Expected: ['C', 'A', 'B', 'D']) - BFS result (starting from 'C') in fully connected graph:", result3)

    # Test 4: Isolated node (starting from 'A')
    SOM4 = ["A", "B", "C"]
    MAT4 = [
        [0, 0, 0],  # A is not connected to anyone
        [0, 0, 1],  # B is connected to C
        [0, 1, 0]   # C is connected to B
    ]
    graph4 = (SOM4, MAT4)
    result4 = bfs.bfs(graph4, "A")
    print("Test 4 (Expected: ['A']) - BFS result (starting from 'A') with isolated node:", result4)

    # Test 5: Single node graph (starting from 'A')
    SOM5 = ["A"]
    MAT5 = [
        [0]  # A is not connected to anyone
    ]
    graph5 = (SOM5, MAT5)
    result5 = bfs.bfs(graph5, "A")
    print("Test 5 (Expected: ['A']) - BFS result (starting from 'A') with single node graph:", result5)

    # Test 6: No neighbors (graph with no edges, starting from 'A')
    SOM6 = ["A", "B", "C"]
    MAT6 = [
        [0, 0, 0],  # A is not connected to anyone
        [0, 0, 0],  # B is not connected to anyone
        [0, 0, 0]   # C is not connected to anyone
    ]
    graph6 = (SOM6, MAT6)
    result6 = bfs.bfs(graph6, "A")
    print("Test 6 (Expected: ['A']) - BFS result (starting from 'A') with no edges:", result6)

    # Test 7: Linear graph (starting from 'A')
    SOM7 = ["A", "B", "C", "D"]
    MAT7 = [
        [0, 1, 0, 0],  # A is connected to B
        [1, 0, 1, 0],  # B is connected to A, C
        [0, 1, 0, 1],  # C is connected to B, D
        [0, 0, 1, 0]   # D is connected to C
    ]
    graph7 = (SOM7, MAT7)
    result7 = bfs.bfs(graph7, "A")
    print("Test 7 (Expected: ['A', 'B', 'C', 'D']) - BFS result (starting from 'A') in linear graph:", result7)

    # Test 8: Circular graph (starting from 'A')
    SOM8 = ["A", "B", "C", "D"]
    MAT8 = [
        [0, 1, 0, 0],  # A is connected to B
        [1, 0, 1, 0],  # B is connected to A, C
        [0, 1, 0, 1],  # C is connected to B, D
        [0, 0, 1, 0]   # D is connected to C
    ]
    graph8 = (SOM8, MAT8)
    result8 = bfs.bfs(graph8, "A")
    print("Test 8 (Expected: ['A', 'B', 'C', 'D']) - BFS result (starting from 'A') in circular graph:", result8)

    # Test 9: Graph with multiple components (starting from 'A')
    SOM9 = ["A", "B", "C", "D", "E"]
    MAT9 = [
        [0, 1, 0, 0, 0],  # A is connected to B
        [1, 0, 1, 1, 0],  # B is connected to A, C, D
        [0, 1, 0, 0, 0],  # C is connected to B
        [0, 1, 0, 0, 0],  # D is connected to B
        [0, 0, 0, 0, 0]   # E is isolated
    ]
    graph9 = (SOM9, MAT9)
    result9 = bfs.bfs(graph9, "A")
    print("Test 9 (Expected: ['A', 'B', 'C', 'D']) - BFS result (starting from 'A') in multi-component graph:", result9)

main()
