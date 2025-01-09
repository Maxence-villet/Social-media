from Tools import propagation_path

class PropagationTime:
    def time_path(self, graph_tuple, start, end):
        
        path = propagation_path.PropagationPath()
        path_time = path.best_path(graph_tuple, start, end)
        
        return(str((len(path_time) * 5) - 5) + " sec")
        
        
        
