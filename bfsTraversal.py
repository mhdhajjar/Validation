from collections import deque
from DictRootedGraph import SimpleGraph
from NBits import NBits
from HanoiGraph import HanoiGraph

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

def pred(state, opaque):
    return state == opaque.get("target")

# Exemple avec un graphe représenté par hanois
n = 3
roots = [(tuple(range(n, 0, -1)), (), ())]  
opaque = {"target": tuple([(), tuple(range(n, 0, -1)), ()])} 

hanoi_graph = HanoiGraph(n, roots)
result = bfsTraversal(hanoi_graph, pred, opaque)
print(result)

# Exemple avec un graphe représenté par un dictionnaire
graph_dict = {
    1: [3, 2],
    2: [1, 3, 4],
    3: [3],
    4: []
}
roots = [1]
opaque = {"target": 2}
graph_dict_example = SimpleGraph(graph_dict, roots)
result = bfsTraversal(graph_dict_example, pred, opaque)
print(result)


# Exemple avec un graphe représenté par des bits
N = 5  
roots = [0] 
opaque = {"target": 3}
graph_bits_example = NBits(roots, N)
result = bfsTraversal(graph_bits_example, pred, opaque)
print(result)