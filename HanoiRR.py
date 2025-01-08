class HanoiRR:
    def __init__(self, n):
        self.n = n  
        self.roots = self.initial()  # Initialisation des racines via la méthode root
        self.goal = tuple([tuple(range(n, 0, -1)), (), ()])  

    def initial(self):
        return (tuple(range(self.n, 0, -1)), (), ())

    def actions(self, state):
        possible_actions = []
        state = [list(stack) for stack in state] 

        for i in range(3):  
            if state[i]:  
                for j in range(3):  
                    if i != j:  
                        if not state[j] or state[i][-1] < state[j][-1]:
                            possible_actions.append((i, j))  

        return possible_actions

    def execute(self, state, action):
        source, destination = action
        state = [list(stack) for stack in state]  

        disk = state[source].pop()
        state[destination].append(disk)

        return tuple(tuple(stack) for stack in state)
