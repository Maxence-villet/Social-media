from Tools import Top_Influencer

def main():

    # Test 1: Simple matrix
    MAT = [
        [0, 1, 0, 0], # A follows B
        [1, 0, 1, 1], # B follows A, C, D
        [0, 1, 0, 1], # C follows B, D
        [0, 1, 1, 0]  # D follows B, C
    ]
    SOM = ["Max", 1, "lol", 3]
    # Expected result: ['1']

    # Test 2: Larger matrix
    MAT2 = [[(i + j) % 2 for j in range(20)] for i in range(20)]
    SOM2 = [f"Node_{i}" for i in range(20)]
    # Expected result: ['Node_0', 'Node_1', 'Node_2', 'Node_3', 'Node_4', 'Node_5', 'Node_6', 'Node_7', 'Node_8', 'Node_9', 'Node_10',
    #  'Node_11', 'Node_12', 'Node_13', 'Node_14', 'Node_15', 'Node_16', 'Node_17', 'Node_18', 'Node_19']

    # Test 3: Directed graph with a single influencer
    MAT3 = [
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]
    ]
    SOM3 = ["Alice", "Bob", "Charlie", "David"]
    # Expected result: ['Bob']

    # Test 4: All nodes with equal connections
    MAT4 = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    SOM4 = ["X", "Y", "Z"]
    # Expected result: ["X", "Y", "Z"]

    # Test 5: No connections at all
    MAT5 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    SOM5 = ["Isolé_1", "Isolé_2", "Isolé_3"]
    # Expected result: ["Isolé_1", "Isolé_2", "Isolé_3"]

    # Test 6: One node following all others
    MAT6 = [
        [0, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    SOM6 = ["Leader", "A", "B", "C"]
    # Expected result: ['A', 'B', 'C']

    # Test 7: Circular following
    MAT7 = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]
    ]
    SOM7 = ["A", "B", "C"]
    # Expected result: ["A", "B", "C"]

    # Test 8: Single node graph
    MAT8 = [[0]]
    SOM8 = ["Solo"]
    # Expected result: ["Solo"]

    # Test 9: All nodes follow one
    MAT9 = [
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0]
    ]
    SOM9 = ["Central", "A", "B", "C"]
    # Expected result: ['Central']

    # Test 10: Complex mixed matrix
    MAT10 = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    SOM10 = ["W", "X", "Y", "Z"]
    # Expected result: ["W", "X", "Y", "Z"]

    # Initialize the influencer detection tool
    TOP = Top_Influencer.Top1()

    # Execute all tests
    print("Test 1:", TOP.influencer((SOM, MAT)))
    print("Test 2:", TOP.influencer((SOM2, MAT2)))
    print("Test 3:", TOP.influencer((SOM3, MAT3)))
    print("Test 4:", TOP.influencer((SOM4, MAT4)))
    print("Test 5:", TOP.influencer((SOM5, MAT5)))
    print("Test 6:", TOP.influencer((SOM6, MAT6)))
    print("Test 7:", TOP.influencer((SOM7, MAT7)))
    print("Test 8:", TOP.influencer((SOM8, MAT8)))
    print("Test 9:", TOP.influencer((SOM9, MAT9)))
    print("Test 10:", TOP.influencer((SOM10, MAT10)))

main()
