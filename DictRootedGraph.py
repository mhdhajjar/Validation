class SimpleGraph:
    def __init__(self, graph_dict):
        self.graph_dict = graph_dict    

    def roots(self):
        roots = [1]
        return roots
    
    def neighbours(self, S):
        return self.graph_dict.get(S, [])