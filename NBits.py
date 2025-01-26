class NBits:
    def __init__(self, roots, N):
        self.roots = roots  
        self.N = N          
    
    def roots(self):
        roots = [0]
        return roots
    
    def neighbours(self, S):
        neighbours = []
        for i in range(self.N):
            if S & (1 << i): 
                neighbours.append(i)
        return neighbours