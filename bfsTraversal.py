from collections import deque
from DictRootedGraph import SimpleGraph
from NBits import NBits
from HanoiGraph import HanoiGraph
from ParentTracer import ParentTracer

def bfsTraversal(graph, pred, opaque, parent_tracer):
    i = True
    k = set()
    F = deque()

    while len(F) > 0 or i:
        if i:
            N = graph.roots
            i = False
            current = None  # Initialisation de current à None (pas utilisé dans la première itération) pour le noeud racine.
        else:
            current = F.popleft()
            N = graph.neighbours(current)

        for n in N:
            if n not in k:
                k.add(n)
                F.append(n)
                if current is not None:  # Vérifier que current est défini avant de l'utiliser
                    parent_tracer.set_parent(n, current)  # Enregistrer le parent
                terminates = pred(n, opaque)
                if terminates:
                    # Reconstruire et retourner la trace avec les autres résultats
                    trace = parent_tracer.get_trace(n)
                    return trace

    return [], opaque, k, F


# Fonction prédicat
def pred(state, opaque):
    return state == opaque.get("target")

# Exemple avec les tours de Hanoï
n = 3
roots = (tuple(range(n, 0, -1)), (), ())
opaque = {"target": ((), tuple(range(n, 0, -1)), ())}

hanoi_graph = HanoiGraph(n, [roots])
parent_tracer = ParentTracer()
result = bfsTraversal(hanoi_graph, pred, opaque, parent_tracer)
print("Hanoi Graph Result:", result)

# Exemple avec un graphe représenté par un dictionnaire
# graph_dict = {
#     1: [3, 2],
#     2: [1, 3, 4],
#     3: [3],
#     4: []
# }
# roots = [1]
# opaque = {"target": 2}
# graph_dict_example = SimpleGraph(graph_dict, roots)
# parent_tracer = ParentTracer()
# result = bfsTraversal(graph_dict_example, pred, opaque, parent_tracer)
# print("Dictionary Graph Result:", result)

# Exemple avec un graphe représenté par des bits
# N = 5
# roots = [0]
# opaque = {"target": 3}
# graph_bits_example = NBits(roots, N)
# parent_tracer = ParentTracer()
# result = bfsTraversal(graph_bits_example, pred, opaque, parent_tracer)
# print("Bits Graph Result:", result)