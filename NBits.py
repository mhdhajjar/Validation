class NBits:
    def __init__(self, roots, N):
        self.roots = roots  
        self.N = N          

    def neighbours(self, S):
        neighbours = []
        for i in range(self.N):
            if S & (1 << i): 
                neighbours.append(i)
        return neighbours