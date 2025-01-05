class HanoiGraph:
    def __init__(self, n, roots):
        self.n = n  
        self.roots = roots  
        self.goal = tuple([tuple(range(n, 0, -1)), (), ()])  

    def neighbours(self, state):
        neighbours = []
        state = [list(stack) for stack in state] # state représente les batons
        
        for i in range(3):
            if state[i]:
                for j in range(3):
                    if i != j:  
                        if not state[j] or state[i][-1] < state[j][-1]: # state[i][-1] représente le disque le plus sur le baton
                            new_state = [list(stack) for stack in state]  
                            disk = new_state[i].pop()  
                            new_state[j].append(disk)  
                            neighbours.append(tuple(tuple(stack) for stack in new_state))  
        return neighbours