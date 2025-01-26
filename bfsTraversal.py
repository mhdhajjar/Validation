from collections import deque
from DictRootedGraph import SimpleGraph
#from HanoiRR import HanoiRR
from NBits import NBits
from HanoiGraph import HanoiGraph
from ParentTracer import ParentTracer

def bfsTraversal(graph, roots, pred, opaque, parent_tracer):
    i = True
    k = set()
    F = deque()

    while len(F) > 0 or i:
        if i:
            N = roots
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
def predicate_finder(noeud, opaque):
    return noeud == opaque.get("target")

# #Exemple avec les tours de Hanoï
# n = 3
# roots = (tuple(range(n, 0, -1)), (), ())
opaque = {"target": ((), tuple(range(n, 0, -1)), ())}

hanoi_graph = HanoiGraph(n, [roots])
parent_tracer = ParentTracer()
result = bfsTraversal(hanoi_graph, predicate_finder, opaque, parent_tracer)
print("Hanoi Graph Result:", result)

# #Exemple avec un graphe représenté par un dictionnaire
# graph_dict = {
#     1: [3, 2],
#     2: [1, 3, 4],
#     3: [3],
#     4: []
# }

# opaque = {"target": 2}

# # Création de l'instance
# graph_dict_example = SimpleGraph(graph_dict)

# # Appel de la méthode roots en lui passant les racines désirées
# #roots = graph_dict_example.roots([1])
# #print(f'roots value: {roots}')
# parent_tracer = ParentTracer()
# result = bfsTraversal(graph_dict_example, predicate_finder, opaque)
# print("Dictionary Graph Result:", result)

#*********************************************************************************************************************
#*********************************************************************************************************************
# Exemple avec un graphe représenté par des bits
# N = 5
# roots = [0]
# opaque = {"target": 3}
# graph_bits_example = NBits(roots, N)
# parent_tracer = ParentTracer()
# result = bfsTraversal(graph_bits_example, pred, opaque, parent_tracer)
# print("Bits Graph Result:", result)
#*********************************************************************************************************************
#*********************************************************************************************************************
