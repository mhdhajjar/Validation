class SimpleGraph:
    def __init__(self, graph_dict, roots):
        self.graph_dict = graph_dict  
        self.roots = roots  

    def neighbours(self, S):
        return self.graph_dict.get(S, [])