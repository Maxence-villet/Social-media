from Tools import propagation_path

class PropagationTime:
    def time_path(self, graph_tuple, start, end):
        """
        This fonction collect the path between two nodes in the propagation path module and Addition 5 min for each nodes passed

        Args:
        ------
        [graph_tuple] (tuple of a list and of a list of a list) : a tuple where we can find our matrix and our nodes
        [end] (str or int or float) : the node where the path must end
        [graph_tuple] (tuple of a list and of a list of a list) : a tuple where we can find our matrix and our nodes

        Returns:
        ---------
        (str) : the time with his minute measure
        """
        path = propagation_path.PropagationPath() # Propagation_path instancy
        path_time = path.best_path(graph_tuple, start, end) # collect the path between the node start and end with the propagationPath module
        
        return(str((len(path_time) * 5) - 5) + " min")
        
        
        
