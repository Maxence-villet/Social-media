from Tools import propagation_path

def main():
    # Test 1: Simple path between two nodes
    MAT1 = [
        [0, 1, 0, 0],  # A follows B
        [1, 0, 1, 1],  # B follows A, C, D
        [0, 1, 0, 1],  # C follows B, D
        [0, 1, 1, 0]   # D follows B, C
    ]
    SOM1 = ["A", "B", "C", "D"]
    start1 = "A"
    end1 = "C"
    # Expected result: ['A', 'B', 'C']

    # Test 2: No path between two nodes
    MAT2 = [
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    SOM2 = ["A", "B", "C", "D"]
    start2 = "A"
    end2 = "C"
    # Expected result: ValueError with message "No path found between A and C"

    # Test 3: Path in a larger graph
    MAT3 = [
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0]
    ]
    SOM3 = ["A", "B", "C", "D", "E"]
    start3 = "A"
    end3 = "E"
    # Expected result: ['A', 'B', 'C', 'D', 'E']

    # Test 4: Single node graph
    MAT4 = [[0]]
    SOM4 = ["A"]
    start4 = "A"
    end4 = "A"
    # Expected result: ['A']

    # Test 5: Path with multiple possible routes
    MAT5 = [
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]
    SOM5 = ["A", "B", "C", "D"]
    start5 = "A"
    end5 = "D"
    # Expected result: ['A', 'B', 'D'] or ['A', 'C', 'D']

    # Test 6: Path in a circular graph
    MAT6 = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]
    ]
    SOM6 = ["A", "B", "C"]
    start6 = "A"
    end6 = "C"
    # Expected result: ['A', 'B', 'C']

    # Test 7: No path in a disconnected graph
    MAT7 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    SOM7 = ["A", "B", "C"]
    start7 = "A"
    end7 = "C"
    # Expected result: ValueError with message "No path found between A and C"

    # Test 8: Graph with multiple paths, testing BFS behavior
    MAT8 = [
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]
    SOM8 = ["A", "B", "C", "D"]
    start8 = "A"
    end8 = "D"
    # Expected result: ['A', 'B', 'C', 'D']

    # Test 9: Path in a directed graph
    MAT9 = [
        [0, 1],
        [0, 0]
    ]
    SOM9 = ["A", "B"]
    start9 = "A"
    end9 = "B"
    # Expected result: ['A', 'B']

    # Test 10: Multiple nodes, no valid start/end
    MAT10 = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    SOM10 = ["A", "B", "C"]
    start10 = "A"
    end10 = "C"
    # Expected result: ValueError with message "No path found between A and C"

    # Create an instance of PropagationPath
    top_path = propagation_path.PropagationPath()

    # Execute all tests
    print("Test 1:", top_path.best_path((SOM1, MAT1), start1, end1))  # Expected: ['A', 'B', 'C']


    try:
        print("Test 2:", top_path.best_path((SOM2, MAT2), start2, end2))  # Expected: ValueError
    except ValueError as e:
        print(f"Test 2 Error: {e}")

    try:
        print("Test 3:", top_path.best_path((SOM3, MAT3), start3, end3))  # Expected: ['A', 'B', 'C', 'D', 'E']
    except ValueError as e:
        print(f"Test 3 Error: {e}")

    try:
        print("Test 4:", top_path.best_path((SOM4, MAT4), start4, end4))  # Expected: ['A']
    except ValueError as e:
        print(f"Test 4 Error: {e}")

    try:
        print("Test 5:", top_path.best_path((SOM5, MAT5), start5, end5))  # Expected: ['A', 'B', 'D'] or ['A', 'C', 'D']
    except ValueError as e:
        print(f"Test 5 Error: {e}")

    try:
        print("Test 6:", top_path.best_path((SOM6, MAT6), start6, end6))  # Expected: ['A', 'B', 'C']
    except ValueError as e:
        print(f"Test 6 Error: {e}")

    try:
        print("Test 7:", top_path.best_path((SOM7, MAT7), start7, end7))  # Expected: ValueError
    except ValueError as e:
        print(f"Test 7 Error: {e}")

    try:
        print("Test 8:", top_path.best_path((SOM8, MAT8), start8, end8))  # Expected: ['A', 'B', 'C', 'D']
    except ValueError as e:
        print(f"Test 8 Error: {e}")

    try:
        print("Test 9:", top_path.best_path((SOM9, MAT9), start9, end9))  # Expected: ['A', 'B']
    except ValueError as e:
        print(f"Test 9 Error: {e}")

    try:
        print("Test 10:", top_path.best_path((SOM10, MAT10), start10, end10))  # Expected: ValueError
    except ValueError as e:
        print(f"Test 10 Error: {e}")

main()
