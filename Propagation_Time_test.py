from Tools import Propagation_Time

def main():
    p = Propagation_Time.PropagationTime()

    # Test 1: Simple path between two nodes
    MAT1 = [
        [0, 1, 0, 0],
        [1, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0]
    ]
    SOM1 = ["A", "B", "C", "D"]
    print("Test 1:", p.time_path((SOM1, MAT1), "A", "C"))  # Expected: "10 sec"

    # Test 2: Direct connection
    print("Test 2:", p.time_path((SOM1, MAT1), "D", "C"))  # Expected: "5 sec"

    # Test 3: No connection
    MAT2 = [
        [0, 0],
        [0, 0]
    ]
    SOM2 = ["A", "B"]
    try:
        print("Test 3:", p.time_path((SOM2, MAT2), "A", "B"))
    except ValueError as e:
        print("Test 3 Exception:", e)  # Expected: Exception

    # Test 4: Single node graph
    MAT3 = [[0]]
    SOM3 = ["A"]
    print("Test 4:", p.time_path((SOM3, MAT3), "A", "A"))  # Expected: "0 sec"

    # Test 5: Circular graph
    MAT4 = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]
    ]
    SOM4 = ["X", "Y", "Z"]
    print("Test 5:", p.time_path((SOM4, MAT4), "X", "Z"))  # Expected: "10 sec"

    # Test 6: Larger graph
    MAT5 = [
        [0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 1, 0]
    ]
    SOM5 = ["A", "B", "C", "D", "E"]
    print("Test 6:", p.time_path((SOM5, MAT5), "A", "E"))  # Expected: "10 sec"

    # Test 7: No path available in a larger graph
    print("Test 7:", p.time_path((SOM5, MAT5), "A", "B"))  # Expected: "5 sec"

    # Test 8: Graph with all nodes disconnected
    MAT6 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    SOM6 = ["A", "B", "C"]
    try:
        print("Test 8:", p.time_path((SOM6, MAT6), "A", "C"))  # Expected: Exception
    except ValueError as e:
        print("Test 8 Exception:", e)

    # Test 9: Path within a complete graph
    MAT7 = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    SOM7 = ["A", "B", "C"]
    print("Test 9:", p.time_path((SOM7, MAT7), "A", "C"))  # Expected: "5 sec"

    # Test 10: Edge case with start and end being the same
    print("Test 10:", p.time_path((SOM7, MAT7), "A", "A"))  # Expected: "0 sec"


main()
