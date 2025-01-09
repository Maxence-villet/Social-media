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

        # Start the path from the first node
        dfs(list(network.keys())[0])

        # Checks if all nodes have been visited
        return len(visited) == len(network)


def main():

   # Network 1 (1 community)
    MAT1 = [
        [0, 1, 1],  
        [1, 0, 1],  
        [1, 1, 0]  
    ]
    NODES1 = ["A", "B", "C"]
    
    # Conversion to adjacency list
    network_1 = {NODES1[i]: [NODES1[j] for j in range(len(MAT1)) if MAT1[i][j] == 1] for i in range(len(MAT1))}
    
    
    print(Community.solo_community(network_1))  # return True
    
   # Network 2 (multiple communities)
    MAT2 = [
        [0, 1, 0, 0],  
        [1, 0, 0, 0],  
        [0, 0, 0, 1],  
        [0, 0, 1, 0]   
    ]
    NODES2 = ["A", "B", "C", "D"]
    
    # Conversion to adjacency list
    network_2 = {NODES2[i]: [NODES2[j] for j in range(len(MAT2)) if MAT2[i][j] == 1] for i in range(len(MAT2))}
    
    
    print(Community.solo_community(network_2))  #return false


if __name__ == "__main__":
   #calls the main() function
    main()
