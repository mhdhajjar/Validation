from collections import deque
from DictRootedGraph import SimpleGraph
from NBits import NBits
from HanoiGraph import HanoiGraph
from ParentTracer import ParentTracer

def bfsTraversal(graph,predicate_finder, opaque):
    i = True
    k = set()
    F = deque()

    while len(F) > 0 or i:
        if i:
            N = graph.roots()
            i = False
            current = None  # Initialisation de current à None (pas utilisé dans la première itération) pour le noeud racine.
        else:
            current = F.popleft()
            N = graph.neighbours(current)

        for n in N:
            if n not in k:
                k.add(n)
                F.append(n)