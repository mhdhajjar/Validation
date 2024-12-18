from collections import deque

def bfsTraversal(graph, pred, opaque):
    i = True 
    k = set()  
    F = deque()  

    while len(F) > 0 or i:
        if i:
            N = graph.roots
            i = False
        else:
            current = F.popleft()
            N = graph.neighbours(current)

        for n in N:
            if n not in k:
                k.add(n)
                F.append(n)
                terminates = pred(n, opaque)
                if terminates:
                    return opaque, k, F

    return opaque, k, F


class SimpleGraph:
    def __init__(self, graph_dict, roots):
        self.graph_dict = graph_dict  
        self.roots = roots  

    def neighbours(self, S):
        return self.graph_dict.get(S, [])


def pred(n, opaque):
    target = opaque.get("target")
    if n == target:
        return True 
    return False


graphe_exemple = {
    1: [3, 2],
    2: [1, 3, 4],
    3: [3],
    4: []
}

roots = [1] 

opaque = {"target": 2}

graph = SimpleGraph(graphe_exemple, roots)

result = bfsTraversal(graph, pred, opaque)
print(result)
