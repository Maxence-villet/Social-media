from Tools import community

def main():
  
    MAT1 = [
        [0, 1, 1],  
        [1, 0, 1],  
        [1, 1, 0]  
    ]
    NODES1 = ["A", "B", "C"]

   
    network_1 = {NODES1[i]: [NODES1[j] for j in range(len(MAT1)) if MAT1[i][j] == 1] for i in range(len(MAT1))}
    print(community.Community.solo_community(network_1))  

    
    MAT2 = [
        [0, 1, 0, 0],  
        [1, 0, 0, 0],  
        [0, 0, 0, 1],  
        [0, 0, 1, 0]   
    ]
    NODES2 = ["A", "B", "C", "D"]

    
    network_2 = {NODES2[i]: [NODES2[j] for j in range(len(MAT2)) if MAT2[i][j] == 1] for i in range(len(MAT2))}
    print(community.Community.solo_community(network_2)) 

if __name__ == "__main__":
    main()
