class Community:
    
    def solo_community(network):
        """
        Determines whether a network is a single community.

        A network is a single community if all nodes are connected to each other.
        This function uses a depth-first traversal (DFS) algorithm to check
        whether all nodes are visited from a starting node.

        Args:
            network: A dictionary representing the network. The keys are the nodes
                    and the values are the lists of their neighbors.

        Returns:
            True if the network is a single community, False otherwise
        """

        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in network[node]:
                if neighbor not in visited:
                    dfs(neighbor)

       
        dfs(list(network.keys())[0])

        
        return len(visited) == len(network)


def main():
    MAT1 = [
        [0, 1, 1],  
        [1, 0, 1],  
        [1, 1, 0]  
    ]
    NODES1 = ["A", "B", "C"]
    
   
    network_1 = {NODES1[i]: [NODES1[j] for j in range(len(MAT1)) if MAT1[i][j] == 1] for i in range(len(MAT1))}
    
    
    print(Community.solo_community(network_1)) 
    
    MAT2 = [
        [0, 1, 0, 0],  
        [1, 0, 0, 0],  
        [0, 0, 0, 1],  
        [0, 0, 1, 0]   
    ]
    NODES2 = ["A", "B", "C", "D"]
    
   
    network_2 = {NODES2[i]: [NODES2[j] for j in range(len(MAT2)) if MAT2[i][j] == 1] for i in range(len(MAT2))}
    
    
    print(Community.solo_community(network_2))  


if __name__ == "__main__":
    main()
