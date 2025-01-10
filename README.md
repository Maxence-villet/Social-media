# Social-media

The 'Edge' class has several functions, such as 'count_matrix'. This function goes through a connection matrix and, if it finds a value of 1, it adds 1 to a counter and then divides the final count by 2. The 'count_list' function counts the connections and goes through a connection list, adding 1 for each connection found and then returns a list of all the connections.

This class is used to determine which points are connected and to connect them with lines.

The 'Queue' class is used to create lines. You can add items to the end of the line or remove items from the beginning. The 'Stack' class, on the other hand, is like a stack of plates. You add new plates to the top and remove plates from the top. These classes return a list of items.

The 'Arc' class counts the edges between vertices, enabling us to determine the number of edges connected to each vertex.

The 'BFS' class  performs a breadth-first search (BFS) on a given graph using a list as the queue.
Neighbors are visited in a sorted order.

The 'community' class determines whether a network is a single community or not.

The 'DFS' class starts from a starting node and searches in depth for other vertices having edges in common and then visits the neighbors.

The 'generate graph' class allows you to generate graphs by taking into account the orientation of the graph (oriented or not), the minimum degrees, the maximum degrees, the number of communities as well as the maximum distance between the vertices.

The 'stack' class allows you to remove the last one that was added to the list, unlike the 'queue' class which allows you to remove the first one to arrive in the list.

The 'Loadgraph' class allows to examine the graph and then it returns a list of adjacency and matrix in column form.